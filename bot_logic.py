import random
import json
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import re
from random import randint
from selenium.common.exceptions import NoSuchElementException

options = Options()
ua = UserAgent()
driver = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')


# driver.add_experimental_option("prefs", prefs)
# driver.add_argument("headless")

def get_profiles():
    with open('profiles.txt') as f:
        text = f.readlines()
        text = [row.replace('\n', '') for row in text]
    return text

def send_icebreaker_to_moderation(message):
    global driver
    driver.get('https://prime.date/icebreakers')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[1]')#icebrakerssend to moderation GO
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[1]/div[1]/div/div/div[1]').click()#открыть список
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[2]/div/textarea').send_keys(message)
    #driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[3]/div/button').click()

def send_icebreaker():
    global driver
    driver.get('https://prime.date/icebreakers')
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[3]').click()#icebreakers in progress
    time.sleep(randint(1,3))
    #driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[1]/td[5]/span[1]').click()#close icebraker
    time.sleep(randint(1,5))
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[2]').click()#send icebreakers
    time.sleep(randint(1,4))
    #driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[1]/td[4]/div[1]/span[2]').click()#send first
    time.sleep(1,5)

def send_chat_message(id_profile, message, counter):
    global driver
    manid = randint(40000000, 900000000)
    nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
    driver.get(nexturl)
    time.sleep(5)
    blacklist = []#чёрный список для уникальной рассылки
    for i in range (1,counter):
        try:
            driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/p')
            if (driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/p').text == 'No activity from man. Message cannot be send.'):
                manid = manid + randint(1,10)
                nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
                driver.get(nexturl)
                time.sleep(4)
        except NoSuchElementException:
            if(blacklist.index(manid)>=0):
                blacklist.append(manid)
                driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message[i-1])
                #driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]').click()


def reply(id_profile, id_chat, message):
    pass

def notify(id_profile):
    pass

def answertounread(message):#отвечает на первое неотвеченное сообщение
    driver.get('https://prime.date/chat/:uid')
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[1]/div/button[2]').click()
    time.sleep(3)
    b = 1
    while(True):
        try:
            driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div{b}/div[1]/div[1]/p")
            b = b + 1
        except NoSuchElementException:
            break
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div').click()
    if(driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/div/div{b}/div[1]/div[1]/p").get_attribute('class') !='message-text-like'):
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message)
        time.sleep(2)
        #driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]').click()

def alert_by_new_message():
    pass

def login(accounts):
    global driver
    #     time.sleep(3)
    user_id = []

    driver.execute_script("window.open('https://prime.date/auth')")
    driver.switch_to.window(driver.window_handles[x+1])
    time.sleep(2)
    while driver.current_url == 'https://prime.date/auth':
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").clear()
        except NoSuchElementException:
            pass
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").clear()
        except NoSuchElementException:
            pass
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys(accounts[x][0])
            driver.find_element_by_xpath("/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys(accounts[x][1])
            driver.find_element_by_xpath('/html/body/div[1]/div[4]/div/form/button').click()
            time.sleep(2)
        except NoSuchElementException:
            pass
    driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()
    p = 1
    #while(driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[{p}]")):
     #   user_id.append(driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[{p}]/div[1]").text)
      #  p = p +1
       # try:
        #    driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[{p}]/div[1]")
        #except NoSuchElementException:
         #   break
    return user_id


def get_user_id():
    return ''
def test():
    global driver
    driver = webdriver.Chrome(executable_path='D:/bot_message_template-master/chromedriver',options=driver)
    #важные клики для отправки сообщений закомменчены в функциях во избежание проблем
    uh = 0
    counter = 0
    user_id = []
    accounts = [
        ['dariamironova997@gmail.com', 'dariamironova997'],
    ]

    messages = ['So cute', 'Miss me dear?', 'Hello honey :)']
    while(True):
        print("Enter 1 to login, 2 to send messages, 3 to send icebreakers, 4 to answer to first unread message")
        k = int(input())
        if(k==1):
            user_id = login(accounts)#проверить логин на аккаунте, где несколько анкет, чтобы выцапывать именно айдишники анкет, лаги с очисткой поля пароль хз почему
            for x in range (0,len(user_id)-1):
                print(f"enter {x+1} for managing account {user_id[x]}")
            input(int(uh))
        elif(k==2):
            if(uh>0):
                print("Enter amount of messages")
                input(int(counter))
                #сгенерировать нужное кол-во сообщений
                send_chat_message(user_id[uh-1],messages, counter)#уникальная рассылка с созданием чёрного списка, чтобы не повторяться с собеседниками
        elif(k==3):
            #cгенерировать/внести куда-то сообщения для отправки айсбрекера
            send_icebreaker_to_moderation(messages[2])# нужен аккаунт, где несколько анкет
            send_icebreaker()#смотреть комментарий выше
        elif(k==4):
            answertounread(messages[1])#при необходимости зациклить (?)

        driver.find_element_by_tag_name('html').send_keys(Keys.LEFT_CONTROL + 't')

    # driver.close()
if __name__ == "__main__":
     test()
