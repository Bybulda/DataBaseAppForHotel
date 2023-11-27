import sys

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton, QLineEdit, QMessageBox, QLabel
import configparser
from Admin import AdminWindow


class AuthWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Аутентификация')
        self.config_file = '../config.ini'

        admin_button = QPushButton('Войти в аккаунт')
        admin_button.clicked.connect(self.check_auth)

        self.login = QLineEdit()
        self.login.setPlaceholderText("Логин")
        self.password = QLineEdit()
        self.password.setPlaceholderText("Пароль")


        layout = QVBoxLayout(self)
        layout.addWidget(self.login)
        layout.addWidget(self.password)
        layout.addWidget(admin_button)

    def validate_info(self, login, password):
        config = configparser.ConfigParser()
        config.read(self.config_file)

        real_p = config.get('admin', 'password')
        real_l = config.get('admin', 'login')
        return login == real_l and password == real_p

    def auth_error(self):
        box = QMessageBox(self).setWindowTitle("Ошибка входа!")
        box.setText("Вы допустили ошибку в вводе логина/пароля, пожалуйста, попробуйте ещё раз!")
        box.exec()

    def check_auth(self):
        login = self.login.text()
        password = self.password.text()
        if self.validate_info(login, password):
            self.start_admin_session()
        else:
            self.auth_error()

    def start_admin_session(self):
        self.admin_window = AdminWindow()
        self.admin_window.show()
        self.accept()



def main():
    app = QApplication(sys.argv)

    start_window = AuthWindow()
    if start_window.exec() == QDialog.DialogCode.Accepted:
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
