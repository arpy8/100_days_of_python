import os
from requests import *
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
OWM_API_KEY = os.getenv("OWM_API_KEY")
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
LAT = os.getenv("my_lat")
LONG = os.getenv("my_long")

weather_params = {
    "lat": LAT,
    "lon": LONG,
    "appid": OWM_API_KEY,
}

response = get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

will_rain = False

for i in range(12):
    if 1000 > response.json()["hourly"][i]["weather"][0]["id"]:
        will_rain = True
        break

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔.",
        from_="+15673502660",
        to=os.environ.get("Mobile_Number")
    )
    print(message.status)
    

else:
    print("it won't rain today.")

