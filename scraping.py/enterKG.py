import requests
from bs4 import BeautifulSoup
from links import *
import asyncio

def choose_category(choise):
    if choise == 1:
        link_link = laptop
        print("Вы выбрали Ноутбуки")
    elif choise == 2:
        link_link = monitor
        print("Вы выбрали Мониторы")
    elif choise == 3:
        link_link = computer_case
        print("Вы выбрали Корпус для ПК")
    elif choise == 4:
        link_link = oper_memory
        print("Вы выбрали Оперативную память")
    elif choise == 5:
        link_link = hdd_ccd_memory
        print("Вы выбрали Память для ПК")
    elif choise == 6:
        link_link = videocard
        print("Вы выбрали Видеокарты")
    elif choise == 7:
        link_link = procecor
        print("Вы выбрали Процессоры")
    elif choise == 8:
        link_link = motherboard
        print("Вы выбрали Материнскую плату")
    elif choise == 9:
        link_link = power_block
        print("Вы выбрали Блоки питания для ПК")
    return link_link


def scrape_data(link_link):
    response = requests.get(link_link)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    main = soup.find('div', {'id':'main'})
    wrapper = main.find('div', {'id':'wrapper'})
    content_main = wrapper.find('div', {'id':'content'})
    category_description = content_main.find('div',{"class":"category_description"} ).text.strip()
    browse_view = content_main.find('div', {"class":"browse-view"})
    cards = browse_view.find_all('div', {'class': 'row'})
    span = browse_view.find_all('span', {'class':'prouct_name'})
    span = list(span)
    cards = list(cards)
    
    count = 0
    for i, card in zip(span, cards):
        count += 1
        link = i.find('a')
        item_url = link.get("href")
        
        desc = card.find('span', {'class':'prouct_name'}).text.strip()
        price = card.find('label', {'class':'pricelbl'}).text.strip()
        price_som = card.find('span',{'class':"price"}).text.strip()
        
        print()
        print(desc)
        print(price,price_som)
        
        if 'http://www.google.kg/' in item_url or 'https://enter.kg' in item_url:
            print(item_url)
            print()
        else:
            item_url = "https://enter.kg" + item_url
            print(item_url)
        if count == 10:
            break

    
if __name__ == "__main__":
    try:
        choise = int(input('Выберите пункт:'))
        link_link = choose_category(choise)
        scrape_data(link_link)
    except Exception:
        print("Введите число от 1 до 9")