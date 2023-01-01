# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()
sheet_data = data_manager.get_data()

# print(sheet_data)

flight_search = FlightSearch()
for city in sheet_data:
    if city["iataCode"] == "":
        city["iataCode"] = flight_search.search_city(city["city"])
        data_manager.update_data(city)

    price = flight_search.search_flights(city["iataCode"])
    if price:
        # print(f"{city['city']}: £{price.price}")
        if price.price < city["lowestPrice"]:
            emails = data_manager.get_emails()
            notification_manager.send_message(price)
            notification_manager.send_emails(price, emails)
    else:
        print(f"No flights to {city['city']} found")


# print(sheet_data)
