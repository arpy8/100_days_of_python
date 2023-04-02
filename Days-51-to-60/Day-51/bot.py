import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "arpitsengar99@gmail.com"
TWITTER_PASSWORD = os.getenv("PASSWORD")


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.maximize_window()
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(2)
        self.driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
        self.driver.find_element(By.CLASS_NAME, 'start-text').click()
        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, 'download-speed').text
        self.up = self.driver.find_element(By.CLASS_NAME, 'upload-speed').text
        print(f"Download speed : {self.down}")
        print(f"Upload speed : {self.up}")

    def tweet_at_provider(self):
        driver = self.driver
        driver.get(url="https://twitter.com/login")
        time.sleep(2)

        url_link = 'https://twitter.com/login'
        self.driver.get(url_link)
        time.sleep(6)

        login_btn = self.driver.find_element(By.CLASS_NAME, 'r-30o5oe')
        login_btn.send_keys(TWITTER_EMAIL)

        print(login_btn)

        time.sleep(6)

        next_btn = self.driver.find_elements(By.CLASS_NAME, 'css-901oao')

        for item in next_btn:
            try:
                if item.text == 'Next':
                    try:
                        item.click()
                    except:
                        pass
            except:
                pass

        time.sleep(2)

        password = self.driver.find_element(By.NAME, 'password')
        time.sleep(1)
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        time.sleep(2)

        next_btn = self.driver.find_elements(By.CLASS_NAME, 'css-901oao')

        for item in next_btn:

            try:
                if item.text == 'Log in':
                    try:
                        item.click()
                    except:
                        pass
            except:
                pass

        time.sleep(2)

        text_tweet = f"My current speed is {self.up} and {self.down}"

        new_tweet = self.driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
        new_tweet.send_keys(text_tweet)

        time.sleep(2)

        tweet_btn = self.driver.find_elements(By.CLASS_NAME, 'css-901oao')

        for item in tweet_btn:

            try:
                if item.text == 'Tweet':
                    try:
                        item.click()

                    except:
                        pass
            except:
                pass

        time.sleep(15)

        self.driver.close()
        self.driver.quit()