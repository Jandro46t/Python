import requests
import json
url_sehir = "https://ezanvakti.herokuapp.com/sehirler/2"
r = requests.get(url_sehir)
j = r.json()
sehir_adi = input("Şehir:")
ilce_adi = input("İlçe:")
for sehir in j:
    if sehir_adi == sehir["SehirAdi"]:
        ID = sehir["SehirID"]
        print(ID)
url_ilce = "https://ezanvakti.herokuapp.com/ilceler/{}".format(ID)
re = requests.get(url_ilce)
je = re.json()
for ilce in je:
    if ilce_adi == ilce["IlceAdi"]:
        PD = ilce["IlceID"]
        print(PD)
url_vakit = "https://ezanvakti.herokuapp.com/vakitler/{}".format(PD)
res = requests.get(url_vakit)
jes = res.json()
muzo = jes[0]
for vakit in muzo:
    print(vakit,":",muzo[vakit])
input("Çıkmak için herhangi bir tuşa bas")        