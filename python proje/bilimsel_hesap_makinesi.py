import math

def bilimsel_hesap_makinesi():
    
    islemler = {
    "1": "Toplama",
    "2": "Çıkarma",
    "3": "Çarpma",
    "4": "Bölme",
    "5": "Üslü Sayı",
    "6": "Karekök",
    "7": "Sinüs",
    "8": "Cosinus",
    "9": "Tanjant",
    "10": "Logaritma"    
 }

    while True:
        secim = input(f"{islemler}, Bir işlem seçiniz, çıkış yapmak için q'yu tuşlayın: ")
        
        if secim == "q":
            print("Çıkış yapıldı")
            break
        
        if secim in ("1", "2", "3", "4", "5"):
            sayi1 = float(input("1. Sayının değerini gir: "))
            sayi2 = float(input("2. Sayının değerini gir:"))

            if secim == "1":
                print(f"İşlemin sonucu = {sayi1 + sayi2}")
            elif secim == "2":
                print(f"İşlemin sonucu = {sayi1 - sayi2}")
            elif secim == "3":
                print(f"İşlemin sonucu = {sayi1 * sayi2}")
            elif secim == "4":
                print(f"İşlemin sonucu = {sayi1 / sayi2}")
            elif secim == "5":
                print(f"İşlemin sonucu = {sayi1 ** sayi2}")

        elif secim == "6":
            karekok_sayi = float(input("Karekökünü hesaplamak istediğin değeri gir: "))
            print(f"İşlemin sonucu = {math.sqrt(karekok_sayi)}")
        
        elif secim == "7":
            sinus_aci = float(input("Açı değeri gir: "))
            print(f"Açının değeri = {math.sin(math.radians(sinus_aci))}")
        
        elif secim == "8":
            cos_aci = float(input("Açı değeri gir: "))
            print(f"Açının değeri = {math.cos(math.radians(cos_aci))}")
        
        elif secim == "9":
            tan_aci = float(input("Açı değeri gir: "))
            print(f"Açının değeri = {math.tan(math.radians(tan_aci))}")
        
        elif secim == "10":
            log_deger = float(input("Logaritma değerini gir: "))
            print(f"Logaritmanın değeri = {math.log10(log_deger)}")
        
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

bilimsel_hesap_makinesi()
