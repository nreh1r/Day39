class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, flight, stopovers=0, via_city=""):
        # data["data"][0]["price"]
        self.price = flight["price"]
        self.departure_airport_code = flight["flyFrom"]
        self.departure_city = flight["cityFrom"]
        self.arival_airport_code = flight["flyTo"]
        self.arival_city = flight["cityTo"]
        self.departure_time = flight["local_departure"].split("T")[0]
        self.return_time = flight["route"][1]["local_departure"].split("T")[0]
        self.stopovers = stopovers
        self.via_city = via_city
