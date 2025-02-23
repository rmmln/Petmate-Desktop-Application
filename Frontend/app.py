from PyQt6.QtWidgets import QMainWindow, QApplication, QHeaderView, QFrame, QTableWidgetItem
from PyQt6.QtCore import Qt, QObject, QEvent
from PyQt6.QtGui import QFont, QFontDatabase
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
        self.upcoming_appointment.verticalHeader().setVisible(False)
        self.upcoming_appointment.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)


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

        self.stackedWidget.setCurrentIndex(3)

        self.homeBtn.clicked.connect(lambda: self.navigate_to_page(0))

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
