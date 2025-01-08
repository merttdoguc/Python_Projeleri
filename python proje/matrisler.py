# Matris yazımı

import random

n = int(input("Matrisin boyutunu gir: "))
matris = [[random.randint(0, 9)for i in range(n)]for j in range(n)]
for x in matris:
    print(x)

# Matris toplama

import random

n = int(input("Matrisin boyutunu gir (nxn): "))
m1 = [[random.randint(0, 9) for i in range(n)]for j in range(n)]
m2 = [[random.randint(0, 9) for i in range(n)]for j in range(n)]
mt = [[random.randint(0, 9) for i in range(n)]for j in range(n)]

for x in range(n):
    for y in range(n):
        mt[x][y] = m1[x][y] + m2[x][y]

print("Birinci matris: ")
for satir in m1:
    print(satir)

print("İkinci matris: ")
for satir in m2:
    print(satir)

print("Matrislerin toplamı: ")
for satir in mt:
    print(satir)

# Matrisin transpozu

import random

n = int(input("Matrisin boyutunu gir (nxn):"))
matris = [[random.randint(0, 9) for _ in range(n)]for _ in range(n)]
transpoz = [[matris[j][i] for j in range(n)]for i in range(n)]

print("Orijinal matris: ")
for satir in matris:
    print(satir)

print("\nMatrisin transpozu: ")
for satir in transpoz:
    print(satir)

# 0 - 100 arası rastgele sayılardan oluşan 3x3 matriste 50'den büyük kaç tane sayı olduğunu bulan kod

import random

matris = [[random.randint(0, 100)for i in range(3)]for j in range(3)]

for satir in matris:
    print(satir)

buyuk_50 = sum(1 for satir in matris for eleman in satir if eleman > 50)
print(f"Matriste 50'den büyük {buyuk_50} sayı var")

# 1'den 10'a kadar olan sayıları ve karelerini matris olarak oluşturup yazan kod

matris = [[sayi, sayi**2]for sayi in range(1, 11)]
for sayi in matris:
    print(sayi)

# 0 - 100 arası rastgele sayılardan oluşturulan 4x4 matristeki en büyük, en küçük, ve ortalama sayıyı bulan kod

import random

matris = [[random.randint(0, 100)for i in range(4)]for j in range(4)]

for satir in matris:
    print(satir)

matris_elemanlar = [eleman for satir in matris for eleman in satir]
en_buyuk  = max(matris_elemanlar)
en_kucuk = min(matris_elemanlar)
ortalama = sum(matris_elemanlar) / len(matris_elemanlar)
print(f"En büyük değer: {en_buyuk}, En küçük değer: {en_kucuk}, Ortalama değer: {ortalama}")

# Girilen n değerine göre nxn matris oluşturup 1'den n'e kadar sırayla sayıları yerleştiren kod

n = int(input("Matrisin boyutunu gir: "))
matris = [[(i + j*n + 1)for i in range(n)]for j in range(n)]
for satir in matris:
    print(satir)
