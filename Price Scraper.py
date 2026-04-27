import requests
from bs4 import BeautifulSoup
from colorama import init, Fore
import pandas as pd
import re
import time
import random

init(autoreset=True)

url = "http://books.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = []

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN + "Connected!\n")

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_="product_pod")

        for book in books:
            title = book.h3.a.get("title")

            price = book.find("p", class_="price_color").text
            clean_price = re.findall(r"\d+\.\d+", price)

            if clean_price:
                clean_price = clean_price[0]
            else:
                clean_price = "0"

            link = book.h3.a.get("href")
            full_link = "http://books.toscrape.com/" + link

            data.append([title, clean_price, full_link])

            # Delay (human behavior)
            time.sleep(random.uniform(1, 2))

        df = pd.DataFrame(data, columns=["Title", "Price", "Link"])
        df.to_csv("Book List.csv", index=False)

        print(Fore.YELLOW + "\nSaved as Books List.csv successfully!")

    else:
        print(Fore.RED + "Failed:", response.status_code)

except Exception as e:
    print(Fore.RED + "Error:", e)
"""line 1-7 import necessary modules.line 11 url on which we are scraping.line 13 headers which ensures we are not blocked, line 17 the data list will contain the data we scrape. line 19 we handle errors with  try:/except.line 20 goes to the website url and collects data.line 22 if the status_code is 200 then we successfully connected to the website. line 25 converts HTML to readable data by parsing.line 27 where data is stored in html. line 29 to 30 gets book title. line 32 gets the price of the books. line 33 uses regular expression to collect price in an organized manner. line 40 and 41 get product links. line 43 appends or adds the data found in the data list in line 17.line 48 will create columns for data to be stored in an organized manner. line 49 saves everything thing in a clean CSV. line 53 takes action only if we didn't connect to the url. line 56 handles any error like line 19."""
""" use valid url, use good IDE like Pycharm or Pydroid3,make sure you are connected to the internet before you scrape"""