import requests
from bs4 import BeautifulSoup

headers = {
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.837 YaBrowser/23.9.4.837 Yowser/2.5 Safari/537.36'
}



def get_url(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)
    
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(response.text)
    
def main():
    get_url(url='https://enter.kg/korpusa_bishkek')
    
    
    
    
    
if __name__=='__main__':
    main()