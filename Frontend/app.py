from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6.QtCore import Qt
import resource
from PyQt6.QtGui import QFontDatabase, QFont
from uiLogic import UIHandler
from Backend.sendData import save_data_to_db
import os
import django
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.', 'Backend')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Backend.myproject.settings")
django.setup()


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi("Home.ui", self)

        self.ui_handler = UIHandler(self.provinceComboBox, self.cityComboBox, self.barangayComboBox)
        self.ui_handler.load_provinces()

        #Changing main Page
        self.stackedWidget.setCurrentIndex(0)
        self.homeBtn.clicked.connect(lambda: self.navigate_to_page(0))
        self.addPatientBtn.clicked.connect(lambda: self.navigate_to_page(1))
        self.petRecordsBtn.clicked.connect(lambda: self.navigate_to_page(2))
        self.appointmentBtn.clicked.connect(lambda: self.navigate_to_page(3))
        self.schedVaxBtn.clicked.connect(lambda: self.navigate_to_page(4))

        self.confirmButton.clicked.connect(self.submit_data)
        self.successfullAlert.hide()

    def submit_data(self):
        firstName = self.firstNameEdit.text()
        lastName = self.lastNameEdit.text()
        phoneNumber = self.phoneNumberEdit.text()
        province = self.provinceComboBox.currentText()
        city = self.cityComboBox.currentText()
        barangay = self.barangayComboBox.currentText()
        detailedAddress = self.detailedAddressEdit.text()
        email = self.emailEdit.text()
        emergencyNumber = self.emergencyNoEdit.text()

        save_data_to_db(firstName, lastName, phoneNumber, province, city, barangay, detailedAddress, email,
                        emergencyNumber)



    def navigate_to_page(self, index):
        self.stackedWidget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    font_path = os.path.join(os.path.dirname(__file__), "font/Montserrat/Montserrat-VariableFont_wght.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)

    ui = MainUI()
    ui.show()
    app.exec()
