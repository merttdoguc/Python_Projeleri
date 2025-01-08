ogrenciler = {}
ortalamalar = {}

while True:
    a = input("Öğrencinin adını giriniz, sistemden çıkmak için q'yu tuşlayın: ")
    if a != "q":
        vize = int(input(f"{a} adlı öğrencinin vize notunu giriniz: "))
        final = int(input(f"{a} adlı öğrencinin final notunu giriniz: "))
        ortalama = vize * 0.4 + final * 0.6
        ogrenciler[a] = [vize, final]
        ortalamalar[a] = ortalama
    else:
        break

print("Öğrenciler ve notları: ")
for ogrenci, notlar in ogrenciler.items():
    print(f"{ogrenci}: {notlar}")

print("\nÖğrencilerin ortalamaları:") 
for ogrenci, ortalama in ortalamalar.items(): 
    print(f"{ogrenci}: {ortalama:.2f}")