import os
from requests import *
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "c685b352b40bc7c23f9d921e9f9a45b1"
account_sid = "ACs8e2f108bf91834f5503f73c813929875"
auth_token = "60eee7077845c856491eda1345152994"

weather_params = {
    "lat": 28.669155,
    "lon": 77.453758,
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
        to="+919311389851"
    )
    print(message.status)
    message = client.messages.create(
        body="It's not going to rain today.",
        from_="+15673502660",
        to="+919311389851"
    )

else:
    print("it won't rain today.")

