from bot import InternetSpeedTwitterBot

CHROME_DRIVER_PATH = r"C:\Users\asus\Documents\assets\chromedriver.exe"

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
