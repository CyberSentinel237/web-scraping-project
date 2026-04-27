import requests
from bs4 import BeautifulSoup
import time
import os
from colorama import init, Fore

init(autoreset=True)

url = "http://books.toscrape.com"

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Create folder
folder = "images"
os.makedirs(folder, exist_ok=True)

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(Fore.GREEN + "Connected!\n")

        soup = BeautifulSoup(response.text, "html.parser")

        images = soup.find_all("img")

        total = len(images)

        print(Fore.YELLOW + "Found", total, "images\n")

        for i, img in enumerate(images, start=1):
            src = img.get("src")

            if not src:
                continue

            full_url = "http://books.toscrape.com/" + src

            try:
                img_data = requests.get(full_url, headers=headers).content

                filename = os.path.join(folder, str(i) + ".jpg")

                with open(filename, "wb") as f:
                    f.write(img_data)

                percent = (i / total) * 100

                print(
                    Fore.CYAN + "Saved",
                    str(i) + ".jpg",
                    "-",
                    "Progress:",
                    i,
                    "/",
                    total,
                    "(",
                    round(percent, 1),
                    "% )"
                )

                time.sleep(2)

            except Exception as e:
                print(Fore.RED + "Error downloading image:", e)

    else:
        print(Fore.RED + "Failed:", response.status_code)

except Exception as e:
    print(Fore.RED + "Error:", e)
"""line 1-5 necessary imports.line 9 to 11 the url we are scraping from and the headers prevent us from being blocked. line 19 handles error/exception with the try:/except statement. line 22 if status code is 200 we successfully connected. line 25 converts messy HTML to readable text. line 27 finds images in html. line 29 counts the number of images. line 49 to 62 show scraping progress in %.line 64 make the scraping process similar to human behavior using delays. line 66 incase improper download.line 70 if status code is not 200.line 72 part of exception handling."""  
"""Use valid url, connect to the internet before scraping, use proper IDE like Pycharm or Pydroid3""" 