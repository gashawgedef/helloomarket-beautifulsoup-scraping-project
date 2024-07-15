# import csv
# import requests
# from bs4 import BeautifulSoup
# import datetime

# url = "https://helloomarket.com/index.php?route=product/category&path=82"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
# }

# res = requests.get(url, headers=headers)

# # Write scraped data to a file
# today = datetime.date.today()
# file_name = f'{today}.csv'
# with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(['Product Name','Brand','Product Code','Availability' ,'Price', 'Tax', 'Rating', 'Image Url', 'Product Url'])
#     soup = BeautifulSoup(res.content, 'lxml')
#     item_list = soup.find('div', class_="row category-product")
#     product_items = item_list.find_all('div', class_="product-layout")
    
#     for item in product_items:
#         # Extract image URL and product URL
#         image_div = item.find('div', class_="image")
#         if image_div:
#             image_tag = image_div.find('a')
#             product_url = image_tag['href']
#             image_url = image_tag.find('img', class_="img-responsive")['src']

#         # Extract product details
#         caption = item.find('div', class_="caption")
#         if caption:
#             title_tag = caption.find('h4').find('a')
#             title = title_tag.get_text(strip=True)
#             product_url = title_tag['href']
#             price_p = caption.find('p', class_="price")
#             price = price_p.contents[0].strip()
#             tax = price_p.find('span', class_="price-tax").get_text(strip=True).replace('Ex Tax: ', '')
#             rating_span = caption.find('div', class_="rating").find_all('span', class_="fa fa-star fa-stack-1x")
#             rating = len(rating_span)
            
#             # Fetch additional product details from product page
#             if product_url:
#                 product_res = requests.get(product_url, headers=headers)
#                 product_soup = BeautifulSoup(product_res.content, 'lxml')
#                 ul_items = product_soup.find('div', class_='productpage').find('div', class_='col-sm-6 product-right').find('ul', class_='list-unstyled')
#                 li_items = ul_items.find_all('li')
#                 for li in li_items:
#                     desc = li.find('span', class_='desc').get_text(strip=True)
#                     if desc == 'Brand:':
#                         brand = li.find('a').get_text(strip=True)
#                     elif desc == 'Product Code:':
#                         product_code = li.contents[-1].strip()
#                     elif desc == 'Availability:':
#                         availability = li.contents[-1].strip()

#             # Write data to CSV file
#             writer.writerow([
#                 title,
#                 brand,
#                 product_code,
#                 availability,
#                 price,
#                 tax,
#                 rating,
#                 image_url,
#                 product_url
#             ])
import csv
import requests
from bs4 import BeautifulSoup
import datetime

def fetch_page_data(url, headers, writer):
    res = requests.get(url, headers=headers)
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
            price_p = caption.find('p', class_="price")
            price = price_p.contents[0].strip()
            tax = price_p.find('span', class_="price-tax").get_text(strip=True).replace('Ex Tax: ', '')
            rating_span = caption.find('div', class_="rating").find_all('span', class_="fa fa-star fa-stack-1x")
            rating = len(rating_span)
            
            # Initialize brand, product code, and availability
            brand = ''
            product_code = ''
            availability = ''
            
            # Fetch additional product details from product page
            if product_url:
                product_res = requests.get(product_url, headers=headers)
                product_soup = BeautifulSoup(product_res.content, 'lxml')
                ul_items = product_soup.find('div', class_='productpage').find('div', class_='col-sm-6 product-right').find('ul', class_='list-unstyled')
                li_items = ul_items.find_all('li')
                for li in li_items:
                    desc = li.find('span', class_='desc').get_text(strip=True)
                    if desc == 'Brand:':
                        brand = li.find('a').get_text(strip=True)
                    elif desc == 'Product Code:':
                        product_code = li.contents[-1].strip()
                    elif desc == 'Availability:':
                        availability = li.contents[-1].strip()

            # Write data to CSV file
            writer.writerow([
                title,
                brand,
                product_code,
                availability,
                price,
                tax,
                rating,
                image_url,
                product_url
            ])

def get_pagination_urls(base_url, headers):
    res = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(res.content, 'lxml')
    pagination = soup.find('ul', class_='pagination')
    page_links = []
    if pagination:
        for link in pagination.find_all('a'):
            page_url = link.get('href')
            if page_url and page_url not in page_links:
                page_links.append(page_url)
    return page_links

url = "https://helloomarket.com/index.php?route=product/category&path=82"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}

# Write scraped data to a file
today = datetime.date.today()
file_name = f'{today}.csv'
with open(file_name, 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Product Name', 'Brand', 'Product Code', 'Availability', 'Price', 'Tax', 'Rating', 'Image Url', 'Product Url'])
    
    # Fetch and write data from the first page
    fetch_page_data(url, headers, writer)
    
    # Get pagination URLs and iterate through each page
    page_urls = get_pagination_urls(url, headers)
    for page_url in page_urls:
        fetch_page_data(page_url, headers, writer)
