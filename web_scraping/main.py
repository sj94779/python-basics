import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {'title' : [], 'price' : []}

url = "https://www.amazon.in/s?k=iphone&crid=1TKZPIVN2NYYG&sprefix=ipho%2Caps%2C270&ref=nb_sb_noss_2"

r = requests.get(url)

soup = BeautifulSoup(r.text , 'html.parser')
# print(soup.prettify())

spans = soup.select("span.a-size-medium.a-color-base.a-text-normal")
prices = soup.select("span.a-price")
for span in spans:
    print(span.string)
    data["title"].append(span.string)

for price in prices:
    if not("a-text-price" in price.get("class")):
        print(price.find("span").get_text()) 
        data["price"].append(price.find("span").get_text()) 
        if len(data["price"]) == len(data["title"]):
               break 

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv" , index=False)        