from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.python.org/"

service = Service(r"C:\Users\asus\Documents\assets\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url=URL)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }
print(events)
driver.quit()
