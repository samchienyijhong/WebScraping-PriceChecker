import requests
from bs4 import BeautifulSoup
import smtplib

PRODUCT_URL = 'https://www.amazon.com/example-product'
MY_EMAIL = "__________@gmail.com"
MY_PASSWORD = "________________"

headers = {
    'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
}
response = requests.get(PRODUCT_URL, headers=headers)
html_page = response.text

soup = BeautifulSoup(html_page, 'lxml')
print(soup.prettify())
price = soup.find('span', id='priceblock_ourprice').get_text(0)
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = int

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
        )