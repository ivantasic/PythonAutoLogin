from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        time.sleep(3)
        email = bot.find_element_by_class_name('_2hvTZ pexuQ zyHYP')
        password = bot.find_element_by_class_name('_2hvTZ pexuQ zyHYP')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)

ib = InstaBot('#ussername', '#password')
ib.login()