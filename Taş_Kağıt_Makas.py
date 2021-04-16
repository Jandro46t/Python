import random
score = 0
sys_score = 0
print('''Yapacağınız hamleyi girin:
1)Taş
2)Kağıt
3Makas''')
while True:
    if score == 3:
        print("Maçı sen kazandın")
        break
    if sys_score == 3:
        print("Maçı system kazandı")
        break
    hamle = int(input("Hamlenizi giriniz:"))
    sys_hamle = random.randrange(1,4)
    if hamle == sys_hamle:
        print("Berabere kimse puan alamadı")
        continue
    elif hamle == 1 and sys_hamle == 2:
        print("Kağıt taşı sarar system 1 puan kazandı")
        sys_score+=1
        continue
    elif hamle == 1 and sys_hamle == 3:
        print("Taş makası ezer sen 1 puan kazandın")
        score+=1
        continue
    elif hamle == 2 and sys_hamle == 1:
        print("Kağıt taşı sarar sen 1 puan kazandın")
        score+=1
        continue
    elif hamle == 2 and sys_hamle == 3:
        print("Makas kağıdı keser system 1 puan kazandı")
        sys_score+=1
        continue
    elif hamle == 3 and sys_hamle == 1:
        print("Taş makası ezer system 1 puan kazandı")
        sys_score+=1
        continue
    elif hamle == 3 and sys_hamle == 2:
        print("Makas kağıdı ezer sen 1 puan kazandın")
        score+=1
        continue
    else:
        print('''Sadece bunlar:
1)Taş
2)Kağıt
3Makas''')

