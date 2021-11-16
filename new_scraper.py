import requests
from bs4 import BeautifulSoup
from database import MySQL

db = MySQL('Prices', '#eW2IV0pK&rH9&R65*IO')
for asin in db.get_product_table():
    link = "https://www.amazon.com/dp/" + asin

    headers = {
        'authority': 'www.amazon.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-US,en;q=0.9',
    }

    response = requests.get(link, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")
    price = soup.find('input', {'id':"attach-base-product-price"})["value"]
    print(asin + " : " + price)

    db.insert_to_prices(asin, price)

    print(db.get_price_date(asin))

    