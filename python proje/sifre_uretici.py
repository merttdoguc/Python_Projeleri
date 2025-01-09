import random

def sifre(uzunluk):
    kullanici_sifre = ""
    for i in range(uzunluk):
        sifre_karakterleri = chr(random.randint(32, 126))
        kullanici_sifre += sifre_karakterleri
    return kullanici_sifre

uzunluk = int(input("Şifre ne kadar uzunlukta olsun: "))
kullanici_sifre = sifre(uzunluk)
print(kullanici_sifre)
