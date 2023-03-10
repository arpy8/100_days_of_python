import os
from requests import *
from datetime import *
from twilio.rest import Client

today = date.today()

yesterday = today - timedelta(days=1)
day_before_yesterday = today - timedelta(days=2)

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API = "XO7R4IZ43NZDWDV7"
NEWS_API = "83ace640242a42a3a5d4d29d120b6c6b"
TWILIO_SID = "AC8e2f108bf91834f5503f73c813929875"
TWILIO_AUTH_TOKEN = "60eee7077845c856491eda1345152994"

stock_parameters = {"function": "TIME_SERIES_DAILY_ADJUSTED", "symbol": STOCK_NAME, "apikey": STOCK_API}
stock_response = get(url=STOCK_ENDPOINT, params=stock_parameters)

yesterday_stock_price = float(stock_response.json()["Time Series (Daily)"][str(yesterday)]["4. close"])
dby_stock_price = float(stock_response.json()["Time Series (Daily)"][str(day_before_yesterday)]["4. close"])

diff = abs(dby_stock_price - yesterday_stock_price)
emoji = "🔻"

if dby_stock_price > yesterday_stock_price:
    prcnt = diff / dby_stock_price * 100
else:
    prcnt = diff / yesterday_stock_price * 100
    emoji = "🔺"

if prcnt > 5:
    news_parameters = {"apiKey": NEWS_API, "qInTitle": COMPANY_NAME, "language": "en", "searchln": "stocks"}
    news_response = get(url=NEWS_ENDPOINT, params=news_parameters)

    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    formatted_articles = [f"{STOCK_NAME}: {emoji}{round(prcnt, 2)}%\nHeadline : \n{article['title']}. \nBrief : \n{article['description']}" for article in
                          three_articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(body=article, from_="+15673502660", to="+919311389851")
    print(message.status)