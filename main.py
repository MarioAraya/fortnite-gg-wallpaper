import imgList
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By

for img in imgList.imgList:
    print(img)
    img_name = img[30:34] + ".jpg"
    img_data = requests.get(img).content
    with open(img_name, 'wb') as handler:
        handler.write(img_data)
