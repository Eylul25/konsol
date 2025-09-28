
print("╔═════════════════════╗")
print("║        MENU         ║")
print("║═════════════════════║")
print("║  1-Not Hesaplama    ║")
print("║  2-Birim Dönüştürücü║")
print("║  3Sayı Tahmin Oyunu ║")
print("║  4-Hesap Makinesi   ║")
print("║  5-Çıkış            ║")
print("║                     ║")
print("║    Seçimiz nedir?   ║")
print("╚═════════════════════╝")


def not_hesaplama():
    print("not hesaplama")
    ad=input("öğrenci adı:")
    not1= float(input("1.sınav notu:"))
    not2= float(input("2.sınav notu:"))
    ortalama=(not1+not2)/2
    if ortalama>=50:
        print(f"{ad} gecti Ortalama:{ortalama}")
    else:
        print(f"{ad} kaldı Ortalama:{ortalama}")

def birim_donusturucu():
    print("birim dönüştürücü")
    print("cm->m")
    print("m->cm")
    secim=input("seçiminiz")
    if secim=="1":
        cm=float(input("santimetre değeri"))
        print(f"{cm} cm={cm/100} m")
              elif secim=="2":
                  m=float(input("metre değeri:"))
                  print(f"{m} m={cm*100} cm)

import random
def sayi_tahmin():
    print("sayi tahmin oyunu")
    hedef=random.randint(1,10)
    tahmin=0
    while tahmin != hedef:
        tahmin=int(input(1 ile 10 arası bir sayı tahmin et))
        if tahmin < hedef:
            print("daha küçük bir sayı dene")
        elif tahmin > hedef:
            print("daha büyük bir sayı dene")
        print("tebrikler doğru bildin")

def hesap_makinesi():
    while True:
        print("\n -------Hesap Makinesi------")
        print("1.Toplama")
        print("2.Çıkarma")
        print("3.Çarpma")
        print("4.Bölme")
        print("5.Çıkış")
        secim = input("seçiminizi yapınız:")
         
         if secim=="0":
             print("hesap makinesi kapatılıyor")
             break
         if secim in["1","2","3","4"]:
             try:
                 sayi1 = float(input("1. sayıyı giriniz: "))
                sayi2 = float(input("2. sayıyı giriniz: "))
            except ValueError:
                print("Hatalı giriş yaptınız! Sayı giriniz.")
                continue

            if secim == "1":
                print("Sonuç:", sayi1 + sayi2)
            elif secim == "2":
                print("Sonuç:", sayi1 - sayi2)
            elif secim == "3":
                print("Sonuç:", sayi1 * sayi2)
            elif secim == "4":
                if sayi2 == 0:
                    print("Hata: Bir sayı 0'a bölünemez!")
                else:
                    print("Sonuç:", sayi1 / sayi2)
        else:
            print("Geçersiz seçim yaptınız!")

        


def menu():
    while True:
        print("===Ana Menu===")
        print("1: Not Hesaplama")
        print("2: Birim Dönüştürücü")
        print("3: Sayı Tahmin Oyunu")
        print("4: Çıkış")

        secim = input("seciminiz:")
        if secim == "1":
            not_hesaplama()
        elif secim == "2":
            birim_donusturucu()
        elif secim == "3":
            sayi_tahmin()
        elif secim == "4":
            print("program kapatılıyor")
            break:
        else:
            print("geçersiz seçim, tekrar deneyin")
