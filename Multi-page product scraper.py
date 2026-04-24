import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

data = []

headers = {
    "User-Agent": "Mozilla/5.0"
}

for page in range(1, 4):

    url = "http://books.toscrape.com/catalogue/page-" + str(page) + ".html"

    print("Scraping page", page)

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, "html.parser")

            books = soup.find_all("article", class_="product_pod")

            for book in books:
                title = book.h3.a.get("title")

                data.append([title])

        else:
            print("Failed:", response.status_code)

    except Exception as e:
        print("Error:", e)

    time.sleep(2)

df = pd.DataFrame(data, columns=["Title"])
df.to_csv("multi_page.csv", index=False)

print("Done! Saved multi_page.csv")