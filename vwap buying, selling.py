import re
from numpy import append, true_divide
from pynse import *
import requests
from pprint import pprint
import time
import ORB

watchlist = ['SBIN','INFY','WIPRO','RELIANCE','ADANIENT',
                'TATAPOWER', 'TECHM', 'TITAN','JSWSTEEL', 'SBILIFE',  'M&M',
                'TATAMOTORS', 'TATASTEEL','TATACHEM',  'TCS', 'WIPRO']
nse=Nse()
count  = 0
buying = []
selling = []

for i in watchlist:
  #  print(i)
    while  count <= 74:
            a = nse.get_quote(i)
            vwap = int(a['vwap'])
            ltp = int(a['lastPrice'])
           # print("ltp is:",ltp)
           # print("vwap is:",vwap)
            if vwap < ltp:
                buying.append(str(i))
                #print("BUY SIGNEL in: "+str(i))
            elif vwap>ltp:
                selling.append(str(i))
               # print("SELL SIGNEL: "+str(i))
            #prnt(i)
            count += 1
            break
    #time.sleep(2)
print("your buying stocks is: ",buying)
print("your selling stocks is: ",selling)    
time.sleep(300)         

