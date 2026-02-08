import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]

    price_text = book.find("p", class_="price_color").text
    price = float(re.sub(r"[^\d.]", "", price_text))

    availability = book.find("p", class_="instock availability").text.strip()

    data.append({
        "Title": title,
        "Price": price,
        "Availability": availability
    })

df = pd.DataFrame(data)
df.to_csv("books_data.csv", index=False)

print("Web scraping completed successfully")
