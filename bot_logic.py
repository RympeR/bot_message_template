import random
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent

options = Options()
ua = UserAgent()
driver = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
userAgent = ua.random
print(userAgent)
options.add_argument(f'user-agent={userAgent}')
driver = webdriver.Chrome( executable_path='D:/develop/pypr/bot_messages_template/chromedriver',options=driver)


# driver.add_experimental_option("prefs", prefs)
# driver.add_argument("headless")

def get_profiles():
    with open('profiles.txt') as f:
        text = f.readlines()
        text = [row.replace('\n', '') for row in text]
    return text

def send_icebreaker(id_profile, message):
    pass

def send_chat_message(id_profile, message):
    pass

def reply(id_profile, id_chat, message):
    pass

def notify(id_profile):
    pass


def login(username, password):
    id_profile = int()
    return id_profile


def test():
    accounts = [
        ['zhelyaskova1M@gmail.com', '54321012'],
        ['2107miker@gmail.com', '2107miker'],
    ]
    for i in range(2):
        for j in range(2):
            driver.get('https://prime.date/auth')
            time.sleep(3)
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys(accounts[i][0])
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys(accounts[i][1])
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/button').click()

        driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')

    # driver.close()
test()
