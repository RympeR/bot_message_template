import json
import random
import re
import time
from random import randint
import requests

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class DriverLogic:
    def __init__(self):
        options = Options()
        ua = UserAgent()
        driver = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        userAgent = ua.random
        options.add_argument(f'user-agent={userAgent}')
        # driver.add_experimental_option("prefs", prefs)
        # driver.add_argument("headless")

    def get_html(self, url):
        response = requests.get(url)
        return response.text

    def get_bs_object(self, hmtl):
        bs = BeautifulSoup(hmtl, parser='html.parser')
        return bs

    def get_profiles(self):
        with open('profiles.txt') as f:
            text = f.readlines()
            text = [row.replace('\n', '') for row in text]
        return text

    def getladynameandage(self, id_profile):
        global driver
        # save name and age
        driver.get(f"https://prime.date/profile-woman/{id_profile}")
        ladynameandage = driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div/div[1]/div[2]/div[1]/div[2]/div[1]").text
        print(ladynameandage)
        return ladynameandage

    def send_icebreaker_to_moderation(self, id_profile, message):
        global driver
        ladynameandage = getladynameandage(id_profile)
        driver.get('https://prime.date/icebreakers')
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[1]')  # GO TO send to moderation
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[1]/div[1]/div/div/div[1]').click()  # открыть список
        b = 1
        while (True):
            try:
                if driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[1]/div[1]/div/div/div[3]/ul/li[{b}]/span/span").text == ladynameandage:
                    driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[1]/div[1]/div/div/div[3]/ul/li[{b}]/span").click()  # click to choose lady
                    print(b)
                    driver.find_element_by_xpath(
                        '/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[2]/div/textarea').send_keys(
                        message)
                    # driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/main/div/div/div[2]/div[3]/div/button').click()
                    return True
                    break
                b = b + 1
            except NoSuchElementException:
                break
                return False

    def send_icebreaker(self, id_profile):
        global driver
        ladynameandage = getladynameandage(id_profile)
        driver.get('https://prime.date/icebreakers')
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[3]').click()  # GO TO icebreakers in progress
        time.sleep(randint(1, 3))
        b = 1
        while (True):
            try:
                if driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[{b}]/td[2]/p[2]").text == ladynameandage:
                    # driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[{b}]/td[5]/span[1]").click()#click to close icebreaker
                    print(b)
                    break
                b = b + 1
            except NoSuchElementException:
                break
        time.sleep(randint(1, 4))
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[1]/div/div/div/div[2]/button[2]').click()  # GO TO send icebreakers
        time.sleep(randint(1, 4))
        b = 1
        while (True):
            try:
                if driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[{b}]/td[2]/p[2]").text == ladynameandage:
                    # driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/main/div/table/tbody/tr[{b}]/td[4]/div[1]/span[2]").click()#click to send icebreaker
                    print(b)
                    break
                    return True
                b = b + 1
            except NoSuchElementException:
                break
                return False

    def send_chat_message(self, id_profile, message):  # READY TO GO
        global driver
        manid = randint(40000000, 900000000)
        nexturl = 'https://prime.date/chat/' + id_profile + '_' + str(manid)
        driver.get(nexturl)
        time.sleep(2)
        blacklist = []  # чёрный список для уникальной рассылки
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/p')
            if (driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/p').text == 'No activity from man. Message cannot be send.'):
                return False  # отправка невозможна, сообщение не отправлено
        except NoSuchElementException:
            if(blacklist.index(manid) < 0):
                blacklist.append(manid)
                driver.find_element_by_xpath(
                    '/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message)
                # driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]').click()
                return True  # сообщение отправлено
            else:
                return False  # мы обосрались, этот мужик уже был

    def reply(self, id_profile, id_chat, message):
        pass

    def notify(self, id_profile):
        global driver
        ladynameandage = getladynameandage(id_profile)
        driver.get('https://prime.date/chat/:uid')
        driver.find_element_by_xpath(
            "/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[2]/div/label/span[1]").click()  # men online
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[1]/div/button[2]').click()  # unanswered
        b = 1
        while (True):
            try:
                if driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div[{b}]/div").text == ladynameandage:
                    driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div[{b}]/div").click()
                    print(b)
                    break
                b = b + 1
            except NoSuchElementException:
                break
        try:  # /html/body/div[1]/section/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[10]/div/div/div[3]
            if (driver.find_element_by_xpath(
                    "/html/body/div[1]/section/div/div/div[1]/div[2]/div[2]/div/div[1]/div").get_attribute(
                    "class") != "empty-state-list"):
                print(
                    f"{id_profile}, {ladynameandage} has unanswered messages in chats!")
        except:
            pass

    # отвечает на первое неотвеченное сообщение
    def answertounread(self, id_profile, message):
        global driver
        ladynameandage = getladynameandage(id_profile)
        driver.get('https://prime.date/chat/:uid')
        time.sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[1]/div/button[2]').click()  # unanswered
        b = 1
        while (True):
            try:
                if driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div[{b}]/div").text == ladynameandage:
                    driver.find_element_by_xpath(
                        f"/html/body/div[1]/section/div/div/div[1]/div[1]/div/div[4]/div/div[1]/div[{b}]/div").click()
                    print(b)
                    break
                b = b + 1
            except NoSuchElementException:
                break
                return False
        time.sleep(2)
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/section/div/div/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div/div').click()
        except NoSuchElementException:
            return False
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/textarea').send_keys(message)
        time.sleep(1)
        # driver.find_element_by_xpath('/html/body/div[1]/section/div/div/div[2]/div/div[2]/div[1]/div[2]/div[2]/div[2]/button[2]').click()
        return True

    def alert_by_new_message(self):
        pass

    def login(self, accounts):
        global driver
        # time.sleep(3)
        user_id = []

        driver.execute_script("window.open('https://prime.date/auth')")
        driver.switch_to.window(driver.window_handles[x+1])
        time.sleep(2)
        while driver.current_url == 'https://prime.date/auth':
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/form/div[2]/input").clear()
            except NoSuchElementException:
                pass
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/form/div[3]/input").clear()
            except NoSuchElementException:
                pass
            try:
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/form/div[2]/input").send_keys(accounts[x][0])
                driver.find_element_by_xpath(
                    "/html/body/div[1]/div[4]/div/form/div[3]/input").send_keys(accounts[x][1])
                driver.find_element_by_xpath(
                    '/html/body/div[1]/div[4]/div/form/button').click()
                time.sleep(2)
            except NoSuchElementException:
                pass
        driver.find_element_by_xpath(
            '/html/body/div[1]/section/div/div[1]/div/div[3]/div[3]/div/label/input').click()
        p = 1
        # while(driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div/div[{p}]")):
        #   user_id.append(driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[{p}]/div[1]").text)
        #  p = p +1
        # try:
        #    driver.find_element_by_xpath(f"/html/body/div[1]/section/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div[1]/div[{p}]/div[1]")
        # except NoSuchElementException:
        #   break
        return user_id

    def get_user_id(self):
        return ''

    def test(self):
        global driver
        driver = webdriver.Chrome(
            executable_path='D:/bot_message_template-master/chromedriver', options=driver)
        # важные клики для отправки сообщений закомменчены в функциях во избежание проблем
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
            if(k == 1):
                # проверить логин на аккаунте, где несколько анкет, чтобы выцапывать именно айдишники анкет, лаги с очисткой поля пароль хз почему
                user_id = login(accounts)
                for x in range(0, len(user_id)-1):
                    print(f"enter {x+1} for managing account {user_id[x]}")
                input(int(uh))
            elif(k == 2):
                if(uh > 0):
                    print("Enter amount of messages")
                    input(int(counter))
                    # сгенерировать нужное кол-во сообщений
                    # уникальная рассылка с созданием чёрного списка, чтобы не повторяться с собеседниками
                    send_chat_message(user_id[uh-1], messages, counter)
            elif(k == 3):
                # cгенерировать/внести куда-то сообщения для отправки айсбрекера
                # нужен аккаунт, где несколько анкет
                send_icebreaker_to_moderation(messages[2])
                send_icebreaker()  # смотреть комментарий выше
            elif(k == 4):
                answertounread(messages[1])  # при необходимости зациклить (?)

            driver.find_element_by_tag_name(
                'html').send_keys(Keys.LEFT_CONTROL + 't')


    # driver.close()
if __name__ == "__main__":
    test()
