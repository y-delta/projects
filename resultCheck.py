import requests 
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen

#Our college website
#url = 'https://results.vtu.ac.in'
#Any other website for testing
url = 'https://www.reddit.com/r/all/new'

response = urlopen(url).read()
currentHash = hashlib.md5(response).hexdigest()

while True:

    response = urlopen(url).read()
    currentHash = hashlib.md5(response).hexdigest()
    #Checks website every 2 minutes, change parameter value to suit your needs
    time.sleep(120)
    response = urlopen(url).read()
    newHash = hashlib.md5(response).hexdigest()

    if newHash == currentHash:
        continue
    
    else:
        print("[!]Website got updated in the last 15 minutes.\n")
        print("Sending an email...\n")
        
        msg = EmailMessage()
        msg.set_content(url)
        msg['From'] = 'SENDER_ADDRESS'
        msg['To'] = 'RECEIVER_ADDRESS'
        msg['Subject'] = 'Website UPDATED!'
        fromaddr = 'SENDER_ADDRESS'
        toaddrs = ['RECEIVER_ADDRESS', 'RECEIVER_ADDRESS_2']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #Enable IMAP and Less Secure Apps access from gmail settings
        server.login('SENDER_ADDRESS', 'SENDER_PASSSWORD')
        server.send_message(msg)
        print("[•]Email sent.\n")
        server.quit()

        #Computing the hash again
        response = urlopen(url).read()
        currentHash = hashlib.md5(response).hexdigest()
        time.sleep(120)
        continue