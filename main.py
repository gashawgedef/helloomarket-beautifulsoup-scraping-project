# from turtle import title
# import requests
# from bs4 import BeautifulSoup

# url  = "https://helloomarket.com/index.php"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
# }

# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.content,'lxml')
# item_list = soup.find('div',class_="box-product")
# product_items = item_list.find_all('div',class_="product-items")
# for item in product_items:
#     title =item.find('div',class_="product_details")
import requests
from bs4 import BeautifulSoup

url = "https://helloomarket.com/index.php"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'lxml')
item_list = soup.find('div', class_="box-product")
product_items = item_list.find_all('div', class_="product-items")

for item in product_items:
    caption = item.find('div', class_="caption")
    if caption:
        title = caption.find('h4').find('a')
        if title:
            print(title.get_text(strip=True))
