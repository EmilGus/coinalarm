#!/usr/bin/python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, smtplib, time, sys

def getPrice(coin):
	r = requests.get("http://coinmarketcap.com/currencies/"+coin+"/")
	data = r.text
	soup = BeautifulSoup(data, "html.parser")
	return soup.find(id="quote_price").string[1:-3]

def sendMail():
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, msg)
	server.quit()

# Variables.
fromaddr = 'from@gmail.com'
toaddrs  = 'to@gmail.com'
username = 'username'
password = 'password'
sleep_timer = 3600 # Checks price every hour.

try:
	price_alarm = int(sys.argv[2])
except:
	sys.exit("No argument found for alarm-price in dollars. Command: coinalarm.py <name-of-coin> <alarm-price>\n\
Example: coinalarm.py bitcoin 1000")

try:
	coin = sys.argv[1]
except:
	sys.exit("No argument found for alarm-price in dollars. Command: coinalarm.py <name-of-coin> <alarm-price>\n\
Example: coinalarm.py bitcoin 1000")

while True:
	price = getPrice(coin)
	if int(price) > price_alarm:
		msg = 'The price of '+coin+' is '+price+"$."
		print msg
		sendMail()
		sys.exit("Mail has been sent, shuting down script.")
	else:
		print "The price of "+coin+" is "+price+"$."
	time.sleep(sleep_timer)