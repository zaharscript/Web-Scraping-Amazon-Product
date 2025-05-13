# Description: This script scrapes product data from an Amazon HTML page and 
# saves it to a JSON file using BeautifulSoup and requests libraries.
from bs4 import BeautifulSoup
import json
import csv
import pandas as pd

# Load the saved HTML file
with open('index.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Find all product containers
product_divs = soup.find_all('div', class_='s-result-item')

results = []

for item in product_divs:
    # Image link
    img_tag = item.find('img', class_='s-image')
    link = img_tag['src'] if img_tag else ""

    # Product title from full h2 > span
    h2_tag = item.find('h2', class_='a-size-base-plus a-spacing-none a-color-base a-text-normal')
    if h2_tag:
        span = h2_tag.find('span')
        title = span.get_text(strip=True) if span else ""
    else:
        title = ""

    # Rating
    rating_tag = item.find('span', class_='a-icon-alt')
    rating = rating_tag.get_text(strip=True) if rating_tag else ""

    # Price
    price_tag = item.find('span', class_='a-price-whole')
    price = price_tag.get_text(strip=True) if price_tag else ""

    results.append({
        "link": link,
        "title": title,
        "rating": rating,
        "price": price
    })

print(f"✅ Scraped {len(results)} products.")

# Save to JSON
with open("amazon_data.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

# Save to CSV
if results:
    keys = results[0].keys()
    with open("amazon_data.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(results)

# Save to Excel
df = pd.DataFrame(results)
df.to_excel("amazon_data.xlsx", index=False)

print("📦 Data saved to amazon_data.json, amazon_data.csv, and amazon_data.xlsx.")
# Note: The above code assumes the HTML structure is similar to the one used in the original script.
# If the structure changes, you may need to adjust the selectors accordingly.