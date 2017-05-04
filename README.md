# coinalarm
A python script that fetches the price of any cryptocoin listed on coinmarketcap.com and sends a email via Gmail when the coin has surpassed, or fallen below, a specified price.

usage: ./coinalarm.py [name-of-cryptocoin] [alarm-price-in-dollars] [method (rising/falling)]

examples:

  coinalarm.py bitcoin 1500 rising
  
  coinalarm.py dash 10 falling
