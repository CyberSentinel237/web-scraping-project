import requests 
from bs4 import BeautifulSoup 
import pandas as pd
import re
from colorama import init,Fore
import time
import random

init(autoreset=True)
url ="http://quotes.toscrape.com"
headers ={"User-Agent":"Mozilla/5.0"}
data=[]

try:
    response= requests.get(url, headers=headers)
    if response.status_code == 200:
        print(Fore.GREEN +"Connected!...\n")
        soup = BeautifulSoup(response.text,"html.parser")
        quotes=soup.find_all("div",class_="quote")
        print(len(quotes))
        for q in quotes:
            text=q.find("span",class_="text").text.strip()
            author=q.find("small",class_="author")
            data.append({"Quotes":text,"Author":author})
         
        df=pd.DataFrame(data)
           
        df.to_csv("Quotes List.csv",index=False)
        time.sleep(random.uniform(1,2))
            
        print(Fore.CYAN +"\nSaved to Quotes List.csv")
            
    else:
        print(Fore.RED +"\nNo Connection...")
except Exception as e:
        print(Fore.RED + "ERROR")
"""line 1 to 7 necessary imports. line 10 to 12 url to scrape, headers prevents us from being blocked, data list stores data we scrape. line 14 exception handler with try:/except statement. line 15 goes and gets data from the url. line 16 is status code is 200 we are connected to the website. line 18 converts HTML to readable text. line 19 where quotes are stored in HTML. line 20 counts number of quotes. line 23 where author's name is stored in html. line 24 adds or appends the data to the data list. line 28 saves as clean CSV. line 29 makes the scraping behavior human like. line 33 is status code is not 200.line 35 handles exception."""
""" use valid url, connect to the internet before scraping, use proper IDE like Pycharm or Pydroid3"""