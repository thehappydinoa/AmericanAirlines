from pprint import pprint

from requests import get

# Settings
URL = "http://airborne.gogoinflight.com/abp/ws/absServices/statusTray"


def get_info():
    try:
        response = get(URL)
        return response.json().get("Response")
    except ValueError as error:
        print(repr(error))
        exit(0)


def print_info(info_dict):
    print("\nFLIGHT INFO")
    flight_info = info_dict.get("flightInfo")
    print("Airline Name: %s" % flight_info.get("airlineName"))
    print("Airline Code: %s" % flight_info.get("airlineCode"))
    print("Tail Number: %s" % flight_info.get("tailNumber"))
    print("Flight Number Info: %s" % flight_info.get("flightNumberInfo"))
    print("Departure Airport Code: %s" %
          flight_info.get("departureAirportCode"))
    print("Destination Airport Code: %s" %
          flight_info.get("destinationAirportCode"))
    print("Departure Airport Code Iata: %s" %
          flight_info.get("departureAirportCodeIata"))
    print("Destination Airport Code Iata: %s" %
          flight_info.get("destinationAirportCodeIata"))
    print("Departure Airport Latitude: %s" %
          flight_info.get("departureAirportLatitude"))
    print("Destination Airport Latitude: %s" %
          flight_info.get("destinationAirportLatitude"))
    print("Departure Airport Longitude: %s" %
          flight_info.get("departureAirportLongitude"))
    print("Destination Airport Longitude: %s" %
          flight_info.get("destinationAirportLongitude"))
    print("Expected Arrival: %s" % flight_info.get("expectedArrival"))
    print("Latitude: %d" % flight_info.get("latitude"))
    print("Longitude: %d" % flight_info.get("longitude"))
    print("Altitude: %d" % flight_info.get("altitude"))
    print("H Speed: %d" % flight_info.get("hspeed"))
    print("V Speed: %d" % flight_info.get("vspeed"))

    print("\nSERVICE INFO")
    service_info = info_dict.get("serviceInfo")
    print("Service: %s" % service_info.get("service"))
    print("Remaining: %s" % service_info.get("remaining"))
    print("Quality: %s" % service_info.get("quality"))
    print("Alerts: %s" % service_info.get("alerts"))


def print_json(info_dict):
    pprint(info_dict)


if __name__ == "__main__":
    info_dict = get_info()
    print_info(info_dict)
