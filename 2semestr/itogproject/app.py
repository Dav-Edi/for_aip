from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.is_check_button = True

        self.setWindowTitle("Chat")
        button = QPushButton("Press me!")
        button.setCheckable(True)
        button.clicked.connect(self.check_button)
        button.setChecked(self.is_check_button)

        self.setMinimumSize(QSize(400, 600))

        self.setCentralWidget(button)



    def check_button(self, checked):
        self.check_button = checked
        print(self.check_button)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()