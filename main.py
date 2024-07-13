import csv
import requests
from bs4 import BeautifulSoup
import datetime
url = "https://helloomarket.com/index.php?route=product/category&path=82"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

res = requests.get(url, headers=headers)

"""Write scraped data to a file"""

today = datetime.date.today()
file_name = f'{today}.csv'
with open(file_name,'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    # writer.writerow(['Product Name','Brand','Product Code','Availability','Price with Tax','Price Without Tax','Image Url'])
    writer.writerow(['Product Name','Price','Tax','Rating','Image Url','Product Url'])
    """End of write a file"""
    
    soup = BeautifulSoup(res.content, 'lxml')
    item_list = soup.find('div', class_="row category-product")
    product_items = item_list.find_all('div', class_="product-layout")
    for item in product_items:
            
        # Extract image URL and product URL
        image_div = item.find('div', class_="image")
        if image_div:
            image_tag = image_div.find('a')
            product_url = image_tag['href']
            image_url = image_tag.find('img', class_="img-responsive")['src']

        # Extract product details
        caption = item.find('div', class_="caption")
        if caption:
            title_tag = caption.find('h4').find('a')
            title = title_tag.get_text(strip=True)
            product_url = title_tag['href']
            price = caption.find('p', class_="price").get_text(strip=True)
            tax = caption.find('span', class_="price-tax").get_text(strip=True)
            rating_span = caption.find('div', class_="rating").find_all('span', class_="fa fa-star fa-stack-1x")
            rating = len(rating_span)
            if product_url:
                res = requests.get(product_url, headers=headers)
                soup = BeautifulSoup(res.content, 'lxml')
                ul_items =soup.find('div',class_='productpage').find('div',class_='col-sm-6 product-right').find('ul',class_='list-unstyled')
                li_items =ul_items.find_all('li')
                for item in li_items:
        
                # if ul_items:
                #     li_items =ul_items.find_all('li')
                    
            
            # print(f"Title: {title}")
            # print(f"Product URL: {product_url}")
            # print(f"Image URL: {image_url}")
            # print(f"Price: {price}")
            # print(f"Tax: {tax}")
            # print(f"Rating: {rating} stars")
            # print("-" * 40)
            
            # writer.writerow([
            #     title,
            #     price,
            #     tax,
            #     rating,
            #     image_url,
            #     product_url
            # ])
            
          