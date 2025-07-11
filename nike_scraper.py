from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

CHROMEDRIVER_PATH = "chromedriver.exe"

options = Options()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=options)

driver.get("https://www.nike.com/w/mens-shoes-nik1zy7ok")
time.sleep(5)

last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

products = driver.find_elements(By.CSS_SELECTOR, 'div.product-card__body')

data = []

for product in products:
    try:
        name = product.find_element(By.CSS_SELECTOR, 'div.product-card__title').text
        price = product.find_element(By.CSS_SELECTOR, 'div.product-price').text
        data.append({'Name': name, 'Price': price})
    except:
        continue

driver.quit()

df = pd.DataFrame(data)
df.to_csv("nike_mens_shoes.csv", index=False)
print("Saved all product info to nike_mens_shoes.csv")