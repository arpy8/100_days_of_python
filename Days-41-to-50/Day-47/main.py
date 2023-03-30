import requests
from bs4 import BeautifulSoup
import smtplib
import os

URL = "https://www.amazon.in/Samsung-Galaxy-Cloud-128GB-Storage/dp/B08VB57558?ref_=Oct_DLandingS_D_38b39bc2_60"
MY_EMAIL = "arpitsengar99@gmail.com"
MY_PASSWORD = os.getenv("GMAIL_PASS")
PARAMS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) "
                        "Chrome/111.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.8"}

response = requests.get(url=URL, headers=PARAMS)

soup = BeautifulSoup(response.text, "html.parser")

price = []
product_title = ""

try:
    for i in soup.find(class_="priceToPay"):
        price += i
    product_price = int(price[0][1:])

except ValueError:
    product_price = int(str(price[0]).replace(",", "")[1:])

for title in soup.find(id="productTitle"):
    product_title = title.strip()

user_price = 60000

# email part

message = f"""Subject:Alert, Lower price on {product_title.split()[0]}


{product_title} is now available for just {product_price} rupees.
You can consider buying it right now.
Here\'s the link
{URL}"""

if user_price >= product_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=message)
