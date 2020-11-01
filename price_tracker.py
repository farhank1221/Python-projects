import smtplib
import config
import os
import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.in/Apple-iPhone-11-64GB-White/dp/B07XVMCLP7/ref=mp_s_a_1_1?dchild=1&keywords=iphone&qid=1604043721&sr=8-1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36'}

#This is a function to check the price of the product
def check_price():
    page = requests.get(url,headers=headers)

    soup = BeautifulSoup(page.content,'html.parser')

    #Accessing the title and price of the product
    title = soup.find(id='title').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()

    #Elimating the currency symbol and other non-relevant values
    converted_price = price[2:8]

    #replace the ',' in price to '.' to convert to a float
    new_price = converted_price.replace(',','.')

    #convert the price string to float number
    num_price =float(new_price)

    print(title.strip())
    print(new_price)

    if (num_price > 49.998):
        send_mail()

def send_mail():
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS,config.PASSWORD)

        subject = 'Price fell down!!!'
        body = 'IPhone 11(64 GB) is available at a lower price now. Click here:  https://www.amazon.in/Apple-iPhone-11-64GB-White/dp/B07XVMCLP7/ref=mp_s_a_1_1?dchild=1&keywords=iphone&qid=1604043721&sr=8-1'
        msg = f'Subject:{subject}\n\n{body}'
        server.sendmail(config.EMAIL_ADDRESS,config.EMAIL_ADDRESS,msg)
        print('mail sent')
        server.quit()

check_price()
