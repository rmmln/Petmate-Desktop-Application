import requests
from PyQt6.QtWidgets import QComboBox


class UIHandler:
    def __init__(self, provinceComboBox, cityComboBox, barangayComboBox):
        self.provinceComboBox = provinceComboBox
        self.cityComboBox = cityComboBox
        self.barangayComboBox = barangayComboBox

        # Connect ComboBox signals to appropriate methods
        self.provinceComboBox.currentIndexChanged.connect(self.on_province_selected)
        self.cityComboBox.currentIndexChanged.connect(self.on_city_selected)

    def load_provinces(self):
        url = "https://psgc.gitlab.io/api/provinces/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                provinces = response.json()
                self.provinceComboBox.clear()  # Clear the previous items
                self.provinceComboBox.addItem("Select Province")  # Add default text
                for prov in provinces:
                    self.provinceComboBox.addItem(prov["name"], prov["code"])
        except Exception as e:
            print("Error loading provinces:", e)

    def on_province_selected(self, index):
        if index == 0:
            self.cityComboBox.clear()  # Clear the city ComboBox if no province is selected
            self.barangayComboBox.clear()  # Clear the barangay ComboBox as well
            return

        province_code = self.provinceComboBox.itemData(index)
        url = f"https://psgc.gitlab.io/api/provinces/{province_code}/cities-municipalities/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                cities = response.json()
                self.cityComboBox.clear()  # Clear the previous cities
                self.cityComboBox.addItem("Select City/Municipality")  # Default text
                for city in cities:
                    self.cityComboBox.addItem(city["name"], city["code"])
                self.barangayComboBox.clear()  # Clear barangay ComboBox
            else:
                print(f"Failed to fetch cities for province {province_code}")
        except Exception as e:
            print("Error loading cities:", e)

    def on_city_selected(self, index):
        if index == 0:
            self.barangayComboBox.clear()  # Clear barangay ComboBox if no city is selected
            return

        city_code = self.cityComboBox.itemData(index)
        url = f"https://psgc.gitlab.io/api/cities-municipalities/{city_code}/barangays/"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                barangays = response.json()
                self.barangayComboBox.clear()  # Clear the previous barangays
                self.barangayComboBox.addItem("Select Barangay")  # Default text
                for brgy in barangays:
                    self.barangayComboBox.addItem(brgy["name"])
            else:
                print(f"Failed to fetch barangays for city {city_code}")
        except Exception as e:
            print("Error loading barangays:", e)
