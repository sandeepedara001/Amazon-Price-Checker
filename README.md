# Amazon Price Checker

## Overview
The Amazon Price Checker is a Python script designed to monitor the price of a specific product on Amazon and send an email alert when the price drops below a predefined threshold. This tool utilizes BeautifulSoup for web scraping to extract product details and price information.

## Features
- Monitors product prices on Amazon.
- Sends an email alert when the product price falls below a set value.
- Utilizes web scraping with BeautifulSoup.
- Automated checking at defined intervals.

## Technologies Used
- Python
- BeautifulSoup for web scraping
- smtplib for sending email notifications

## Setup and Usage
1. Ensure you have Python installed on your system.
2. Install the required packages: `pip install requests BeautifulSoup4`
3. Clone this repository or download `pricechecker.py` to your local machine.
4. Update the script with the desired product URL and your email details.
5. Run the script: `python pricechecker.py`

## Configuration
- **Product URL**: Set the `url` variable to the Amazon product page URL you wish to monitor.
- **Email Details**: Configure the sender and receiver email addresses and the sender's email password within the `send_mail` function.
- **Price Threshold**: Modify the `check_price` function to change the price threshold according to your preference.

## Important Notes
- The script uses a placeholder user agent. You may need to update the `headers` dictionary with your current user agent string for successful requests.
- Ensure the email password and sensitive information are securely managed, especially when using personal email accounts for sending alerts.

## Disclaimer
This script is intended for educational purposes. Be mindful of Amazon's terms of service regarding web scraping and automated access to their site.

Enjoy tracking product prices and never miss a deal again!
