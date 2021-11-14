import string, random, re#, lxml
import time
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
from PIL import Image
import os, pytesseract, shutil

ua = UserAgent()

list = ["pass", "username", "email", "password", "code", "pin number"] #Put whatever keywords here

while True:
    try:
        full = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(6))
        header = {'User-Agent':str(ua.random)}
        url = "https://prnt.sc/" + full
        response = requests.get(url, headers=header)
        soup = BeautifulSoup(response.text, "lxml")
        imy = soup.find("img", {"class": "no-click screenshot-image"})
        print(imy["src"])
        filename = imy["src"]
        response = requests.get(filename, headers=header)
        save = full + "." + filename[-3:]
        file = open(save, "wb")
        file.write(response.content)
        file.close()
        keep = False
        owo = pytesseract.image_to_string(Image.open(save))
        for i in list:
            if i in owo:
                keep = True
                break
        if keep is False:
            os.remove(save)
        else:
            pass #shutil.move
    except Exception as fuck:
        print(fuck)

