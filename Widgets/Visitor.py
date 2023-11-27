import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QCalendarWidget, \
    QVBoxLayout, QWidget, QFormLayout, QComboBox, QMessageBox, QTabWidget


class HotelBookingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.last_booking_info = {"SNP": '', "Price": 0, "Room_type": "", "Room_id": 0, "Date_start": '',
                                  "Date_end": ''}

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Hotel Booking App')

        self.tab_widget = QTabWidget()

        book_action = self.show_book_room()
        self.tab_widget.addTab(book_action, 'Забронировать номер')

        cancel_action = self.show_cancel()
        self.tab_widget.addTab(cancel_action, 'Отменить бронь')

        view_action = self.show_view()
        self.tab_widget.addTab(view_action, 'Просмотреть брони')

        receipt_action = QPushButton('Получить чек')
        receipt_action.clicked.connect(self.show_receipt_dialog)
        self.tab_widget.addTab(receipt_action, 'Получить чек')
        self.setCentralWidget(self.tab_widget)

    # region booking
    def show_book_room(self):
        # Создание виджетов для ввода данных
        self.name_input = QLineEdit(self)
        self.gender_input = QComboBox(self)
        self.gender_input.addItems(['Male', 'Female', 'Other'])
        self.passport_input = QLineEdit(self)
        self.phone_input = QLineEdit(self)
        self.room_type_input = QComboBox(self)
        self.room_type_input.addItems(['Classic', 'Comfort', 'Lux'])
        self.start_date_input = QCalendarWidget(self)
        self.end_date_input = QCalendarWidget(self)

        # Создание кнопки для бронирования
        self.book_button = QPushButton('Забронировать', self)
        self.book_button.clicked.connect(self.book_room)

        # Создание формы
        form_layout = QFormLayout()
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

    def book_room(self):
        # Получение данных из полей ввода
        name = self.name_input.text()
        gender = self.gender_input.currentText()
        passport = self.passport_input.text()
        phone = self.phone_input.text()
        room_type = self.room_type_input.currentText()
        start_date = self.start_date_input.selectedDate().toString('yyyy-MM-dd')
        end_date = self.end_date_input.selectedDate().toString('yyyy-MM-dd')

        # Здесь можно добавить логику для обработки данных (например, отправка запроса на сервер или сохранение в базе данных)
        print(f'Бронирование: {name}, {gender}, {passport}, {phone}, {room_type}, {start_date}, {end_date}')
        self.show_book_dialog(True)

    def show_book_dialog(self, statement):
        # Окно для бронирования
        book_dialog = QMessageBox(self)
        book_dialog.setWindowTitle('Информация о бронировании')
        if statement is True:
            book_dialog.setText('Вы успешно забронировали номер!')
        else:
            book_dialog.setText('Вы не смогли забронировать номер, на это время он уже занят!')
        book_dialog.exec()

    # endregion
    def show_cancel(self):
        self.name_del = QLineEdit(self)
        self.gender_del = QComboBox(self)
        self.gender_del.addItems(['Male', 'Female', 'Other'])
        self.passport_del = QLineEdit(self)
        self.phone_del = QLineEdit(self)
        self.room_type_del = QComboBox(self)
        self.room_type_del.addItems(['Classic', 'Comfort', 'Lux'])
        self.start_date_del = QCalendarWidget(self)
        self.end_date_del = QCalendarWidget(self)

        # Создание кнопки для бронирования
        self.book_del = QPushButton('Удалить бронь', self)
        self.book_del.clicked.connect(self.show_cancel_dialog)

        # Создание формы
        form_layout = QFormLayout()
        form_layout.addRow('ФИО:', self.name_del)
        form_layout.addRow('Пол:', self.gender_del)
        form_layout.addRow('Паспорт:', self.passport_del)
        form_layout.addRow('Телефон:', self.phone_del)
        form_layout.addRow('Тип комнаты:', self.room_type_del)
        form_layout.addRow('Дата начала:', self.start_date_del)
        form_layout.addRow('Дата конца:', self.end_date_del)
        form_layout.addRow(self.book_del)

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)

        # Основной виджет
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        return main_widget

    def show_cancel_dialog(self):
        # Окно для отмены бронирования
        cancel_dialog = QMessageBox(self)
        cancel_dialog.setWindowTitle('Информация')
        cancel_dialog.setText('Бронь отменена!')
        cancel_dialog.exec()

    def show_view(self):
        self.name_view = QLineEdit(self)
        self.gender_view = QComboBox(self)
        self.gender_view.addItems(['Male', 'Female', 'Other'])
        self.passport_view = QLineEdit(self)

        # Создание кнопки для бронирования
        self.view_button = QPushButton('Просмотреть все брони', self)
        self.view_button.clicked.connect(self.show_view_dialog)

        # Создание формы
        form_layout = QFormLayout()
        form_layout.addRow('ФИО:', self.name_view)
        form_layout.addRow('Пол:', self.gender_view)
        form_layout.addRow('Паспорт:', self.passport_view)
        form_layout.addRow(self.view_button)

        # Основной макет
        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)

        # Основной виджет
        main_widget = QWidget(self)
        main_widget.setLayout(main_layout)

        self.setCentralWidget(main_widget)
        return main_widget

    def show_view_dialog(self):
        # Окно для просмотра броней
        view_dialog = QMessageBox(self)
        view_dialog.setWindowTitle('Информация')
        view_dialog.setText('Просмотр текущих броней')
        view_dialog.exec()

    def show_receipt_dialog(self):
        # Окно для получения чека
        receipt_dialog = QMessageBox(self)
        receipt_dialog.setWindowTitle('Информация')
        receipt_dialog.setText('Чек успешно получен!')
        receipt_dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = HotelBookingApp()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
