from pprint import pprint
import requests
from bs4 import BeautifulSoup

headers = {'User-agent': 'Mozilla/5.0'}
url = 'http://www.za-door.ru/catalog/Zadoor/'

r = requests.get(url, headers=headers)


soup = BeautifulSoup(r.text, 'lxml')

product_links = (tag.get('href') for tag in soup.select('.item'))

def get_product_info(url):
    data = dict()
    r = requests.get(url, headers=headers) 
    soup = BeautifulSoup(r.text, 'lxml')
    
    data['link'] = soup.find(rel='canonical').get('href')
    data['name'] = soup.find('h1').text.strip()
    data['price'] = soup.find('.pr_int').text if soup.find('.pr_int') else None

    return data

products_data = []
for link in product_links:
    print('Parse ' + link)
    products_data.append(get_product_info(link))
    time.sleep(1)

pprint(products_data)