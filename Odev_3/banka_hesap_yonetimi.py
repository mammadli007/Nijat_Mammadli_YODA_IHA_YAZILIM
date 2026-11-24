class Hesap:
    def __init__(self, hesap_sahibi, hesap_no, bakiye=0):
        self.hesap_sahibi = hesap_sahibi
        self.hesap_no = hesap_no
        self.bakiye = bakiye

    def para_yatir(self, miktar):
        if miktar > 0:
            self.bakiye += miktar
            print(f"{miktar} TL yatırıldı. Yeni bakiye: {self.bakiye} TL")
        else:
            print("Geçersiz tutar, 0'dan büyük bir değer girin.")

    def para_cek(self, miktar):
        if miktar <= 0:
            print("Çekilecek tutar 0'dan büyük olmalı.")
        elif miktar > self.bakiye:
            print("Yetersiz bakiye.")
        else:
            self.bakiye -= miktar
            print(f"{miktar} TL çekildi. Kalan bakiye: {self.bakiye} TL")

    def bakiye_goster(self):
        print(f"Güncel bakiye: {self.bakiye} TL")


print("=== Hesap Oluşturma ===")
ad = input("Hesap sahibi: ")
no = input("Hesap no: ")
ilk_bakiye = float(input("Başlangıç bakiyesi: "))

hesap = Hesap(ad, no, ilk_bakiye)

# menü döngüsü
while True:
    print("\n1- Para Yatır")
    print("2- Para Çek")
    print("3- Bakiye Sorgula")
    print("4- Hesap Bilgileri")
    print("5- Çıkış")

    secim = input("İşlem seçin: ")

    if secim == "1":
        tutar = float(input("Yatırılacak tutar: "))
        hesap.para_yatir(tutar)

    elif secim == "2":
        tutar = float(input("Çekilecek tutar: "))
        hesap.para_cek(tutar)

    elif secim == "3":
        hesap.bakiye_goster()

    elif secim == "4":
        print(f"\nHesap Sahibi: {hesap.hesap_sahibi}")
        print(f"Hesap No: {hesap.hesap_no}")
        hesap.bakiye_goster()

    elif secim == "5":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Hatalı seçim, tekrar deneyin.")