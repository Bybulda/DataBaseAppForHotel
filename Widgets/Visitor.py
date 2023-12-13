import configparser
import sys
import datetime
import os.path as path

import psycopg2
from query.visitorQuery import *
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QCalendarWidget, \
    QVBoxLayout, QWidget, QFormLayout, QComboBox, QMessageBox, QTabWidget, QLabel, QTableWidget, QTableWidgetItem, \
    QFileDialog


def validate_info(name, phone, passport):
    if name == '' or phone == '' or passport == '':
        return False
    splitter = name.split()
    if len(splitter) == 3:
        sm = sum(0 if i.isalpha() else 1 for i in splitter)
        if sm == 0:
            if len(passport) == 10:
                return True
    return False


class HotelBookingApp(QMainWindow):
    def __init__(self, config_file='../config/config.ini'):
        super().__init__()
        self.last_booking_info = {"SNP": '', "Gender": '', "Price": 0, "Room_type": "",
                                  "Room_id": 0, "Passport": '', "Telephone": '',
                                  "Date_start": '', "Date_end": ''}
        self.status_booking = False
        self.open_connection(config_file)

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hotel Booking App')

        self.tab_widget = QTabWidget()

        book_action = self.show_book_room()
        self.tab_widget.addTab(book_action, 'Забронировать/Отменить номер')

        view_action = self.show_view()
        self.tab_widget.addTab(view_action, 'Просмотреть брони')

        receipt_action = self.show_receipt()

        self.tab_widget.addTab(receipt_action, 'Получить чек')
        self.setCentralWidget(self.tab_widget)

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def open_connection(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        self.conn = psycopg2.connect(user=config.get("databaseN", "username"),
                                     password=config.getint("databaseN", "password"),
                                     host=config.get("databaseN", "host"),
                                     port=config.get("databaseN", "port"),
                                     database=config.get("databaseN", "database"),
                                     options="-c search_path=" + config.get("databaseN", "schema"))
        self.cur = self.conn.cursor()

    # region booking
    def show_book_room(self):
        # Создание виджетов для ввода данных
        self.bookin_option = QComboBox(self)
        self.bookin_option.addItems(['Забронировать', 'Отменить бронь'])
        self.bookin_option.currentIndexChanged.connect(self.update_booking)
        self.name_input = QLineEdit(self)
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(['Мужской', 'Женский'])
        self.passport_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.room_type_input = QComboBox(self)
        self.room_type_input.addItems(['Classic', 'Comfort', 'Lux'])
        self.start_date_input = QCalendarWidget(self)
        self.end_date_input = QCalendarWidget(self)

        # Создание кнопки для бронирования
        self.book_button = QPushButton('Забронировать', self)
        self.book_button.clicked.connect(self.book_action)

        # Создание формы
        form_layout = QFormLayout()
        form_layout.addRow('Опция', self.bookin_option)
        form_layout.addRow('ФИО:', self.name_input)
        form_layout.addRow('Пол:', self.gender_input)
        form_layout.addRow('Паспорт:', self.passport_input)
        form_layout.addRow('Телефон:', self.phone_input)
        form_layout.addRow('Тип комнаты:', self.room_type_input)
        form_layout.addRow('Дата начала:', self.start_date_input)
        form_layout.addRow('Дата конца:', self.end_date_input)
        form_layout.addRow(self.book_button)

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)

        # Основной виджет
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        return main_widget

    def update_booking(self):
        text = self.bookin_option.currentText()
        self.book_button.setText(text)

    def succesffull_booking(self, book_info):
        self.receipt.setText(
            f'Уважаемый гость: {book_info[0]}, вы успешно забронировали комнату!\nБронирование содержит следующую информацию:\n '
            f'ФИО посетителя: {book_info[0]}\n'
            f'Пол: {book_info[1]}\n'
            f'Паспорт: {book_info[5]}\nТип комнаты: {book_info[3]}\n'
            f'Дата заселения: {book_info[-2]}\n'
            f'Дата выселения: {book_info[-1]}\nСтоимость: {book_info[2]}')
        for i, key in enumerate(self.last_booking_info.keys()):
            self.last_booking_info[key] = book_info[i]

    def book_room(self, name, phone, passport, gender, room_type, start_date, end_date):
        if not validate_info(name, phone, passport):
            self.show_box("Ошибка", "Вы ввели некорректные данные, попробуйте ещё раз!")
            return
        surname, name_, patron = [(i.lower()).capitalize() for i in name.split()]
        start_date, end_date = '-'.join(str(i) for i in start_date), '-'.join(str(i) for i in end_date)
        start_d, end_d = datetime.datetime.strptime(start_date, "%Y-%m-%d"), datetime.datetime.strptime(end_date, "%Y-%m-%d")
        if start_d > end_d:
            self.show_box("Ошибка", "Вы дата начала бронирования должна идти до даты конца бронирования!")
            return

        try:
            self.cur.execute(serach_query, (name_, surname, patron, str(passport)))
            srch = self.cur.fetchone()
            if srch is None:
                self.cur.execute(insrt_vis, (name_, surname, patron, passport, phone, gender.lower()))
                self.conn.commit()
                self.cur.execute(serach_query, (name_, surname, patron, passport))
                srch = self.cur.fetchone()
            self.cur.execute(search_room_time, (room_type.lower(), start_date, end_date, start_date, end_date,
                                                start_date, end_date, start_date, end_date))
            room_id = self.cur.fetchone()
            if room_id is None:
                self.show_box('Внимание', 'На текущий промежуток нет свободных комнат!')
                return
            self.cur.execute(insrt_book, (srch[0], int(room_id[0]), start_date, end_date))
            self.conn.commit()
            self.cur.execute(room_price, (room_type.lower(),))
            price = self.cur.fetchone()[0]
            real_price = ((datetime.datetime.strptime(end_date, "%Y-%m-%d")
                          - datetime.datetime.strptime(start_date, "%Y-%m-%d")).days + 1) * int(price)
            self.succesffull_booking(
                [name, gender, str(real_price), room_type, str(room_id), str(passport), phone, start_date, end_date])
            self.show_box('Информация', 'Вы успешно забронировали номер!')
        except Exception:
            self.show_box('Что-то пошло не так', 'Пожалуйста повторите позже!')

    def cancel_room(self, name, phone, passport, room_type, start_date, end_date):
        if not validate_info(name, phone, passport):
            self.show_box("Ошибка", "Вы ввели некорректные данные, попробуйте ещё раз!")
            return
        surname, name_, patron = [(i.lower()).capitalize() for i in name.split()]
        start_date, end_date = '-'.join(str(i) for i in start_date), '-'.join(str(i) for i in end_date)
        try:
            self.cur.execute(search_booking_pos, (passport, start_date, end_date))
            res = self.cur.fetchone()
            if res is None:
                self.show_box("Ошибка", "Вы не никогда не бронировали номер в нашем отеле или были удалены из базы!")
                return
            self.cur.execute(cancel_booking, (res[0],))
            self.conn.commit()
            self.last_booking_info = {"SNP": '', "Gender": '', "Price": 0, "Room_type": "",
                                  "Room_id": 0, "Passport": '', "Telephone": '',
                                  "Date_start": '', "Date_end": ''}
            self.receipt.setText("Вы отменили бронь, но здесь всё также будет отображаться информация о бронировании!")
            self.show_box('Информация', "Вы успешно отменили бронь!")
        except Exception:
            self.show_box('Ошибка',
                          'Внимание, скорее всего вы ошиблись при вводе данных, убедитесь что всё ввели правильно!')

    def book_action(self):
        # Получение данных из полей ввода
        name = self.name_input.text()
        gender = self.gender_input.currentText()
        passport = self.passport_input.text()
        phone = self.phone_input.text()
        room_type = self.room_type_input.currentText()
        start_date = self.start_date_input.selectedDate().getDate()
        end_date = self.end_date_input.selectedDate().getDate()
        if self.book_button.text() == "Забронировать":
            self.book_room(name, phone, passport, gender, room_type, start_date, end_date)
        else:
            self.cancel_room(name, phone, passport, room_type, start_date, end_date)

    # endregion

    def show_view(self):
        self.name_view = QLineEdit(self)
        self.gender_view = QComboBox(self)
        self.gender_view.addItems(["Мужской", "Женский"])
        self.passport_view = QLineEdit(self)

        # Создание кнопки для бронирования
        self.view_button = QPushButton('Просмотреть все брони', self)
        self.view_button.clicked.connect(self.show_view_dialog)
        self.booking_table = QTableWidget(self)
        self.booking_table.setColumnCount(4)
        self.booking_table.setHorizontalHeaderLabels(["ФИО", "Номер комнаты", "Дата заселения", "Дата выселения"])

        # Создание формы
        form_layout = QFormLayout()
        form_layout.addRow('ФИО:', self.name_view)
        form_layout.addRow('Пол:', self.gender_view)
        form_layout.addRow('Паспорт:', self.passport_view)
        form_layout.addRow(self.booking_table)
        form_layout.addRow(self.view_button)

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)

        # Основной виджет
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        return main_widget

    def show_view_dialog(self):
        try:
            self.booking_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
            passport = int(self.passport_view.text())
            surname, name, patr = self.name_view.text().split()
            self.cur.execute(query, (passport, name, surname, patr))
            res = self.cur.fetchall()
            self.booking_table.setRowCount(0)
            for row, value in enumerate(res):
                self.booking_table.insertRow(row)
                self.booking_table.setItem(row, 0, QTableWidgetItem(self.name_view.text()))
                for col in range(1, len(value) + 1):
                    self.booking_table.setItem(row, col, QTableWidgetItem(str(value[col - 1])))

        except Exception:
            self.show_box('Ошибка', 'Скорее всего вы допустили ошибку в указании данных, проверьте их ещё раз')

    def show_box(self, title, message):
        cancel_dialog = QMessageBox(self)
        cancel_dialog.setWindowTitle(title)
        cancel_dialog.setText(message)
        cancel_dialog.exec()

    def get_receiption(self):
        if self.last_booking_info['SNP'] == '':
            self.show_box('Внимание', 'Вы не бронировали комнату или уже отменили на неё бронь!')
            return
        directory = QFileDialog.getExistingDirectory(
            self,
            "Выберите папку для сохранения чека:"
        )

        with open(path.join(f'{directory}', f'{self.last_booking_info["SNP"]}_receipt.txt'), encoding='utf-8', mode='w') as file:
            file.write(f'Гость: {self.last_booking_info["SNP"]}\nПаспорт: {self.last_booking_info["Passport"]}\n'
                       f'Телефон: {self.last_booking_info["Telephone"]}\n'
                       f'Пол: {self.last_booking_info["Gender"]}\n'
                       f'Номер комнаты: {self.last_booking_info["Room_id"]}\n'
                       f'Тип комнаты: {self.last_booking_info["Room_type"]}\n'
                       f'Стоимость: {self.last_booking_info["Price"]}\n'
                       f'Дата заселения: {self.last_booking_info["Date_start"]}\n'
                       f'Дата выселения: {self.last_booking_info["Date_end"]}\n')
        self.show_box('Информация', 'Спасибо что вы с нами!')

    def show_receipt(self):
        # Окно для получения чека
        self.receipt = QLabel("Здесь будет отображаться информация о бронировании.", self)
        self.receipt.setStyleSheet(''' font-size: 16px; 
        ''')
        self.get_reciept = QPushButton("Получить чек в формате txt")
        self.get_reciept.clicked.connect(self.get_receiption)
        self.receipt.setAlignment(Qt.AlignmentFlag.AlignJustify | Qt.AlignmentFlag.AlignHCenter)
        self.receipt.setWordWrap(False)
        layout = QVBoxLayout(self)
        layout.addWidget(self.receipt)
        layout.addWidget(self.get_reciept)
        main_widget = QWidget()
        main_widget.setLayout(layout)
        return main_widget


def main():
    app = QApplication(sys.argv)
    window = HotelBookingApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
