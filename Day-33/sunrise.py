from requests import *
from datetime import *

MY_LAT = 28.669155
MY_LONG = 77.453758
FORMAT = 0

parameters = {"lat": MY_LAT, "long": MY_LONG, "formatted": 0}

response = get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.now()

print(time_now.hour)

