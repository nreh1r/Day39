import requests
from dotenv import load_dotenv
import os

load_dotenv()

print("Welcome to Nick's Flight Club.\nWe find the best flight deals and email you.")

first_name = input("What is your first name?\n").title()
last_name = input("What is your last name?\n").title()
email = input("What is you email?\n")
email_verify = input("What is your email?\n")

if email == email_verify:
    params = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }

    response = requests.post(url=os.getenv("SHEETY_POST_URL"), json=params)
    print(response.json())
    print("You're in the club!")
else:
    print("Emails do not match please try again.")
