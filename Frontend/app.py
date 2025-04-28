from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt
import resource
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi("Home.ui", self)

        #Changing main Page
        self.stackedWidget.setCurrentIndex(0)
        self.homeBtn.clicked.connect(lambda: self.navigate_to_page(0))
        self.addPatientBtn.clicked.connect(lambda: self.navigate_to_page(1))
        self.petRecordsBtn.clicked.connect(lambda: self.navigate_to_page(2))
        self.appointmentBtn.clicked.connect(lambda: self.navigate_to_page(3))
        self.schedVaxBtn.clicked.connect(lambda: self.navigate_to_page(4))

    def navigate_to_page(self, index):
        self.stackedWidget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()

