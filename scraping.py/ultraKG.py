import requests
from bs4 import BeautifulSoup
from links import *



def choose_category(choise):
    if choise == 1:
        link_link = laptop_2
        print("Вы выбрали Ноутбуки")
    elif choise == 2:
        link_link = monitor_2
        print("Вы выбрали Мониторы")
    elif choise == 3:
        link_link = computer_case_2
        print("Вы выбрали Корпус для ПК")
    elif choise == 4:
        link_link = oper_memory_2
        print("Вы выбрали Оперативную память")
    elif choise == 5:
        link_link = hdd_ccd_memory_2
        print("Вы выбрали Память для ПК")
    elif choise == 6:
        link_link = videocard_2
        print("Вы выбрали Видеокарты")
    elif choise == 7:
        link_link = procecor_2
        print("Вы выбрали Процессоры")
    elif choise == 8:
        link_link = motherboard_2
        print("Вы выбрали Материнскую плату")
    elif choise == 9:
        link_link = power_block_2
        print("Вы выбрали Блоки питания для ПК")
    return link_link










def scrape_data(link_link):
    response = requests.get(link_link)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    foundation = soup.find('div', {"id":"foundation"})
    main = foundation.find('div', {"class":"color_white"})
    limiter = main.find('div', {"class":"limiter"})
    right = limiter.find('div', {"id":"right"})
    catalog = right.find('div', {"id":"catalog"})
    catalog_section = catalog.find('div', {"id":"catalogSection"})
    items = catalog_section.find_all('div', {'class':'item product sku'})
    # print(items)

    for item in items:
        tabloid_nowp = item.find('div',{'class':'tabloid nowp'})
        productTable = tabloid_nowp.find('div',{'class':'productTable'})
        productColText = productTable.find('div',{'class':'productColText'})
        text_in_a = productColText.find('a',{'class':'name'})
        url_in_a ='https://www.ultra.kg' + text_in_a.get('href')
        price = productColText.find('a',{'class':'price'}).text.strip()
        print('Название' + text_in_a.text.strip())
        print('Цена' + price)
        print('Ссылка' + url_in_a)
        print()
        print()
        
        
        
if __name__ == "__main__":
    try:
        choise = int(input('Выберите пункт:'))
        link_link = choose_category(choise)
        scrape_data(link_link)
    except Exception:
        print("Введите число от 1 до 9")