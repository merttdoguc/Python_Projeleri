import random
tahmin = random.randint(1, 100)
print("1 ile 100 arasında bir sayı tahmin edin: ")

while True:
    kullanici_tahmin = int(input("Tahmin: "))

    if kullanici_tahmin < tahmin:
        print("Tahmin ettiğiniz sayı küçük, daha büyük bir sayı tahmin ediniz")

    elif kullanici_tahmin > tahmin:
        print("Tahmin ettiğiniz sayı büyük, daha küçük bir sayı tahmin ediniz")
    
    else:
        print("Tahmininiz doğru")
        break