import requests
import json
url = "https://api.genelpara.com/embed/para-birimleri.json"
r = requests.get(url)
j = r.json()
para_birimi = input("Para biriminiz(USD,EUR,GBP,BTC,ETH,XRP,BCH,LTC,GA,GAG):")
for pasa in j:
    if para_birimi == pasa:
        print(pasa,":",j[pasa])
    


    
    