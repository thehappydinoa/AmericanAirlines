import json
from pprint import pprint

import requests

# Settings
URL_1 = "http://airborne.gogoinflight.com/abp/ws/absServices/statusTray"
URL_2 = "http://services.inflightpanasonic.aero/inflight/services/flightdata/v1/flightdata"

MAP_1 = {
    "flightInfo": {
        "logo": "Logo",
        "airlineName": "Airline Name",
        "airlineCode": "Airline Code",
        "tailNumber": "Tail Number",
        "flightNumberInfo": "Flight Number Info",
        "departureAirportCode": "Departure Airport Code",
        "destinationAirportCode": "Destination Airport Code",
        "departureAirportCodeIata": "Departure Airport Code Iata",
        "destinationAirportCodeIata": "Destination Airport Code Iata",
        "departureAirportLatitude": "Departure Airport Latitude",
        "destinationAirportLatitude": "Destination Airport Latitude",
        "departureAirportLongitude": "Departure Airport Longitude",
        "destinationAirportLongitude": "Destination Airport Latitude",
        "origin": "Origin",
        "destination": "Destination",
        "departureCity": "Departure City",
        "destinationCity": "Destination City",
        "expectedArrival": "Expected Arrival",
        "latitude": "Latitude",
        "longitude": "Longitude",
        "altitude": "Altitude",
        "hspeed": "H Speed",
        "vspeed": "V Speed",
        "abpVersion": "ADP Version",
        "acpuVersion": "ACPU Version",
        "videoService": "Video Service",
    },
    "serviceInfo": {
        "service": "Service",
        "remaining": "Remaining",
        "quality": "Quality",
        "alerts": "Alerts"
    }
}
MAP_2 = {
    "td_id_fltdata_ground_speed": "Ground Speed",
    "td_id_fltdata_time_to_destination": "Time to Destination",
    "td_id_fltdata_wind_speed": "Wind Speed",
    "td_id_fltdata_mach": "Mach",
    "td_id_fltdata_outside_air_temp": "Outside Air Temperature",
    "td_id_fltdata_head_wind_speed": "Head Wind Speed",
    "td_id_fltdata_distance_to_destination": "Distance to Destination",
    "td_id_fltdata_altitude": "Altitude",
    "td_id_fltdata_present_position_latitude": "00039064",
    "td_id_fltdata_present_position_longitude": "80075467",
    "td_id_fltdata_destination_latitude": "Destination Latitude",
    "td_id_fltdata_destination_longitude": "Destination Longitude",
    "td_id_fltdata_destination_id": "Destination ID",
    "td_id_fltdata_departure_id": "Departure ID",
    "td_id_fltdata_flight_number": "Flight Number",
    "td_id_fltdata_destination_baggage_id": "Destination Baggage ID",
    "td_id_fltdata_departure_baggage_id": "Departure Baggage ID",
    "td_id_airframe_tail_number": "Tail Number",
    "td_id_flight_phase": "Flight Phase",
    "td_id_route_id": "Route ID",
    "td_id_fltdata_time_at_origin": "Time at Origin",
    "td_id_fltdata_time_at_destination": "Time at Destination",
    "td_id_fltdata_distance_from_origin": "Distance from Origin",
    "td_id_fltdata_distance_traveled": "Distance Traveled",
    "td_id_fltdata_estimated_arrival_time": "Estimated Arrival Time",
    "td_id_fltdata_time_at_takeoff": "Time at Takeoff",
    "td_id_fltdata_departure_latitude": "Departure Latitude",
    "td_id_fltdata_departure_longitude": "Departure Longitude",
    "td_id_pdi_fltdata_departure_iata": "Departure Iata",
    "td_id_pdi_fltdata_departure_time_scheduled": "Departure Time Scheduled",
    "td_id_pdi_fltdata_arrival_iata": "Arrival Iata",
    "td_id_fltdata_wind_direction": "Wind Direction",
    "td_id_decompression": "Decompression",
    "td_id_weight_on_wheels": "Weight on Wheels",
    "td_id_all_doors_closed": "All Doors Closed",
    "td_id_media_date": "Media Date",
    "td_id_extv_channel_listing_version": "EXTV Channel Listing Version",
}


def try_urls(urls=[URL_1, URL_2]):
    for url in urls:
        try:
            response = requests.get(url)
            return response.json()
        except (requests.exceptions.ConnectionError, ValueError):
            continue
    print("Failed to gather information")
    exit(1)


def format_value(value):
    if isinstance(value, str):
        if value.startswith("0"):
            try:
                value = str(int(value))
            except (TypeError, ValueError):
                pass
    return value


def print_stat(title, value):
    if title and value:
        value = format_value(value)
        print("{title}: {value}".format(title=title, value=value))


def map_values(response, map):
    for map_key, map_value in map.items():
        if isinstance(map_value, dict):
            sub_dict = response.get(map_key)
            for k, v in map_value.items():
                title = v
                value = sub_dict.get(k)
                print_stat(title, value)
        else:
            title = map_value
            value = response.get(map_key)
            print_stat(title, value)


def print_json(info_dict):
    pprint(info_dict)


if __name__ == "__main__":
    response = try_urls()
    # response = json.loads(open("response_2.json").read())
    map = MAP_2
    if "Response" in response.keys():
        response = response.get("Response")
        map = MAP_1

    map_values(response, map)
