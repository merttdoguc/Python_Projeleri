# SQLITE VERİTABANIYLA ÇALIŞAN MÜZİK LİSTESİ
import sqlite3
import time

class Sarki:
    def __init__(self, sarki_ismi, sanatci, album, sarki_suresi):
        self.sarki_ismi = sarki_ismi
        self.sanatci = sanatci
        self.album = album
        self.sarki_suresi = sarki_suresi

    def __str__(self):
        return "Şarkı İsmi: {}\nSanatçı: {}\nAlbüm: {}\nŞarkı Süresi: {}\n".format(
            self.sarki_ismi, self.sanatci, self.album, self.sarki_suresi
        )

class MuzikListesi:
    def __init__(self):
        self.baglanti = sqlite3.connect("muzikler.db")
        self.cursor = self.baglanti.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Şarkılar (
                Şarkı_Ismi TEXT,
                Sanatçı TEXT,
                Albüm TEXT,
                Şarkı_Süresi REAL
            )
        """)
        self.baglanti.commit()

    def sarkilari_goster(self):
        self.cursor.execute("SELECT * FROM Şarkılar")
        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Listede Şarkı Yok")
        else:
            for sarki in sarkilar:
                print(sarki)

    def sarki_sorgula(self, sarki_ismi):
        self.cursor.execute("SELECT * FROM Şarkılar WHERE Şarkı_Ismi=?", (sarki_ismi,))
        sarkilar = self.cursor.fetchall()

        if len(sarkilar) == 0:
            print("Aradığınız Şarkı Listede Bulunmuyor")
        else:
            sarki = Sarki(sarkilar[0][0], sarkilar[0][1], sarkilar[0][2], sarkilar[0][3])
            print(sarki)

    def sarki_ekle(self, sarki):
        self.cursor.execute("""
            INSERT INTO Şarkılar (Şarkı_Ismi, Sanatçı, Albüm, Şarkı_Süresi) VALUES (?, ?, ?, ?)
        """, (sarki.sarki_ismi, sarki.sanatci, sarki.album, sarki.sarki_suresi))
        self.baglanti.commit()

    def sarki_sil(self, sarki_ismi):
        self.cursor.execute("DELETE FROM Şarkılar WHERE Şarkı_Ismi=?", (sarki_ismi,))
        self.baglanti.commit()

    def toplam_sure(self):
        self.cursor.execute("SELECT SUM(Şarkı_Süresi) FROM Şarkılar")
        toplam = self.cursor.fetchone()[0]
        if toplam is None:
            toplam = 0
        dakika, saniye = divmod(toplam * 60, 60)
        print("Toplam Şarkı Süresi: {:.0f} dakika {:.0f} saniye".format(dakika, saniye))

print("Müzik Listesine Hoşgeldiniz\nİşlemler:\n1- Şarkıları Göster\n2- Şarkıları Sorgula\n3- Şarkı Ekleme\n4- Şarkı Silme\n5- Şarkıların Toplam Süresini Gösterme\nÇıkmak İçin q'ya Basın")

while True:
    islem = input("Yapmak İstediğiniz İşlemi Seçin: ")
    if islem == "q":
        print("Programdan Çıkılıyor..")
        break

    elif islem == "1":
        muzik_listesi = MuzikListesi()
        muzik_listesi.sarkilari_goster()
    
    elif islem == "2":
        sarki_ismi = input("Sorgulamak İstediğiniz Şarkının İsmi: ")
        print("Şarkı Sorgulanıyor..")
        time.sleep(2)
        muzik_listesi = MuzikListesi()
        muzik_listesi.sarki_sorgula(sarki_ismi)
    
    elif islem == "3":
        sarki_ismi = input("Şarkının İsmi: ")
        sanatci = input("Sanatçı: ")
        album = input("Albüm: ")
        sarki_suresi = float(input("Şarkı Süresi (dakika): "))
        yeni_sarki = Sarki(sarki_ismi, sanatci, album, sarki_suresi)
        print("Şarkı Ekleniyor..")
        time.sleep(2)
        muzik_listesi = MuzikListesi()
        muzik_listesi.sarki_ekle(yeni_sarki)
        print("Şarkı Başarıyla Eklendi")

    elif islem == "4":
        sarki_ismi = input("Silmek İstediğiniz Şarkının İsmi: ")
        print("Şarkı Siliniyor..")
        time.sleep(2)
        muzik_listesi = MuzikListesi()
        muzik_listesi.sarki_sil(sarki_ismi)
        print("Şarkı Başarıyla Silindi")

    elif islem == "5":
        muzik_listesi = MuzikListesi()
        muzik_listesi.toplam_sure()
    
    else:
        print("Lütfen Geçerli Bir İşlem Seçin.")
