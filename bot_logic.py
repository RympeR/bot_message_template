import json
import random
import time
import re
from random import randint
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from multiprocessing.pool import ThreadPool

TABS = []
options = Options()
ua = UserAgent()
driver = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
# driver = webdriver.Chrome( executable_path='D:/develop/pypr/bot_messages_template/chromedriver',options=driver)
driver = webdriver.Chrome( executable_path='/home/rymper/bot_test/chromedriver',options=driver)


# driver.add_experimental_option("prefs", prefs)
# driver.add_argument("headless")

def answertounread(message):
    driver.get('https://prime.date/chat/:uid')
    time.sleep(4)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[1]/div/button[2]').click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div').click()
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]').click()

def get_profiles():
    with open('profiles.txt') as f:
        text = f.readlines()
        text = [row.replace('\n', '') for row in text]
    return text

def open_new_tab():
    TABS = driver.get_window_Handles()

def switch_tab(number):
    driver.switch_to_window(TABS.index(number))

def send_icebreaker():
    global driver
    driver.get('https://prime.date/icebreakers')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[3]').click()#icebreakers in progress
    time.sleep(randint(1,3))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[1]/td[5]/span[1]').click()#close icebraker
    time.sleep(randint(1,5))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[2]').click()#send icebreakers
    time.sleep(randint(1,4))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[1]/td[4]/div[1]/span[2]').click()#send first
    time.sleep(1,5)

def send_chat_message(id_profile, message):
    global driver
    manid = randint(50000000, 60000000)
    nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
    driver.get(nexturl)
    time.sleep(5)
    while (driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/p').text == 'No activity from man. Message cannot be send.'):
        manid = manid + 5
        nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
        driver.get(nexturl)
        time.sleep(5)
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message)
        except:
            manid = manid + randint(1,10)
            nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
            driver.get(nexturl)
            time.sleep(5)

def reply(id_profile, id_chat, message):
    pass

def notify(id_profile):
    pass

def get_user_id():
    return ''

def logout():
    try:
        driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        driver.get('https://prime.date/ladies')
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()
        driver.find_element_by_xpath('/html/body/div[1]/aside/div[1]/nav/a[11]').click()
        
        return True
    except Exception:
        return False

def get_offline(username, password):
    driver.get('https://prime.date/ladies')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()

def login(username, password, auth=False):
    if not auth:
        try:
            driver.get('https://prime.date/auth')
        except Exception as identifier:
            pass
        #     time.sleep(3)
        while driver.current_url == 'https://prime.date/auth':
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys(username)
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys(password)
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/button').click()
            time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()
    user_id = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]').text
    return user_id, True

def send_icebreaker_to_moderation(message):
    global driver
    driver.get('https://prime.date/icebreakers')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[1]')#icebrakerssend to moderation GO
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[1]/div[1]/div/div/div[1]').click()#открыть список
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[2]/div/textarea').send_keys(message)
    #driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[3]/div/button').click()
    
def test():

    accounts = [
        ['dariamironova997@gmail.com', 'dariamironova997'],
        ['2107miker@gmail.com', '2107miker'],
    ]
    driver.get('https://prime.date/auth')
    #     time.sleep(3)
    while driver.current_url == 'https://prime.date/auth':
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys(accounts[i][0])
        driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys(accounts[i][1])
        driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/button').click()
        time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()
    driver.find_element_by_tag_name('html').send_keys(Keys.LEFT_CONTROL + 't')

    # driver.close()
if __name__ == "__main__":
    test()
