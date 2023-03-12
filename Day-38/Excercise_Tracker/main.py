import os
from requests import *
from datetime import *

APP_ID = os.getenv("NUTRITIONIX_APP_ID")
API_ID = os.getenv("NUTRITIONIX_API_KEY")

GENDER = "male"
WEIGHT = 60
HEIGHT = 169
AGE = 18

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/925a1240bfd664959dc98e7080b4be59/workoutTracking/workouts"

user_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_ID
}
user_params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = post(url=exercise_endpoint, json=user_params, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {"workout":
        {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }


sheet_response = post(
    sheety_endpoint,
    json=sheet_inputs,
    auth=(
        os.environ.get("SHEETY_USERNAME"),
        os.environ.get("SHEETY_PASSWORD")
    )
)

print(sheet_response.text)