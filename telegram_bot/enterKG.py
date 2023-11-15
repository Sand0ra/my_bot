import requests
from bs4 import BeautifulSoup
from links import *
import time
import random



lst_names = []
lst_prices = []
lst_urls = []


# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 RuxitSynthetic/1.0 v87973850306561619 t6525593192282166271 ath1fb31b7a altpriv cvcv=2 smf=0 svfu=1'}


random_delay = random.uniform(1,10)
def scrape_enterKG(user_choice):
    print('Процесс парсинга сайта EnterKG начался')
    lst_names.clear()  
    lst_prices.clear()
    lst_urls.clear()
    response = requests.get(user_choice)
    content = response.content
    time.sleep(random_delay)
    soup = BeautifulSoup(content, 'html.parser')
    time.sleep(random_delay)
    main = soup.find('div', {'id':'main'})
    time.sleep(random_delay)
    wrapper = main.find('div', {'id':'wrapper'})
    time.sleep(random_delay)
    content_main = wrapper.find('div', {'id':'content'})
    time.sleep(random_delay)
    browse_view = content_main.find('div', {"class":"browse-view"})
    time.sleep(random_delay)
    cards = browse_view.find_all('div', {'class': 'row'})
    time.sleep(random_delay)
    span = browse_view.find_all('span', {'class':'prouct_name'})
    span = list(span)
    cards = list(cards)
    
    
    
    
    for i, card in zip(span, cards):
        
        link = i.find('a')
        item_url = link.get("href")
        
        desc = card.find('span', {'class':'prouct_name'}).text.strip()
        price = card.find('label', {'class':'pricelbl'}).text.strip()
        price_som = card.find('span',{'class':"price"}).text.strip()
        
        # print()
        # print(desc)
        # print(price,price_som)
        
        if 'http://www.google.kg/' in item_url or 'https://enter.kg' in item_url:
            # print(item_url)
            lst_urls.append(item_url)
            # print()
        else:
            item_url = "https://enter.kg" + item_url
            lst_urls.append(item_url)
            # print(item_url)
        
        lst_names.append(desc)
        lst_prices.append(price_som)
        


    
