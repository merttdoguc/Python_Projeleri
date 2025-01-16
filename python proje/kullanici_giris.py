sistemkullanicisi = "mert"
sistemsifresi = "1234"

yas = int(input("Yaşınızı giriniz: "))

if yas < 18:
    print("18'den küçük yaştaysanız sisteme giriş yapamazsınız!")
else:
    kullanici = input("Kullanıcı adınızı giriniz: ")
    sifre = input("Şifrenizi giriniz: ")

    if sistemkullanicisi == kullanici and sistemsifresi != sifre:
        print("Şifre yanlış") 
    
    elif sistemkullanicisi != kullanici and sistemsifresi == sifre:
        print("Kullanıcı adı yanlış")
    
    elif sistemkullanicisi != kullanici and sistemsifresi != sifre:
        print("Kullanıcı adı ve şifre yanlış")
    
    else:
        print("Sisteme giriş başarılı")
