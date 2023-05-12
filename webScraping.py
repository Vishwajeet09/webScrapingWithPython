import requests
from bs4 import BeautifulSoup
import pandas



productNames = []
prices = []
description = []


url = "https://www.flipkart.com/search?q=mobile+under+40000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page=1"

response = requests.get(url)

# print(response)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

productName = soup.find_all('div', class_ = "_4rR01T")
for i in productName:
    name = i.text
    productNames.append(name)
# print(productNames)
# print()
# print()
# print()

price = soup.find_all('div', class_ = "_30jeq3 _1_WHN1")
for i in price:
    num = i.text
    prices.append(num)
# print(prices)
# print()
# print()
# print()
        

desc = soup.find_all('ul', class_ = "_1xgFaf")
# print(desc)
for i in desc:
    details= i.text
    description.append(details)
# print(description)

df = pandas.DataFrame({"productName":productName, "prices":price, "description":desc })

# print(df)

df.to_csv("C:/Users/Vishwajeet/Desktop/Web Scraping with python/flipkardWebscraping.csv")








