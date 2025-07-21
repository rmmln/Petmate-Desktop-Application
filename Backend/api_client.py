import requests

BASE_URL = "http://127.0.0.1:8000/api"   # later change to your real server url

def add_new_patient(data):
    """
    data: dict with all patient info
    """
    try:
        response = requests.post(f"{BASE_URL}/patients/", json=data)
        if response.status_code == 201:
            print("Successfully added!")
            return True
        else:
            print("Failed to add patient:", response.status_code, response.text)
            return False
    except Exception as e:
        print("Error:", e)
        return False

def get_all_patients():
    try:
        response = requests.get(f"{BASE_URL}/patients/")
        if response.status_code == 200:
            return response.json()  # this will be a list of dicts
        else:
            print("Failed to fetch patients:", response.status_code, response.text)
            return []
    except Exception as e:
        print("Error:", e)
        return []