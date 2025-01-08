print("*HESAP MAKİNESİ*")

islemler = "+, -, *, /"
x = float(input("İlk sayıyı giriniz: "))
print(islemler)
islem = input("Yapmak istediğiniz işlemi seçiniz: ")
y = float(input("İkinci sayıyı giriniz: "))

if islem == "+":
    print(x, islem, y, "=", x+y)

elif islem == "-":
    print(x, islem, y, "=", x-y)

elif islem == "*":
    print(x, islem, y, "=", x*y)

elif islem == "/":
    print(x, islem, y, "=", x/y)    






