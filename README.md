Nike Men's Shoes Scraper – Project Overview
This is a Python-based web scraper that collects product names and prices from Nike’s official men’s shoes webpage. 
The purpose of this script is to quickly gather and save Nike shoe listings into a CSV file so that you can analyze prices, track products, or build a dataset for any project.

What the script does
• Opens the men's shoes section on Nike's website
• Automatically scrolls down to load all available products
• Collects each product’s name and price
• Saves the extracted information into a CSV file named nike_mens_shoes.csv
How to use it
1. Download or clone the project files into a folder on your computer.
2. Install the required Python libraries (only needs to be done once). You can open a terminal or command prompt and run:
pip install selenium pandas
3. Download ChromeDriver that matches your installed version of Google Chrome. You can get the correct version from: https://googlechromelabs.github.io/chrome-for-testing/
4. After downloading, extract the chromedriver.exe file and place it in the same folder as the Python script.
5. Open your terminal in that folder and run:
python nike_scraper.py
6. After the script runs, it will create a CSV file named nike_mens_shoes.csv with the product names and prices.
What's inside the folder
• nike_scraper.py – This is the main script that does the scraping
• requirements.txt – A file listing the Python libraries used
• nike_mens_shoes.csv – This file is created after running the script and contains all the scraped data

Notes
• The script runs in headless mode, which means you won’t see the browser window opening.
• Depending on your internet speed, the script may take 20 to 30 seconds to load and scrape all products.
• If Nike updates their website structure, the script may need small updates to continue working properly.

This project was created by Vikramjeet Paul.
You can find me on LinkedIn here: https://www.linkedin.com/in/vikramjpaul
Feel free to use, improve, or share this script. Feedback and suggestions are always welcome.
