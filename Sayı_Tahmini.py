import random
sys_sayi = random.randrange(1,101)
while True:
    sayi = int(input("1 den 100 e kadar olan bir sayı giriniz:"))
    if sayi < sys_sayi:
        print("Daha da büyük gir")
        continue
    elif sayi > sys_sayi:
        print("Daha da küçük gir")
        continue
    else:
        print("Doğru tahmin")
        break
    