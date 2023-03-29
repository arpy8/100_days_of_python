import csv

name = input("Name: ")
email = input("Email: ")
date = list(map(int, input("Date (YYYY-MM-DD): ").split("-")))

field_names = ["name", "email", "year", "month", "day"]
dict1 = {"name": name, "email": email, "year": date[0], "month": date[1], "day": date[2]}

with open("birthdays.csv", "a", newline='') as file:
    a = csv.DictWriter(file, fieldnames=field_names)
    a.writerow(dict1)
