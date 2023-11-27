import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Окно с виджетами')

        self.stacked_widget = QStackedWidget(self)

        # Первый виджет
        widget1 = QWidget(self)
        label1 = QLabel('Это первый виджет', widget1)
        next_button1 = QPushButton('Следующий виджет', widget1)
        next_button1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))

        layout1 = QVBoxLayout(widget1)
        layout1.addWidget(label1)
        layout1.addWidget(next_button1)

        # Второй виджет
        widget2 = QWidget(self)
        label2 = QLabel('Это второй виджет', widget2)
        back_button2 = QPushButton('Предыдущий виджет', widget2)
        back_button2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))

        layout2 = QVBoxLayout(widget2)
        layout2.addWidget(label2)
        layout2.addWidget(back_button2)

        # Добавляем виджеты в QStackedWidget
        self.stacked_widget.addWidget(widget1)
        self.stacked_widget.addWidget(widget2)

        self.setCentralWidget(self.stacked_widget)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
