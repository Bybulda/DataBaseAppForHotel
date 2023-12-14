import sys

from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QPushButton

from AuthWindow import AuthWindow
from Visitor import HotelBookingApp


class StartWindow(QDialog):
    def __init__(self, app):
        super().__init__()
        self.app = app

        self.setWindowTitle('Выбор пользователя')

        admin_button = QPushButton('Войти как администратор')
        admin_button.clicked.connect(self.open_admin_window)

        visitor_button = QPushButton('Войти как посетитель')
        visitor_button.clicked.connect(self.open_visitor_window)

        layout = QVBoxLayout(self)
        layout.addWidget(admin_button)
        layout.addWidget(visitor_button)

    def __del__(self):
        pass

    def open_admin_window(self):
        self.admin_window = AuthWindow(self.app)
        self.admin_window.show()
        self.accept()

    def open_visitor_window(self):
        self.visitor_window = HotelBookingApp(self.app)
        self.visitor_window.show()
        self.accept()


def main():
    app = QApplication(sys.argv)

    start_window = StartWindow(app)
    if start_window.exec() == QDialog.DialogCode.Accepted:
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
