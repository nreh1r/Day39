import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from flight_data import FlightData
import json

load_dotenv()


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.

    def search_city(self, city):

        headers = {
            "apikey": os.getenv("TEQUILA_API_KEY"),
            "Content-Type": "application/json"
        }

        query = {
            "term": city
        }

        response = requests.get(url=os.getenv(
            "TEQUILA_ENDPOINT_LOCATIONS"), params=query, headers=headers)
        # print(response.text)
        data = response.json()
        code = data["locations"][0]["code"]
        # print(code)
        return code

    def search_flights(self, city):
        headers = {
            "apikey": os.getenv("TEQUILA_API_KEY"),
            "Content-Type": "application/json"
        }

        early_departure = datetime.now() + timedelta(days=1)
        late_departure = datetime.now() + timedelta(days=180)

        query = {
            "fly_from": "LON",
            "fly_to": city,
            "date_from": early_departure.strftime("%d/%m/%Y"),
            "date_to": late_departure.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight-type": "round",
            "curr": "GBP",
            "max_stopovers": 0
        }

        try:
            response = requests.get(url=os.getenv(
                "TEQUILA_ENDPOINT_FLIGHT_SEARCH"), params=query, headers=headers)
            data = response.json()
            # data["data"][0]["price"]
            # print(data["data"])
            return FlightData(data["data"][0])
        except IndexError:
            try:
                query["max_stopovers"] = 2
                query["max_sector_stopovers"] = 1
                response = requests.get(url=os.getenv(
                    "TEQUILA_ENDPOINT_FLIGHT_SEARCH"), params=query, headers=headers)
                data = response.json()
                test_for_error = data["data"][0]
            except IndexError:
                return None
            else:
                # print("No direct flights but found flights with a stop over.")
                # data["data"][0]["price"]
                # print(data["data"])
                stop_over_city = data["data"][0]["route"][0]["cityTo"]
                return FlightData(data["data"][0], 1, stop_over_city)
