# Description: Scrapes product data from Amazon search results using Selenium and saves to JSON, CSV, and Excel.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import csv
import pandas as pd

# Setup Chrome WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run in background
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

# Visit the live Amazon search page
url = "https://www.amazon.com/s?k=car+accessories"
driver.get(url)
time.sleep(3)

# Scroll down to load more results
scroll_pause = 2
last_height = driver.execute_script("return document.body.scrollHeight")

for _ in range(5):  # Scroll 5 times
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

# Find all product containers
products = driver.find_elements(By.CSS_SELECTOR, "div.s-result-item.s-asin")

results = []

for product in products:
    try:
        img = product.find_element(By.CSS_SELECTOR, "img.s-image").get_attribute("src")
    except NoSuchElementException:
        img = ""

    # Title extraction (robust)
    try:
        h2 = product.find_element(By.TAG_NAME, "h2")
        title = h2.text.strip()
    except NoSuchElementException:
        title = ""

    try:
        rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
    except NoSuchElementException:
        rating = ""

    try:
        price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
    except NoSuchElementException:
        price = ""

    results.append({
        "link": img,
        "title": title,
        "rating": rating,
        "price": price
    })

driver.quit()

print(f"✅ Scraped {len(results)} products.")

# Save to JSON
with open("amazon_data_live.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# Save to CSV
if results:
    keys = results[0].keys()
    with open("amazon_data_live.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

# Save to Excel
df = pd.DataFrame(results)
df.to_excel("amazon_data_live.xlsx", index=False)

print("📦 Data saved to amazon_data_live.json, amazon_data_live.csv, and amazon_data_live.xlsx.")
