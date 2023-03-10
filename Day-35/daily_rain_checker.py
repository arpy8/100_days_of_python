import os
from requests import *
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "***********************"
account_sid = "***********************"
auth_token = "***********************"

weather_params = {
    "lat": "<latitude>",
    "lon": "<longitude>",
    "appid": api_key,
}

response = get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()

will_rain = False

for i in range(12):
    if 700 > response.json()["hourly"][i]["weather"][0]["id"]:
        will_rain = True
        break

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella ☔.",
        from_="+15673502660",
        to="***********************"
    )
    print(message.status)
    

else:
    print("it won't rain today.")

