import requests
from bs4 import BeautifulSoup
from links import *
import time
import random


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36'
           }



list_name = []
list_price = []
list_url = []

random_delay = random.uniform(1,10)
def scrape_UltraKG(user_choise):
    print('Процесс парсинга сайта UltraKG начался')
    response = requests.get(user_choise, headers=headers)
    content = response.content
    time.sleep(4)
    soup = BeautifulSoup(content, 'html.parser')
    time.sleep(random_delay)
    foundation = soup.find('div', {"id":"foundation"})
    time.sleep(random_delay)
    main = foundation.find('div', {"class":"color_white"})
    time.sleep(random_delay)
    limiter = main.find('div', {"class":"limiter"})
    time.sleep(random_delay)
    right = limiter.find('div', {"id":"right"})
    time.sleep(random_delay)
    catalog = right.find('div', {"id":"catalog"})
    catalog_section = catalog.find('div', {"id":"catalogSection"})
    time.sleep(random_delay)
    items = catalog_section.find_all('div', {'class':'item product sku'})
    # print(items)




    for item in items:
        tabloid_nowp = item.find('div',{'class':'tabloid nowp'})
        productTable = tabloid_nowp.find('div',{'class':'productTable'})
        productColText = productTable.find('div',{'class':'productColText'})
        text_in_a = productColText.find('a',{'class':'name'})
        url_in_a ='https://www.ultra.kg' + text_in_a.get('href')
        price = productColText.find('a',{'class':'price'}).text.strip()
        # print('Название' + text_in_a.text.strip())
        list_name.append(text_in_a.text.strip())
        # print('Цена' + price)
        list_price.append(price.strip('/ шт'))
        # print('Ссылка' + url_in_a)
        list_url.append(url_in_a)
    
        
        
