from KITT import send_email
import requests
from bs4 import BeautifulSoup
import time

URL = 'https://www.amazon.in/Beats-Powerbeats-Pro-Wireless-Earphones/dp/B07RB7YHWH/ref=sr_1_1_sspa?crid=11K03X88325K3&dchild=1&keywords=powerbeats+pro&qid=1626865138&sprefix=powerbeats+pr%2Caps%2C270&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVVzNNN1NMRE1RNEYmZW5jcnlwdGVkSWQ9QTAyNjMyMDUzTE1NVVc5NEZWTTZGJmVuY3J5cHRlZEFkSWQ9QTA2NTQyMTExMkdJM1M1OUoyTVpHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'}

def check_price():    
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = int(price[1:3]+price[4:7])

    print(converted_price, title.strip())

    subject = "Price fell down!"
    body = "Check the link https://www.amazon.in/Beats-Powerbeats-Pro-Wireless-Earphones/dp/B07RB7YHWH/ref=sr_1_1_sspa?crid=11K03X88325K3&dchild=1&keywords=powerbeats+pro&qid=1626865138&sprefix=powerbeats+pr%2Caps%2C270&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFVVzNNN1NMRE1RNEYmZW5jcnlwdGVkSWQ9QTAyNjMyMDUzTE1NVVc5NEZWTTZGJmVuY3J5cHRlZEFkSWQ9QTA2NTQyMTExMkdJM1M1OUoyTVpHJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="

    msg = f"Subject: {subject} \n\n {body}"

    if(converted_price < 15000):
        send_email('harshil.patel@sakec.ac.in', msg, body)

    # print("Email sent!")

while(True):
    check_price()
    time.sleep(60)




