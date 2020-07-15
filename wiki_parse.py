import requests
from bs4 import BeautifulSoup as bs
import os
import time
import lxml
import csv
from fake_useragent import UserAgent
from selenium import webdriver

ua = UserAgent()
headers = {'accept': '*/*', 'user-agent': ua.firefox}
os.system("cls")

BASE_URL       = 'https://en.wikipedia.org'
BASE_URL_WIKI  = 'https://en.wikipedia.org/wiki/'
BASE_URL_IMAGE = 'https://en.wikipedia.org/wiki/File:'


def pretify():
    with open('city.txt', 'r') as f:
        text = f.read()
        text = text.replace('::', '\n')
        text = text.replace('-', '_')
        with open('city_list.txt', 'w') as f1:
            f1.write(text.title())


def get_links_state():
    r = requests.get('https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States')
    html = bs(r.content, 'html.parser')
    with open('link_states.txt', 'w') as f:
        for el in html.select('.wikitable > * > tr > th >a'):
            print(el.attrs['href'])
            f.write(el.attrs['href'] + '\n' )


text = list()
# with open('link_states.txt', 'r') as f:
#         text = f.readlines()
#         print(text)


def get_states_description():
    image_name = 1
    with open('states_info.txt', 'w') as f:
        for i, el in enumerate(text):
            time.sleep(4)
            req = BASE_URL + text[i][:len(text[i]) - 1]
            print(req)
            r = requests.get(BASE_URL + text[i][:len(text[i]) - 1])
            k = 0
            soup = bs(r.content, 'lxml')
            f.write('Info about: ' + text[i][:len(text[i]) - 1] + '\n')
            for el in soup.find_all('p'):
                k += 1
                if k in (3, 4):
                    f.write(el.text + '\n')
                    print(el.text)
                elif k > 4:
                    break
                elif k < 3:
                    continue

def get_html(url):
    r = requests.get(url, headers=headers)
    return r.text


def csv_formatter(data):
    with open('county.csv', 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow((data['name'], data['first'], data['second']))

def county_description():
    with open('county.txt', 'r') as c:
        text = c.readlines()

        for i, el in enumerate(text):
            time.sleep(1)
            url = BASE_URL_WIKI + el
            # soup = bs(get_html(url),'html5lib')
            soup = bs(get_html('https://en.wikipedia.org/wiki/Kodiak_Island'),'html5lib')
            print(url)
            name = el
            # print(get_html(url))
            first = soup.find_all('div', class_='mw-parser-output')
            print(first)
            break

# for el in soup.find_all(attrs={'class':'thumbborder'}):
#     print(el.attrs['src'])

    # img_data = requests.get(BASE_URL_IMAGE  + el.attrs['src']).content
    # with open('state_images/' + str(image_name) + '.jpg', 'wb') as handler:
    #     handler.write(img_data)
    # image_name += 1

def get_description(driver):
    res = driver.find_element_by_class_name('mw-parser-output').find_element_by_class_name('reflist')
    result = driver.find_element_by_class_name('mw-parser-output').find_elements_by_tag_name('p')
    name = driver.find_element_by_id('firstHeading').text
    k = 0
    first = ''
    second = ''
    for res in result:
        k += 1
        if k == 1:
            first = res.text
        elif k == 2:
            second = res.text
        else:
            break
    data = {'name' : name, 'first' : first,'second' : second}
    print('data:: ' + data['name'])
    csv_formatter(data)


def main():
    driver = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    driver.add_experimental_option("prefs", prefs)
    driver.add_argument("headless")
    driver = webdriver.Chrome(executable_path='D:/develop/pypr/bot_messages_template/chromedriver',chrome_options=driver)

    with open('city_list.txt', 'r') as f:
        text = f.readlines()
        for row in text:
            state, county, city = row.split(' ')
            driver.get(BASE_URL_WIKI + city)
            try:
                get_description(driver)
            except Exception as e:
                try:
                    search_res = driver.find_element_by_class_name('mw-parser-output').find_element_by_tag_name('ul').find_elements_by_tag_name('li')
                    current_links = []
                    for result in search_res:
                        current_links.append({'text': result.find_element_by_tag_name('a').text, 'href' : result.find_element_by_tag_name('a').get_attribute('href')})
                    for ind, link in enumerate(current_links):
                        if state.lower() in current_links[ind]['text'].lower():
                            driver.get(current_links[ind]['href'])
                            get_description(driver)
                        if 'city' in current_links[ind]['text'].lower() or 'island' in current_links[ind]['text'].lower():
                            driver.get(current_links[ind]['href'])
                            get_description(driver)
                except Exception as e:
                    pass
        driver.quit()

if __name__ == '__main__':
    # county_description()
    main()
