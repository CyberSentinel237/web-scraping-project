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

                time.sleep(1)

            except Exception as e:
                print(Fore.RED + "Error downloading image:", e)

    else:
        print(Fore.RED + "Failed:", response.status_code)

except Exception as e:
    print(Fore.RED + "Error:", e)