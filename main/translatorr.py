from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import json
import time
import requests
def translate(lang_from, lang_to, text):
    kk = None
    options = Options()


    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    web = webdriver.Firefox(options=options)
    if lang_from == 'kaa':
        web.get('https://www.from-to.uz/')

        web.find_element('xpath', '//*[@id="__layout"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span/i').click()
        web.find_element('xpath', '//*[@id="inputText"]').send_keys(text)
        time.sleep(2)
        web.find_element('xpath', '//*[@id="__layout"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span').click()
        text = web.find_element('xpath', '//*[@id="inputText"]').get_attribute('value')
        lang_from = 'uz'
        kk = True

    elif lang_to == 'kaa':
        kk=False
        lang_to = 'uz'
    web.get(f"https://translate.google.com/?sl={lang_from}&tl={lang_to}&op=translate")
    web.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').send_keys(text)
    time.sleep(1)
    web.find_element('xpath', '/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[3]/div/span/button').click()
    web.find_element('xpath','/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').get_attribute('value')
    time.sleep(1)
    text = web.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[2]/c-wiz[1]/span/span/div/textarea').get_attribute('value')




    if kk == False:
        web.get('https://www.from-to.uz/')
        web.find_element('xpath', '//*[@id="inputText"]').send_keys(text)
        time.sleep(1)
        web.find_element('xpath',
                         '//*[@id="__layout"]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[2]/div/span').click()
        text = web.find_element('xpath', '//*[@id="inputText"]').get_attribute('value')
        time.sleep(1)
    web.quit()
    return text












'''response = requests.request(method='get', url='https://translate.google.com/?hl=ru').text
main_soup = BeautifulSoup(response, 'lxml')
a = main_soup.find_all('div', class_='qSb8Pe')
# Создаем объект BeautifulSoup
data = {}
for html_string in a:
    html_string = str(html_string)
    soup = BeautifulSoup(html_string, 'html.parser')

# Извлекаем значение атрибута data-language-code
    language_code = soup.div['data-language-code']

# Извлекаем текст из внутреннего тега div с классом "Llmcnf"
    language_name = soup.div.find(class_='Llmcnf').text.title()
    data[f'{language_code}'] = str(language_name)
    print("Значение data-language-code:", language_code)
    print("Текстовое значение:", language_name)
with open(r'C:/Users/atikc/PycharmProjects/kktranslator/translator/language_data.json', 'w') as file:
    json.dump(data, file)'''
