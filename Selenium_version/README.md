# 🛍️ Amazon Product Scraper (Selenium Version)

This project is a web scraper built with **Python**, **Selenium**, and **Pandas** to extract product data from Amazon search result pages. It collects product image links, titles, ratings, and prices, then saves the data into `JSON`, `CSV`, and `Excel` formats.

> ⚠️ This script is intended for educational purposes only. Scraping Amazon's live site may violate their Terms of Service.

---

## 📌 Features

- Scrapes:
  - Product image URLs
  - Product titles
  - Star ratings
  - Whole number prices
- Supports **live scraping with automatic scrolling**
- Outputs data into:
  - `amazon_data.json`
  - `amazon_data.csv`
  - `amazon_data.xlsx`

---

## 🧰 Technologies Used

- Python 3.x
- Selenium WebDriver
- ChromeDriver Manager
- Pandas
- JSON / CSV / Excel output

---

## Setup Instructions

## 🚀 How to Run

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/amazon-product-scraper.git
cd amazon-product-scraper
```

2. **Install dependencies**

   ```bash
   pip install selenium pandas openpyxl webdriver-manager
   ```

3. **Run the scraper**

   ```bash
   python amazon_scraper.py
   ```

   The script will:

- Open Amazon and scroll through results.
- Extract product info.
- Save the data to JSON, CSV, and Excel files.

🖼️ Sample Output

```json
 [
 {
   "link": "https://m.media-amazon.com/images/I/91j3gOyz4dL._AC_UL320_.jpg",
   "title": "SINGARO Car Cup Holder Coaster...",
   "rating": "4.4 out of 5 stars",
   "price": "6"
 },
 ...
]

```

🧪 Testing with Local HTML
To test with a saved page instead of live scraping:

1. Save a search result page from Amazon as index.html.

2. Replace the line:

```python
driver.get("https://www.amazon.com/s?k=car+accessories")

```

with:

```python

driver.get("file://" + os.path.abspath("index.html"))

```

✅ Author

Zahar

Self-taught web developer building real-world data projects.
Feel free to fork or suggest improvements!

📄 License
This project is open-source and licensed under the MIT License.

```yaml
---
Let me know if you want this customized with your GitHub repo link, name, or sample image preview!
```
