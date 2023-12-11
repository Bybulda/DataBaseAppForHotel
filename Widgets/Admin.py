import configparser
import sys

import psycopg2
from query.adminQuery import *
from PyQt6.QtCore import QDateTime
from PyQt6.QtWidgets import QMainWindow, QPushButton, QTabWidget, QApplication, QWidget, QTableWidget, QVBoxLayout, \
    QLineEdit, QLabel, QDateTimeEdit, QComboBox, QTableWidgetItem, QMessageBox


class AdminWindow(QMainWindow):
    def __init__(self, config_file='../config/config.ini'):
        super().__init__()
        self.open_connection(config_file)
        self.init_ui()

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

    def init_ui(self):
        self.setWindowTitle('Управление отелем')

        self.tab_widget = QTabWidget()

        delete_visitor_button = self.show_delete_user()

        add_employee = self.show_employee_manage()

        show_employees_button = QPushButton('Вывести список сотрудников')
        show_employees_button.clicked.connect(self.show_employees)

        change_salary_button = QPushButton('Изменить зарплату сотрудника')
        change_salary_button.clicked.connect(self.change_salary)

        add_task_button = self.show_delete_task()

        delete_task_button = QPushButton('Удалить задачу из расписания')
        delete_task_button.clicked.connect(self.delete_task)

        show_schedule_button = self.show_view()

        self.tab_widget.addTab(delete_visitor_button, 'Удалить посетителя')
        self.tab_widget.addTab(add_employee, 'Добавить/Удалить/Изменить зарплату сотрудника')
        self.tab_widget.addTab(add_task_button, 'Добавить/Удалить задачу')
        self.tab_widget.addTab(show_schedule_button, 'Вывести расписание/Список сотрудников')

        self.setCentralWidget(self.tab_widget)

    # region view
    def show_view(self):
        view_widget = QWidget()
        view_widget_layout = QVBoxLayout()
        self.view_employee = QTableWidget(self)
        self.view_employee.setColumnCount(5)
        self.view_employee.setHorizontalHeaderLabels(
            ["ID Сотрудника", "ФИО", "Паспорт", "Опыт", "Зарплата"])
        self.view_schedule = QTableWidget(self)
        self.view_schedule.setColumnCount(7)
        self.view_schedule.setHorizontalHeaderLabels(
            ["ID Расписания", "ID Задачи", "ID Персонала", "ID Комнаты", "Дата начала", "Дата конца", "Занятость"])
        self.refresh_view = QPushButton("Обновить таблицы")
        self.refresh_view.clicked.connect(self.refresh_accept)
        self.empl_label = QLabel("Таблица сотрудников")
        self.schdl_label = QLabel("Таблица расписания задач")
        view_widget_layout.addWidget(self.refresh_view)
        view_widget_layout.addWidget(self.empl_label)
        view_widget_layout.addWidget(self.view_employee)
        view_widget_layout.addWidget(self.schdl_label)
        view_widget_layout.addWidget(self.view_schedule)
        view_widget.setLayout(view_widget_layout)
        return view_widget

    def refresh_accept(self):
        # query_emp = 'select * from staff'
        # query_tasks = 'select * from schedule'
        self.cur.execute(query_emp)
        emp_res = self.cur.fetchall()

        for row, employee in enumerate(emp_res):
            self.view_employee.insertRow(row)
            snp = []
            col = 0
            for j, item in enumerate(employee):
                if 0 < j < 4:
                    snp.append(item)
                    continue
                elif j == 4:
                    col = 2
                self.view_employee.setItem(row, col, QTableWidgetItem(str(item)))
                col += 1
            self.view_employee.setItem(row, 1, QTableWidgetItem(" ".join(snp)))

        self.cur.execute(query_tasks)
        schdl_res = self.cur.fetchall()

        for row, task in enumerate(schdl_res):
            self.view_schedule.insertRow(row)
            for col, item in enumerate(task):
                self.view_schedule.setItem(row, col, QTableWidgetItem(str(item)))

    # endregion view
    # region user
    def show_delete_user(self):
        # Remove Visitor Tab
        remove_visitor_tab = QWidget()
        remove_visitor_layout = QVBoxLayout()

        # Fields for input
        self.fio_line_edit = QLineEdit(self)
        self.passport_line_edit = QLineEdit(self)

        remove_visitor_layout.addWidget(QLabel("ФИО:"))
        remove_visitor_layout.addWidget(self.fio_line_edit)

        remove_visitor_layout.addWidget(QLabel("Паспорт:"))
        remove_visitor_layout.addWidget(self.passport_line_edit)

        # Button to search and display data
        search_button = QPushButton("Найти посетителя")
        search_button.clicked.connect(self.search_visitor)
        remove_visitor_layout.addWidget(search_button)

        # Table to display visitor data
        self.visitor_table_widget = QTableWidget(self)
        self.visitor_table_widget.setColumnCount(5)
        self.visitor_table_widget.setHorizontalHeaderLabels(
            ["ID Посетителя", "ФИО", "Паспорт", "Номер телефона", "Пол"])
        remove_visitor_layout.addWidget(self.visitor_table_widget)

        # Button to remove selected visitor
        remove_button = QPushButton("Удалить посетителя")
        remove_button.clicked.connect(self.delete_visitor)
        remove_visitor_layout.addWidget(remove_button)

        remove_visitor_tab.setLayout(remove_visitor_layout)
        return remove_visitor_tab

    def search_visitor(self):
        surname, name, patronymic = (i.lower().capitalize() for i in self.fio_line_edit.text().split())
        passport = int(self.passport_line_edit.text())
        self.cur.execute(search_user_query, (name, surname, patronymic, passport))
        res = self.cur.fetchone()
        if len(res) == 0:
            self.show_box('Ошибка', "Пользователь не найден!")
            return
        table_for = []
        fio = []
        for i, j in enumerate(res):
            if 0 < i < 4:
                fio.append(j)
                continue
            elif i == 4:
                table_for.append(' '.join(fio))
            table_for.append(j)

        self.visitor_table_widget.insertRow(0)
        for col, item in enumerate(table_for):
            self.visitor_table_widget.setItem(0, col, QTableWidgetItem(str(item)))

    def delete_visitor(self):
        if self.visitor_table_widget.item(0, 0) is None:
            self.show_box('Ошибка удаления', "Пожалуйста, для начала нажмите на кнопку \"Найти пользователя\" и убедитесь что информацию о нем вывело на экран!")
            return

        passport = int(self.visitor_table_widget.item(0, 2))
        self.visitor_table_widget.clearContents()
        self.visitor_table_widget.removeRow(0)
        self.cur.execute(delete_user_query, (passport,))
        self.conn.commit()
        self.show_box('Информация', 'Посетитель успешно удален!')

    # endregion user
    # region task
    def show_delete_task(self):

        # Add Task Tab
        add_task_tab = QWidget()
        add_task_layout = QVBoxLayout()
        self.task_manager = QComboBox(self)
        self.task_manager.addItems([ 'Добавить задачу', 'Удалить задачу'])
        self.task_manager.currentIndexChanged.connect(self.update_task_ui)
        self.id_line_edit = QLineEdit(self)
        self.task_line_edit = QLineEdit(self)
        self.room_line_edit = QLineEdit(self)

        self.start_datetime_edit = QDateTimeEdit(self)
        self.start_datetime_edit.setCalendarPopup(True)  # Make the calendar pop up when the field is selected
        self.start_datetime_edit.setDateTime(QDateTime.currentDateTime())  # Set the default date and time

        self.end_datetime_edit = QDateTimeEdit(self)
        self.end_datetime_edit.setCalendarPopup(True)
        self.end_datetime_edit.setDateTime(QDateTime.currentDateTime())

        self.availability_line = QComboBox(self)
        self.availability_line.addItems(['Комната занята', 'Комната свободна'])

        self.table_widget = QTableWidget(self)
        self.table_widget.setColumnCount(6)
        self.table_widget.setHorizontalHeaderLabels(
            ["ID Перасонала", "ID Задачи", "ID Комнаты", "Дата начала", "Дата конца", "Занятость"])

        add_task_layout.addWidget(self.task_manager)
        add_task_layout.addWidget(QLabel("ID Персонала:"))
        add_task_layout.addWidget(self.id_line_edit)
        add_task_layout.addWidget(QLabel("ID Задачи:"))
        add_task_layout.addWidget(self.task_line_edit)
        add_task_layout.addWidget(QLabel("ID Комнаты:"))
        add_task_layout.addWidget(self.room_line_edit)
        add_task_layout.addWidget(QLabel("Дата и время начала:"))
        add_task_layout.addWidget(self.start_datetime_edit)
        add_task_layout.addWidget(QLabel("Дата и время конца:"))
        add_task_layout.addWidget(self.end_datetime_edit)
        add_task_layout.addWidget(QLabel("Занятость:"))
        add_task_layout.addWidget(self.availability_line)
        add_task_layout.addWidget(self.table_widget)

        # Button to add task
        self.add_button = QPushButton('Добавить задачу', self)
        self.add_button.clicked.connect(self.add_task)
        add_task_layout.addWidget(self.add_button)

        add_task_tab.setLayout(add_task_layout)

        # Remove Visitor Tab

        return add_task_tab

    def update_task_ui(self):
        selected_action = self.task_manager.currentText()

        if selected_action == "Удалить задачу":
            self.add_button.setText("Удалить задачу")
        elif selected_action == "Добавить задачу":

            self.add_button.setText("Добавить задачу")

    def delete_task(self):
        # Логика удаления задачи из расписания
        pass

    def add_task(self):
        # Логика добавления задачи в расписание
        pass

    def show_schedule(self):
        # Логика вывода расписания
        pass

    # endregion task
    # region employee
    def show_employee_manage(self):
        self.employee_widget = QWidget()
        layout = QVBoxLayout()

        # Combo box for selecting action (Add, Remove, or Update Salary)
        self.action_combo_box = QComboBox(self)
        self.action_combo_box.addItem("Добавить сотрудника")
        self.action_combo_box.addItem("Удалить сотрудника")
        self.action_combo_box.addItem("Изменить зарплату")
        self.action_combo_box.currentIndexChanged.connect(self.update_ui)
        layout.addWidget(self.action_combo_box)

        # Fields for input
        self.fio_emp = QLineEdit(self)
        self.passport_emp = QLineEdit(self)
        self.experience_line_edit = QLineEdit(self)
        self.salary_line_edit = QLineEdit(self)

        layout.addWidget(QLabel("ФИО:"))
        layout.addWidget(self.fio_emp)

        layout.addWidget(QLabel("Паспорт:"))
        layout.addWidget(self.passport_emp)
        self.exp = QLabel("Опыт (в годах):")
        layout.addWidget(self.exp)
        layout.addWidget(self.experience_line_edit)
        self.salare = QLabel("Зарплата:")
        layout.addWidget(self.salare)
        layout.addWidget(self.salary_line_edit)

        # Button for managing employee based on selected action
        self.employee_button = QPushButton("Добавить пользователя", self)
        self.employee_button.clicked.connect(self.manage_employee)
        layout.addWidget(self.employee_button)

        # Table to display employee data
        self.employee_table_widget = QTableWidget(self)
        self.employee_table_widget.setColumnCount(5)
        self.employee_table_widget.setHorizontalHeaderLabels(['ID', "ФИО", "Паспорт", "Опыт", "Зарплата"])
        layout.addWidget(self.employee_table_widget)

        self.employee_widget.setLayout(layout)
        return self.employee_widget

    def update_ui(self):
        # Dynamically update UI based on selected action
        selected_action = self.action_combo_box.currentText()

        if selected_action == "Добавить сотрудника":
            self.experience_line_edit.show()
            self.salare.show()
            self.exp.show()
            self.salary_line_edit.show()
            self.employee_button.setText("Добавить сотрудника")
        elif selected_action == "Удалить сотрудника":
            self.experience_line_edit.hide()

            self.salare.hide()
            self.exp.hide()
            self.salary_line_edit.hide()
            self.employee_button.setText("Удалить сотрудника")
        elif selected_action == "Изменить зарплату":
            self.experience_line_edit.hide()
            self.salare.show()
            self.exp.hide()
            self.salary_line_edit.show()
            self.employee_button.setText("Изменить зарплату")

    def manage_employee(self):
        # Implement logic based on selected action
        selected_action = self.action_combo_box.currentText()

        if selected_action == "Добавить сотрудника":
            self.add_employee()
        elif selected_action == "Удалить сотрудника":
            self.delete_employee()
        elif selected_action == "Изменить зарплату":
            self.change_salary()

    def show_employees(self, info, upd=None):
        self.employee_table_widget.clearContents()
        self.employee_table_widget.removeRow(0)
        self.employee_table_widget.insertRow(0)
        id_, *snp, passport, exp, salary = info
        salary = salary if upd is None else upd
        for col, item in enumerate((id_, snp, passport, exp, salary)):
            self.employee_table_widget.setItem(0, col, QTableWidgetItem(str(item)))



    def delete_employee(self):
        try:
            surname, name, patronymic = self.fio_emp.text().split()
            passport = self.passport_emp.text()
            self.cur.execute(search_empl_query, (passport, name, surname, patronymic))
            res = self.cur.fetchone()
            if len(res) == 0:
                self.show_box('Внимание', 'Такого сотрудника не существует! Пожалуйста, проверьте данные!')
                return
            self.cur.execute(delete_empl_query, (passport, name, surname, patronymic))
            self.conn.commit()
            self.show_employees(res[0])
            self.show_box("Информация", "Вы успешно удалили сотрудника")
        except Exception:
            self.show_box('Ошибка', 'Произошла ошибка в обработке запроса, возможно вы ввели неправильные данные')

    def add_employee(self):
        try:
            surname, name, patronymic = self.fio_emp.text().split()
            passport = self.passport_emp.text()
            salary = self.salary_line_edit.text()
            self.cur.execute(search_empl_query, (passport, name, surname, patronymic))
            res = self.cur.fetchone()
            if len(res) == 0:
                self.show_box('Внимание', 'Такого сотрудника не существует! Пожалуйста, проверьте данные!')
                return
            self.cur.execute(update_salary, (salary, passport, name, surname, patronymic))
            self.conn.commit()
            self.show_employees(res[0])
            self.show_box("Информация", "Вы успешно изменили зарплату сотрудника")
        except Exception:
            self.show_box('Ошибка', 'Произошла ошибка в обработке запроса, возможно вы ввели неправильные данные')

    def change_salary(self):
        try:
            surname, name, patronymic = self.fio_emp.text().split()
            passport = self.passport_emp.text()
            salary = self.salary_line_edit.text()
            self.cur.execute(search_empl_query, (passport, name, surname, patronymic))
            res = self.cur.fetchone()
            if len(res) == 0:
                self.show_box('Внимание', 'Такого сотрудника не существует! Пожалуйста, проверьте данные!')
                return
            self.cur.execute(update_salary, (salary, passport, name, surname, patronymic))
            self.conn.commit()
            self.show_employees(res[0], salary)
            self.show_box("Информация", "Вы успешно изменили зарплату сотрудника")
        except Exception:
            self.show_box('Ошибка', 'Произошла ошибка в обработке запроса, возможно вы ввели неправильные данные')

    # endregion
    def show_box(self, title, message):
        cancel_dialog = QMessageBox(self)
        cancel_dialog.setWindowTitle(title)
        cancel_dialog.setText(message)
        cancel_dialog.exec()


def main():
    app = QApplication(sys.argv)
    window = AdminWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
