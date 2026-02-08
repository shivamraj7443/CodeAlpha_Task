Below is a **final, internship-ready `README.md`** that you can **copy-paste directly** into your GitHub repository
`CodeAlpha_WebScraping`.

This version is **clean, professional, and aligned with CodeAlpha expectations**.

---

# Web Scraping Project – CodeAlpha Internship

📌 Project Overview

This project is part of the **CodeAlpha Data Analytics Internship (Task 1 – Web Scraping)**.
The objective is to extract structured data from a public website using Python, clean the data, and store it in a CSV file for further analysis.

---

## 🌐 Website Scraped

* **Website:** Books To Scrape
* **URL:** [https://books.toscrape.com](https://books.toscrape.com)
* This is a public website designed for practicing web scraping.

---

## 📊 Data Extracted

The following information was scraped for each book:

* **Title** – Name of the book
* **Price** – Book price (cleaned and converted to numeric format)
* **Availability** – Stock status

The final dataset is stored in **CSV format**.

---

## 🛠️ Tools & Technologies Used

* **Python 3**
* **Requests** – for sending HTTP requests
* **BeautifulSoup (bs4)** – for parsing HTML
* **Pandas** – for data manipulation and CSV export
* **Regular Expressions (re)** – for data cleaning

---

## 🧹 Data Cleaning Performed

* Removed unwanted and corrupted characters from the price column
* Converted price values from text to **float (numeric)** format
* Ensured the dataset is **analysis-ready** and Excel-compatible

---

## 📁 Project Structure

```
CodeAlpha_WebScraping/
│
├── web_scraping.py
├── books_data.csv
└── README.md
```

---

## ▶️ How to Run the Project

1. Install required libraries:

   ```bash
   pip install requests beautifulsoup4 pandas
   ```

2. Run the Python script:

   ```bash
   python web_scraping.py
   ```

3. Output file:

   * `books_data.csv` will be created in the project folder.

---

## ✅ Output

A clean CSV file containing book details, ready for further analysis such as:

* Exploratory Data Analysis (EDA)
* Data Visualization
* Price comparison

---

## 📌 Internship Requirement

This project fulfills **Task 1 (Web Scraping)** of the CodeAlpha Data Analytics Internship.

---

## 👤 Author

**Yashwant Kumar**
(Data Analytics Intern – CodeAlpha)

---
