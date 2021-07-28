# Notifies via email whenever the price of a particular product at amazon falls

import requests
from bs4 import BeautifulSoup
import time
import smtplib as smtp

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

    receiver = '***************'
    subject = "Price fell down!"
    body = URL
    if(converted_price < 15000):
        send_email(receiver, subject, body)

    # print("Email sent!")

def send_email(receiver, subject, body):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    username = '***************'
    password = '********'

    server.login(username, password)
    subject = subject
    body = body
    composed_message = f"Subject: {subject}\n\n {body}"
    server.sendmail(
        from_addr=username,
        to_addrs= receiver,
        msg=composed_message
    )
    print("EMAIL SENT!")
    server.quit()

while(True):
    check_price()
    time.sleep(60)




