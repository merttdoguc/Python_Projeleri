ogrenciler = {}
ortalamalar = {}
harf_notlari = {}
gecti_kaldi = {}

while True:
    a = input("Öğrencinin adını giriniz, sistemden çıkmak için q'yu tuşlayın: ")
    if a != "q":
        vize = int(input(f"{a} adlı öğrencinin vize notunu giriniz: "))
        final = int(input(f"{a} adlı öğrencinin final notunu giriniz: "))
        ortalama = vize * 0.4 + final * 0.6
        
        if ortalama >= 95:
            harf_notu = "A1"
        elif ortalama >= 90:
            harf_notu = "A2"
        elif ortalama >= 85:
            harf_notu = "A3"
        elif ortalama >= 80:
            harf_notu = "B1"
        elif ortalama >= 75:
            harf_notu = "B2"
        elif ortalama >= 70:
            harf_notu = "B3"
        elif ortalama >= 65:
            harf_notu = "C1"
        elif ortalama >= 60:
            harf_notu = "C2"
        elif ortalama >= 55:
            harf_notu = "C3"
        elif 45 <= ortalama < 55:
            harf_notu = "D"
        else:
            harf_notu = "F"   
            
        if harf_notu in ["C3", "C2", "C1", "B3", "B2", "B1", "A3", "A2", "A1"]:
            durum = "Geçti"
        elif harf_notu == "D":
            durum = "Şartlı Geçti"
        else:
            durum = "Kaldı"
        
        ogrenciler[a] = [vize, final]
        ortalamalar[a] = ortalama
        harf_notlari[a] = harf_notu
        gecti_kaldi[a] = durum
    else:
        break

print("Öğrenciler ve notları: ")
for ogrenci, notlar in ogrenciler.items():
    print(f"{ogrenci}: {notlar}")

print("\nÖğrencilerin ortalamaları ve harf notları:") 
for ogrenci, ortalama in ortalamalar.items(): 
    harf_notu = harf_notlari[ogrenci]
    durum = gecti_kaldi[ogrenci]
    print(f"{ogrenci}: {ortalama:.2f} - {harf_notu} - {durum}")
