import random
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.ChromeOptions()
# driver = webdriver.Chrome("chromedriver.exe")
prefs = {"profile.managed_default_content_settings.images": 2}
# driver.add_experimental_option("prefs", prefs)
# driver.add_argument("headless")
driver = webdriver.Chrome(executable_path='D:/develop/pypr/bot_messages_template/chromedriver', options=driver)

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
    driver.get('https://prime.date/auth')

    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys('2107miker@gmail.com')
    driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys('2107miker')

    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/button').click()
    # driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    # driver.get('https://www.ukr.net')

    time.sleep(5)

    driver.close()
test()
