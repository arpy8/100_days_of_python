import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, \
    ElementNotInteractableException

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1) AppleWebKit/605.1.15 (KHTML, like Gecko) "
                  "Version/14.0.2 Safari/605.1.15",
    "Accept-Language": "en-US"
}
URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B" \
      "%22west%22%3A-122.56825484228516%2C%22east%22%3A-122.29840315771484%2C%22south%22%3A37.685549641111386%2C" \
      "%22north%22%3A37.8649244642985%7D%2C%22mapZoom%22%3A12%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B" \
      "%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22" \
      "%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B" \
      "%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
      "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22" \
      "%3Atrue%7D"
CHROME_DRIVER_PATH = r"C:\Users\asus\Documents\assets\chromedriver.exe"


class DataManager:
    def __init__(self):

        self.links = None
        response = requests.get(url=URL, headers=headers)
        response.raise_for_status()

        self.soup = BeautifulSoup(response.text, "lxml")
        self.prices = []
        self.address = []
        self.links = []

    def get_prices_and_address(self):
        all_prices = self.soup.find_all(class_="property-card-data")

        # colecting prices
        for price in all_prices:
            try:
                self.prices.append(int((price.get_text().split("$")[1]).split("+")[0].replace(",", "")))
            except ValueError:
                self.prices.append(int(price.get_text().split("$")[1].split("+")[0].replace(",", "").split("/mo1")[0]))

        # colecting addresses
        all_adrs = self.soup.find_all(class_="property-card-link")
        for item in all_adrs:
            if item.get_text().split("\n") != ['']:
                self.address.append(item.get_text().split("\n")[0])

        # colecting links
        all_links = self.soup.select("article div div a")
        temp = []
        for item in all_links:
            if item.get("href")[0] == "/":
                temp.append(f"https://www.zillow.com{item.get('href')}")
            else:
                temp.append(item.get("href"))

        for item in temp[::2]:
            self.links.append(item)

        return [self.address, self.prices, self.links]

    def form_filler(self):

        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        driver.maximize_window()

        for i in range(len(self.get_prices_and_address()[0])):
            try:
                driver.get('https://forms.gle/WdDxeBFvBxdwPDWA7')
                driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div['
                                    '1]/input').send_keys(str(self.get_prices_and_address()[0][i]))
                time.sleep(1)
                driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div['
                                    '1]/input').send_keys(str(self.get_prices_and_address()[1][i]))
                time.sleep(1)
                driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div['
                                    '1]/input').send_keys(str(self.get_prices_and_address()[2][i]))
                driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

            except ElementNotInteractableException:
                pass


data_manager = DataManager()

time.sleep(2)

data_manager.form_filler()
