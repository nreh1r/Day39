from twilio.rest import Client
from dotenv import load_dotenv
import os
import smtplib
import requests

load_dotenv()


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def send_message(self, flight):
        client = Client(os.getenv("TWILIO_ACCOUNT_SID"),
                        os.getenv("TWILIO_AUTH_TOKEN"))

        message = f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.arival_city}-{flight.arival_airport_code} from, {flight.departure_time} to {flight.return_time}."

        if flight.stopovers:
            message += f"\n\nFlight has 1 stop over, via {flight.via_city}."

        # Uncomment this to send text messages
        # new_message = client.messages \
        #     .create(
        #         body=message,
        #         from_=os.getenv("TWILIO_PHONE_NUMBER"),
        #         to=os.getenv("TWILIO_SEND_PHONE_NUMBER")
        #     )

        # print(new_message.status)
        # print(message)

    def send_emails(self, flight, emails):
        message = f"Low price alert! Only £{flight.price} to fly from {flight.departure_city}-{flight.departure_airport_code} to {flight.arival_city}-{flight.arival_airport_code} from, {flight.departure_time} to {flight.return_time}."

        if flight.stopovers:
            message += f"\n\nFlight has 1 stop over, via {flight.via_city}."
        message += f"\n\nClick to book now! https://www.google.co.uk/flights?hl=en#flt={flight.departure_airport_code}.{flight.arival_airport_code}.{flight.departure_time}*{flight.arival_airport_code}.{flight.departure_airport_code}.{flight.return_time}"
        message = message.encode("utf-8")

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("SMTPLIB_EMAIL"),
                             password=os.getenv("SMTPLIB_PASSWORD"))
            for email in emails:
                connection.sendmail(from_addr=os.getenv(
                    "SMTPLIB_EMAIL"), to_addrs=email, msg=message)
