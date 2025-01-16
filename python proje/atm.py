hesap_bakiyesi = 50000
islemler = {
    "1": "Bakiye sorgulama",
    "2": "Para Yatırma",
    "3": "Para Çekme"
}
print(f"{islemler}, Çıkış yapmak için q'ya basınız")

while True:
    islem = input("Yapmak istediğiniz işlemi seçiniz: ")
    
    if islem == "q":
        print("Çıkış yapılıyor")
        break
    
    if islem == "1":
        print(f"Hesabınızdaki tutar: {hesap_bakiyesi} TL")
    
    elif islem == "2":
        miktar = int(input("Yatırmak istediğiniz miktarı girin: "))
        hesap_bakiyesi += miktar
        print(f"Hesabınızdaki anlık bakiye {hesap_bakiyesi} TL")
    
    elif islem == "3":
        while True:
            miktar = int(input("Çekmek istediğiniz miktarı girin: "))
            if hesap_bakiyesi - miktar < 0:
                print("Hesap bakiyeniz yetersiz, daha küçük bir miktar girin")
            else:  
                hesap_bakiyesi -= miktar
                print(f"Hesabınızdaki anlık bakiye {hesap_bakiyesi} TL")
                break
    else:
        print("Geçersiz işlem")
