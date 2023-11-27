from PyQt6.QtWidgets import QMainWindow, QPushButton, QTabWidget, QDialog


class CheckOutWindow(QDialog):
    def __init__(self):
        super().__init__()


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Администратор')

        self.tab_widget = QTabWidget()

        delete_visitor_button = QPushButton('Удалить посетителя или сотрудника')
        delete_visitor_button.clicked.connect(self.delete_visitor)

        add_employee_button = QPushButton('Добавить сотрудника')
        add_employee_button.clicked.connect(self.add_employee)

        show_employees_button = QPushButton('Вывести список сотрудников')
        show_employees_button.clicked.connect(self.show_employees)

        change_salary_button = QPushButton('Изменить зарплату сотрудника')
        change_salary_button.clicked.connect(self.change_salary)

        add_task_button = QPushButton('Добавить задачу в расписание')
        add_task_button.clicked.connect(self.add_task)

        delete_task_button = QPushButton('Удалить задачу из расписания')
        delete_task_button.clicked.connect(self.delete_task)

        show_schedule_button = QPushButton('Вывести расписание')
        show_schedule_button.clicked.connect(self.show_schedule)

        self.tab_widget.addTab(delete_visitor_button, 'Удалить посетителя/сотрудника')
        self.tab_widget.addTab(add_employee_button, 'Добавить сотрудника')
        self.tab_widget.addTab(show_employees_button, 'Список сотрудников')
        self.tab_widget.addTab(change_salary_button, 'Изменить зарплату сотрудника')
        self.tab_widget.addTab(add_task_button, 'Добавить задачу в расписание')
        self.tab_widget.addTab(delete_task_button, 'Удалить задачу из расписания')
        self.tab_widget.addTab(show_schedule_button, 'Вывести расписание')

        self.setCentralWidget(self.tab_widget)

    def delete_visitor(self):
        # Логика удаления посетителя или сотрудника
        pass

    def delete_employee(self):
        # Логика добавления сотрудника
        pass

    def delete_task(self):
        # Логика удаления задачи из расписания
        pass

    def add_employee(self):
        # Логика добавления сотрудника
        pass

    def show_employees(self):
        # Логика вывода списка сотрудников
        pass

    def change_salary(self):
        # Логика изменения зарплаты сотрудника
        pass

    def add_task(self):
        # Логика добавления задачи в расписание
        pass

    def show_schedule(self):
        # Логика вывода расписания
        pass
