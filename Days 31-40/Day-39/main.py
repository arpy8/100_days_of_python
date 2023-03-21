from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch

sheet_data = DataManager().prices
print(sheet_data)
flightsearch = FlightSearch.flight_code()
for items in sheet_data:
    if items["iataCode"] != "":
        a = FlightSearch(items["iataCode"])
        print(a.flight_code())
