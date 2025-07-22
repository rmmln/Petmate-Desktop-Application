from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QWidget,QComboBox,QButtonGroup,QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import Qt
import resources_rc
from PyQt6.QtGui import QFontDatabase, QFont, QPixmap, QIcon, QAction
from uiLogic import UIHandler
from toast import Toast
from Backend.api_client import add_new_patient
import requests
import os
import sys



class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        uic.loadUi("Home.ui", self)

        self.ui_handler = UIHandler(self.provinceComboBox, self.cityComboBox, self.barangayComboBox)
        self.ui_handler.load_provinces()

        # 👉 Set layout before loading patients
        self.patientListLayout = self.scrollAreaWidgetContents.layout()
        self.patientListLayout.setSpacing(10)  # spacing between cards
        self.patientListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Load patients now
        self.load_patients()

        #Changing main Page
        self.stackedWidget.setCurrentIndex(0)
        self.homeBtn.clicked.connect(lambda: self.navigate_to_page(0))
        self.addPatientBtn.clicked.connect(lambda: self.navigate_to_page(1))
        self.petRecordsBtn.clicked.connect(lambda: self.navigate_to_page(2))
        self.appointmentBtn.clicked.connect(lambda: self.navigate_to_page(3))
        self.schedVaxBtn.clicked.connect(lambda: self.navigate_to_page(4))

        self.confirmButton.clicked.connect(self.submit_data)

        #Appointment Buttons
        # Make buttons checkable
        self.walkInBtn.setCheckable(True)
        self.websiteBtn.setCheckable(True)
        # Create a QButtonGroup to keep only one active
        self.sourceBtnGroup = QButtonGroup(self)
        self.sourceBtnGroup.setExclusive(True)

        self.sourceBtnGroup.addButton(self.walkInBtn)
        self.sourceBtnGroup.addButton(self.websiteBtn)

        self.walkInBtn.setChecked(True)
        #changing page walkIn/website appointment
        self.walkInBtn.clicked.connect(lambda: self.walkInOrWeb.setCurrentIndex(0))
        self.websiteBtn.clicked.connect(lambda: self.walkInOrWeb.setCurrentIndex(1))
        #backbutton in profile page
        self.profileBackbutton.clicked.connect(lambda: self.navigate_to_page(2))




    def navigate_to_page(self, index):
        self.stackedWidget.setCurrentIndex(index)


    def submit_data(self):
        required_fields = {
            "First Name": self.firstNameEdit,
            "Last Name": self.lastNameEdit,
            "Phone Number": self.phoneNumberEdit,
            "Province": self.provinceComboBox,
            "City": self.cityComboBox,
            "Barangay": self.barangayComboBox,
            "Detailed Address": self.detailedAddressEdit,
            "Email": self.emailEdit,
            "Emergency Number": self.emergencyNoEdit
        }

        missing = []

        default_style = """
            QLineEdit {
                border-right: 2px solid #cccccc;
                border-bottom: 2px solid #cccccc;
                border-radius: 5px;
	
	            font: 57 12pt 'Montserrat Medium';
	            color:rgb(39, 39, 39);
	            padding-left: 10px;
            }"""

        default_combobox_style = """
            QComboBox {
                border-right: 2px solid #cccccc;
                border-bottom: 2px solid #cccccc;
                border-radius: 5px;
                font: 63 12pt "Montserrat SemiBold";
                padding-left: 5px;
                color: rgb(39, 39, 39);
            }
            
            QComboBox::drop-down {
                background-color: white;
                border: none;
            }
            
            QComboBox::down-arrow {
                image: url(:/Icons/Icons/downArrow.png);
                width: 12px;
                height: 12px;
                padding-right: 10px;
            }
            
            /* Dropdown list */
            QComboBox QAbstractItemView {
                background-color: white;
                selection-background-color: rgb(193, 193, 193); 
                selection-color: black;
                font: 63 12pt "Montserrat SemiBold";
                outline: none;
                border:none;
            }
            
            /* List items */
            QComboBox QAbstractItemView::item {
                background-color: white;
                color: black;
                height: 25px;
                font: 63 12pt "Montserrat SemiBold";
            }
            
            QComboBox QAbstractItemView::item:hover {
                background-color: rgb(193, 193, 193);
                color: black;
            }
            
            /* Scrollbar inside dropdown */
            QComboBox QAbstractItemView QScrollBar:vertical {
                background-color: transparent; /* or set a solid color */
                width: 10px;
                border: none;
            }
            
            QComboBox QAbstractItemView QScrollBar::handle:vertical {
                background-color: rgb(129, 191, 218);
                border-radius: 5px;
                min-height: 120px;
            }
            
            QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {
                background-color: rgb(86, 127, 145);
            }
            
            QComboBox QAbstractItemView QScrollBar::add-line:vertical,
            QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                height: 0px;
                background: none;
                border: none;
            }
            
            QComboBox QAbstractItemView QScrollBar::groove:vertical {
                background: transparent;
                outline: none;
                border: none;
            }
            QComboBox QAbstractItemView QScrollBar,
            QComboBox QAbstractItemView QScrollBar::handle,
            QComboBox QAbstractItemView QScrollBar::groove {
                outline: none;
                border: none;
            }

        """

        error_combobox_style = """
                    QComboBox {
                        border: 1px solid #ff4f61;
                        border-radius: 5px;
                        font: 63 12pt "Montserrat SemiBold";
                        padding-left: 5px;
                        color: rgb(39, 39, 39);
                    }

                    QComboBox::drop-down {
                        background-color: white;
                        border: none;
                    }

                    QComboBox::down-arrow {
                        image: url(:/Icons/Icons/downArrow.png);
                        width: 12px;
                        height: 12px;
                        padding-right: 10px;
                    }

                    /* Dropdown list */
                    QComboBox QAbstractItemView {
                        background-color: white;
                        selection-background-color: rgb(193, 193, 193); 
                        selection-color: black;
                        font: 63 12pt "Montserrat SemiBold";
                        outline: none;
                        border:none;
                    }

                    /* List items */
                    QComboBox QAbstractItemView::item {
                        background-color: white;
                        color: black;
                        height: 25px;
                        font: 63 12pt "Montserrat SemiBold";
                    }

                    QComboBox QAbstractItemView::item:hover {
                        background-color: rgb(193, 193, 193);
                        color: black;
                    }

                    /* Scrollbar inside dropdown */
                    QComboBox QAbstractItemView QScrollBar:vertical {
                        background-color: transparent; /* or set a solid color */
                        width: 10px;
                        border: none;
                    }

                    QComboBox QAbstractItemView QScrollBar::handle:vertical {
                        background-color: rgb(129, 191, 218);
                        border-radius: 5px;
                        min-height: 120px;
                    }

                    QComboBox QAbstractItemView QScrollBar::handle:vertical:hover {
                        background-color: rgb(86, 127, 145);
                    }

                    QComboBox QAbstractItemView QScrollBar::add-line:vertical,
                    QComboBox QAbstractItemView QScrollBar::sub-line:vertical {
                        height: 0px;
                        background: none;
                        border: none;
                    }

                    QComboBox QAbstractItemView QScrollBar::groove:vertical {
                        background: transparent;
                        outline: none;
                        border: none;
                    }
                    QComboBox QAbstractItemView QScrollBar,
                    QComboBox QAbstractItemView QScrollBar::handle,
                    QComboBox QAbstractItemView QScrollBar::groove {
                        outline: none;
                        border: none;
                    }

                """
        error_style = """
            QLineEdit {
                border: 1px solid #ff4f61;
                border-radius: 5px;

                font: 57 12pt 'Montserrat Medium';
                color:rgb(39, 39, 39);
                padding-left: 10px;
            }"""

        def apply_style(widget, error=False):
            is_combobox = "QComboBox" in widget.__class__.__name__
            if error:
                if is_combobox:
                    widget.setStyleSheet(error_combobox_style)
                else:
                    widget.setStyleSheet(error_style)
            else:
                if is_combobox:
                    widget.setStyleSheet(default_combobox_style)
                else:
                    widget.setStyleSheet(default_style)

        for name, widget in required_fields.items():
            is_combobox = "QComboBox" in widget.__class__.__name__

            if is_combobox:
                if widget.currentIndex() == 0:  # user didn't select a valid item
                    apply_style(widget, error=True)
                    missing.append(name)
                else:
                    apply_style(widget, error=False)
            else:
                text = widget.text()
                if not text.strip():
                    apply_style(widget, error=True)
                    missing.append(name)
                else:
                    apply_style(widget, error=False)

        if missing:
            message = "The following fields are required:\n• " + "\n• ".join(missing)
            toast = Toast(self, message, icon_path="Icons/warning.png")
            toast.show_toast()
            return

        # ✅ If all good, save and show success
        data = {
            "firstName": self.firstNameEdit.text(),
            "lastName": self.lastNameEdit.text(),
            "phoneNumber": self.phoneNumberEdit.text(),
            "province": self.provinceComboBox.currentText(),
            "city": self.cityComboBox.currentText(),
            "barangay": self.barangayComboBox.currentText(),
            "detailedAddress": self.detailedAddressEdit.text(),
            "email": self.emailEdit.text(),
            "emergencyNumber": self.emergencyNoEdit.text()
        }

        if add_new_patient(data):
            self.navigate_to_page(2)
            self.load_patients()

            # clear fields
            self.firstNameEdit.clear()
            self.lastNameEdit.clear()
            self.phoneNumberEdit.clear()
            self.detailedAddressEdit.clear()
            self.emailEdit.clear()
            self.emergencyNoEdit.clear()

            # Reset combo boxes to first index
            self.provinceComboBox.setCurrentIndex(0)
            self.cityComboBox.setCurrentIndex(0)
            self.barangayComboBox.setCurrentIndex(0)

            # Reset styles to default
            for widget in required_fields.values():
                if isinstance(widget, QLineEdit):
                    widget.setStyleSheet(default_style)
                elif isinstance(widget, QComboBox):
                    widget.setStyleSheet(default_combobox_style)

            toast = Toast(self,icon_path="Icons/check.png")
            toast.show_toast()


        else:
            toast = Toast(self, "Failed to add patient!", icon_path="Icons/warning.png")
            toast.show_toast()

    def load_patients(self):
        response = requests.get("http://127.0.0.1:8000/api/patients/")
        if response.status_code == 200:
            patients = response.json()
        else:
            patients = []

        # 🧹 Clear existing items before adding new ones
        while self.patientListLayout.count():
            child = self.patientListLayout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        for patient in patients:
            card = uic.loadUi("PatientCard.ui")
            card.nameLabel.setText(f"{patient['firstName']} {patient['lastName']}")
            card.emailLabel.setText(patient['email'])

            # Connect delete button
            card.deleteButton.clicked.connect(lambda _, p_id=patient['id']: self.delete_patient(p_id))

            # Connect the card click to open profile
            card.mousePressEvent = lambda event, p=patient: self.show_patient_profile(p)

            self.patientListLayout.insertWidget(0, card)

    def delete_patient(self, patient_id):
        reply = QMessageBox.question(self, "Delete", "Are you sure you want to delete this patient?",
                                     QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            response = requests.delete(f"http://127.0.0.1:8000/api/patients/{patient_id}/")
            if response.status_code == 204:
                toast = Toast(self, "Deleted successfully!", icon_path="Icons/check.png")
                toast.show_toast()
                self.load_patients()
            else:
                toast = Toast(self, "Failed to delete!", icon_path="Icons/warning.png")
                toast.show_toast()

    def show_patient_profile(self, patient):
        full_name = f"{patient['firstName']} {patient['lastName']}"
        self.profileNameLabel.setText(full_name)
        self.profileEmailLabel.setText(patient['email'])

        # Combine address parts
        address = f"{patient['barangay']}, {patient['city']}, {patient['province']}"
        self.addressLabel.setText(address)

        self.phoneLabel.setText(patient['phoneNumber'])

        # Navigate to the profile page
        self.stackedWidget.setCurrentIndex(5)




if __name__ == "__main__":
    app = QApplication(sys.argv)


    font_path = os.path.join(os.path.dirname(__file__), "font/Montserrat/Montserrat-VariableFont_wght.ttf")
    font_id = QFontDatabase.addApplicationFont(font_path)

    ui = MainUI()
    ui.show()
    app.exec()
