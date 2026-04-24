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
        
