import requests
from bs4 import BeautifulSoup as bs
import smtplib # For sending the email
import time

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
#url="https://www.amazon.in/Redmi-Prime-Storage-Display-Camera/dp/B08696XM8J/ref=sr_1_4?dchild=1&keywords=redmi+9&qid=1606475137&sr=8-4"
def check_price():
    page=requests.get(url,headers=headers)
    soup=bs(page.content,"html.parser")
    name=soup.find(id="title").get_text().strip() # Fetching the name of the product and removing the white spaces in it


    price=soup.find(id="priceblock_dealprice").get_text()[2:7] # Fetching the data related to price
    price=int(price.replace(',', '')) # Converting it into it

    print(name)
    print(price)

    if(price<9999):
        send_mail() # Calling the send mail function to send the mail if the price is smaller than the threshold value




def send_mail(): # Function which sends the mail
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo() # to identify itself when establishing a connection
    server.starttls() # For encrypting the connection
    server.ehlo()

    server.login('printondemand50@gmail.com','**********') # Logging into the email

    subject='Price fell down!'

    body='Check the link https://www.amazon.in/Redmi-Prime-Storage-Display-Camera/dp/B08696XM8J/ref=sr_1_4?dchild=1&keywords=redmi+9&qid=1606475137&sr=8-4'

    msg=f"Subject: {subject}\n\n{body}" # Composing the email body

    server.sendmail('printondemand50@gmail.com',
    'suneethachittineni@gmail.com',
    msg
    ) # sending the email
    print("MAIL HAS BEEN SENT SUCCESSFULLY")
    server.close() # Closing the server


while(True): # This is for checking the price for a time interval
    check_price()
    time.sleep(20*60*60)
