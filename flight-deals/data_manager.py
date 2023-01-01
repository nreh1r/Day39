import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:
    # This class is responsible for talking to the Google Sheet.

    def get_data(self):
        response = requests.get(os.getenv("SHEETY_URL"))
        return response.json()["prices"]

    def update_data(self, city):
        params = {
            "price": {
                # "city": city["city"],
                "iataCode": city["iataCode"],
                # "lowestPrice": city["lowestPrice"]
            }
        }
        response = requests.put(
            url=f"{os.getenv('SHEETY_PUT_URL')}/{city['id']}", json=params)
        print(response.json())

    def get_emails(self):
        emails = []
        response = requests.get(os.getenv("SHEETY_USERS_URL"))
        data = response.json()
        for user in data["users"]:
            emails.append(user["email"])
        return emails
