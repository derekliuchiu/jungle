import requests
from bs4 import BeautifulSoup
import subprocess
import mysql.connector

link = "https://www.amazon.com/dp/B0046EC18A"
Asin = "xxxxxxxxxxxx"

# headers = {
#     'authority': 'www.amazon.com',
#     'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
#     'sec-ch-ua-mobile': '?0',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'none',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-user': '?1',
#     'sec-fetch-dest': 'document',
#     'accept-language': 'en-US,en;q=0.9',
# }

# response = requests.get('https://www.amazon.com/dp/B0046EC18A', headers=headers)

# with open("out.html", "w+") as f: 
#     f.write(response.text)


args = [
    "curl",
    link,
    "-H",'authority: www.amazon.com', 
    "-H",'sec-ch-ua: "Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    "-H",'sec-ch-ua-mobile: ?0',
    "-H",'upgrade-insecure-requests: 1',
    "-H",'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
    "-H",'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    "-H",'sec-fetch-site: none',
    "-H",'sec-fetch-mode: navigate',
    "-H",'sec-fetch-user: ?1',
    "-H",'sec-fetch-dest: document',
    "-H",'accept-language: en-US,en;q=0.9',
]


# out = subprocess.run(args, capture_output=True)

# with open("out3.html", "w+") as f:
#      f.write(out.stdout.decode("utf-8"))

with open("out3.html", "rb") as s:
    soup = BeautifulSoup(s.read().decode("utf-8"), "html.parser")

    price = soup.find('input', {'id':"attach-base-product-price"})["value"]

    print(price)
    
    con = mysql.connector.connect(
                    host="127.0.0.1",
                    database = 'prices',
                    port=3306,
                    user="root",
                    password="#eW2IV0pK&rH9&R65*IO"
                    )
    cursor = con.cursor()
    query = "INSERT INTO ProductPrices (Asin, Price, Date) VALUES (%s, %s, UNIX_TIMESTAMP()) ON DUPLICATE KEY UPDATE Price=VALUES(Price)"
    values = (Asin, price)
    cursor.execute(query, values)
    con.commit()

    print(cursor.rowcount, "record inserted")
    
    query = "SELECT Price, FROM_UNIXTIME(Date) FROM ProductPrices WHERE Asin = 'B0046EC18A'"
    cursor.execute(query)
    records = cursor.fetchall()
    for price, date in records:
        print("$"+str(price)+ " : "+str(date))



