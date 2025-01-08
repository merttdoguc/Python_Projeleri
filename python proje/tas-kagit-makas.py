import random 

def pc_secim():
    n = random.randint(1, 3) 
    if n == 1:
        return "Taş"
    elif n == 2:
        return "Kağıt"
    else:
        return "Makas"
    
kullanici_skoru = 0
pc_skoru = 0

while True:
    kullanici_secimi = input("Taş, Kağıt, Makas: ")
    pc_secimi = pc_secim()
    print("Pc seçimi:", pc_secimi)

    if kullanici_secimi == pc_secimi:
        print("Aynı kararı verdiniz, berabere")
    elif kullanici_secimi == "Taş" and pc_secimi == "Makas":
        print("Kazandınız")
        kullanici_skoru += 1
    elif kullanici_secimi == "Makas" and pc_secimi == "Kağıt":
        print("Kazandınız")
        kullanici_skoru += 1
    elif kullanici_secimi == "Kağıt" and pc_secimi == "Taş":
        print("Kazandınız")
        kullanici_skoru += 1
    else:
        print("Kaybettiniz")
        pc_skoru += 1

    print("Kullanıcı:", kullanici_skoru, "Pc:", pc_skoru)

    if kullanici_skoru == 3 or pc_skoru == 3:
        break

if pc_skoru > kullanici_skoru:
    print("Pc oyunu kazandı")
else:
    print("Kullanıcı oyunu kazandı")        