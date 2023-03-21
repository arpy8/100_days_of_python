import os
from requests import *
from pprint import pprint

SHEETY_USERNAME = os.getenv("SHEETY_USERNAME")
SHEETY_PASSWORD = os.getenv("SHEETY_PASSWORD")

sheety_endpoint = "https://api.sheety.co/925a1240bfd664959dc98e7080b4be59/flightDeals/prices"

# This class is responsible for talking to the Google Sheet.
# class DataManager:
#     def __init__(self):
response = post(sheety_endpoint, auth=(os.environ.get("SHEETY_USERNAME"),
                                      os.environ.get("SHEETY_PASSWORD")))

pprint(response.json())
# sheet_inputs = {"IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"},
#                     "IATA Code": {"TESTING"}
#                     }

# response = put(url=f"{sheety_endpoint}/2",json= sheet_inputs, auth=(os.environ.get("SHEETY_USERNAME"),
#                                                   os.environ.get("SHEETY_PASSWORD")))

# pprint(response.json())
# def
# for exercise in result["exercises"]:
#     sheet_inputs = {"workout":
#         {
#             "date": today_date,
#             "time": now_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"]
#         }
#     }
