import smtplib
import os
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open('quotes.txt') as file:
        all_quotes = file.readlines()
        quote = random.choice(all_quotes)

    # --- email part ---

    my_email = "arpitsengar99@gmail.com"
    my_pass = os.getenv("GMAIL_PASS")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Wednesday Motivation\n\n{quote}")
        connection.close()





