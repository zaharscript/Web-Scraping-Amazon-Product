# 🛒 Amazon Product Scraper (BeautifulSoup Version)

This project demonstrates how to scrape product listings from an Amazon search results page using **Python and BeautifulSoup**. It is designed for educational purposes and works with **saved HTML files** (offline), avoiding the need to scrape Amazon directly in real time.

## 📌 Features

- Parses a saved Amazon search result HTML page (e.g., `index.html`)
- Extracts:
  - 🖼️ Product image link
  - 🏷️ Product title
  - ⭐ Rating
  - 💲 Price
- Saves data in:
  - `amazon_bs4_data.json`
  - `amazon_bs4_data.csv`
  - `amazon_bs4_data.xlsx`

## 🧰 Technologies Used

- Python 3
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- `pandas` for Excel export
- `json` and `csv` for structured output

## 🚀 Getting Started

## 1. Clone the repository

```bash
git clone https://github.com/your-username/amazon-bs4-scraper.git
cd amazon-bs4-scraper
```

## 2. Install Dependencies

```bash
pip install beautifulsoup4 pandas openpyxl
```

## 3. Save an Amazon HTML Page

- Go to: https://www.amazon.com/s?k=car+accessories

- Right click > Save as > index.html

## 4. Run the Scraper

```bash
python amazon_scraper_bs4.py

```

📂 Output Files

| File                   | Format | Description                      |
| ---------------------- | ------ | -------------------------------- |
| `amazon_bs4_data.json` | JSON   | Raw structured data              |
| `amazon_bs4_data.csv`  | CSV    | Tabular format, for Excel/Sheets |
| `amazon_bs4_data.xlsx` | Excel  | Excel workbook with product data |

📝 Example Output (JSON)

```json
[
  {
    "link": "https://m.media-amazon.com/images/I/71N6fKh0iPL._AC_UL320_.jpg",
    "title": "SINGARO Car Cup Holder Coaster, Silicone Cup Holder...",
    "rating": "4.6 out of 5 stars",
    "price": "8"
  },
  ...
]
```

⚠️ Disclaimer

This scraper is for **educational/demo purposes only**. Do not use it to scrape Amazon live pages without respecting their robots.txt and Terms of Service.

📌 License

MIT License — free to use and modify.

```yaml
---
Let me know if you want a logo or badge added to the README as well!
```
