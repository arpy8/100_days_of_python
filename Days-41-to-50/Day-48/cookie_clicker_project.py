import click
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

URL = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(r"C:\Users\asus\Documents\assets\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get(url=URL)

cookie = driver.find_element(By.XPATH, '//*[@id="cookie"]')
points = int(driver.find_element(By.ID, 'money').text.replace(",", ""))

while True:
    cookie.click()

    store = driver.find_element(By.ID, 'store')
    my_list = store.text.split("\n")[::2]
    a = [items.split(" - ") for items in my_list]

    for i in range(len(a)):
        if int(a[i][1].replace(",", "")) < points:
            what_to_buy = driver.find_element(By.XPATH, f'//*[@id="buy{a[i][0]}"]')
            what_to_buy.click()
