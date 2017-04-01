import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
domain = 'http://www.za-door.ru'
from django.apps import apps

products = []

def getLinks (pageUel):
    global pages
    html = urlopen

def get_page(url):
    headers = {'User-agent': 'Mozila/5.0'}
    url = url
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')

    return soup

def parse_catalog(category_url, category_name):
    print("Категория {}".format(category_name))
    category_page = get_page('{0}'.format(domain, category_url))
    pages = category_page.select('.pagination a')

    for page in pages:
        page_url = '{0}{1}{2}'.format(domain,category_url,page['href'])
        page = get_page(page_url)
        product_cards = page.select('.item')
        for product in product_cards:
            link = product.select('a.name')[0] 
            parse_product(link['href'], link['title'], link['data'], category_name)
def main():
    main_page = get_page('{0}/catalog/Zadoor/'.format(domain))
    aww = main_page.select('.left_column ul li')

    for li in aww:
        if li.select('a')[0].text == "Двери ZADOOR":
            links = li.select('ul li a')
            for link in links:
                parse_catalog(link['href'], link.text)

def parse_product(product_url, product_name, product_id, category_name):    
    pr_p = get_page('{0}{1}'.format(domain, product_url))
    main_price = 0
    try:
        main_price = pr_p.select('.item_wrap .price .pr_int')[0].contents
    except Exception as ex:
        main_price = pr_p.select('.item_wrap .item_add_basket .price_detail_basket .total_alu_price')[0].contents
    descriptions = pr_p.select('.item_wrap [itemprop="description"] p')
    color_product = pr_p.select('.item_wrap .item_left .var_table .col2 .dash_link')
    color_arr = []
    for color in color_product: color_arr.append(color.contents)
    desc_arr = []
    for desc in descriptions:
        try:
            item = []
            item.append((desc.contents[0]).replace(": ",""))
            item.append(desc.contents[1].contents)
            desc_arr.append(item)
        except Exception as ex:
            print("Чет какая то проблема с выводос свойств, сорян ", ex)
    print("Продукт {0} {1} {2} {3}".format(product_name, main_price, color_arr, desc_arr))
    product_data = {
        "product_id": product_id,
        "category": category_name,
        "name": product_name,
        "price": main_price,
        "colors": color_arr,
        "options": desc_arr
    }
    products.append(product_data)

def do_it():
    main()
    return products
  

# if __name__ == '__main__':
# 	main()
 