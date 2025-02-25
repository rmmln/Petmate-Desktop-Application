from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QFrame, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import Qt
import resource
import sys

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi("Home.ui", self)

        #HOME TABLE
        self.upcoming_appointment.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.upcoming_appointment.verticalHeader().setDefaultSectionSize(100)  # Set row height to 40px

        # Insert Test Data
        self.insert_data([
            ["Robert Moleno", "09987654321", "02", "12:00PM", "Surgery"],
            ["Dredd Domasian", "09987654321", "02", "12:00PM", "Surgery"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
            ["Francis Jerusalem", "09121212121", "03", "2:00PM", "Grooming"],
        ])
        #Changing main Page
        self.stackedWidget.setCurrentIndex(0)
        self.homeBtn.clicked.connect(lambda: self.navigate_to_page(0))
        self.addPatientBtn.clicked.connect(lambda: self.navigate_to_page(1))
        self.petRecordsBtn.clicked.connect(lambda: self.navigate_to_page(2))
        self.appointmentBtn.clicked.connect(lambda: self.navigate_to_page(3))

        #gender placeholder
        self.comboGender.model().item(0).setEnabled(False)
        #ProceedBtn
        self.proceedBtn.clicked.connect(lambda: self.proceed_confirmation_page(1))

    def proceed_confirmation_page(self,index):
        self.AddpatientStack.setCurrentIndex(index)
    def navigate_to_page(self, index):
        self.stackedWidget.setCurrentIndex(index)

    #Insert sa table
    def insert_data(self, data):

        self.upcoming_appointment.setRowCount(len(data))
        self.upcoming_appointment.setColumnCount(len(data[0]))

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(value)
                item.setTextAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
                self.upcoming_appointment.setItem(row_idx, col_idx, item)
        self.upcoming_appointment.viewport().update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec()
