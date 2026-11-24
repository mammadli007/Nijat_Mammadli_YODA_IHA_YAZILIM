
# Kullanıcıdan bir cümle veya paragraf alıyoruz
metin = input("Bir cümle veya paragraf giriniz: ")

# Büyük ve küçük harfleri aynı kabul etmek için metni küçültüyoruz.
# Böylece Python ve PYTHON aynı kelime olarak sayılır.
metin_kucuk = metin.lower()

# Metni kelimelere ayırıyoruz.
kelimeler = metin_kucuk.split()

# Toplam karakter ve kelime sayılarını hesaplıyoruz.
karakter_sayisi = len(metin)
kelime_sayisi = len(kelimeler)

# En uzun kelimenin uzunluğunu bulmak için başlangıçta 0 veriyoruz.
en_uzun = 0

# Kelimelerin kaç defa tekrar ettiğini tutmak için sözlük oluşturuyoruz.
kelime_tekrar = {}

# Listedeki her kelimeyi tek tek kontrol ediyoruz.
for kelime in kelimeler:

    # Kelimenin uzunluğu şu ana kadarki en uzun değerden büyükse güncelliyoruz.
    if len(kelime) > en_uzun:
        en_uzun = len(kelime)

    # Kelime daha önce sözlükte varsa tekrar sayısını bir artırıyoruz.
    if kelime in kelime_tekrar:
        kelime_tekrar[kelime] += 1

    # İlk defa karşılaşıyorsak tekrar sayısını 1 yapıyoruz.
    else:
        kelime_tekrar[kelime] = 1

# Hesaplanan sonuçları ekrana yazdırıyoruz.
print("\n--- KELİME SAYACI SONUÇLARI ---")
print("Toplam kelime sayısı:", kelime_sayisi)
print("Toplam karakter sayısı:", karakter_sayisi)
print("En uzun kelimenin uzunluğu:", en_uzun)

# Her kelimenin kaç defa tekrarlandığını gösteriyoruz.
print("\nKelime tekrar sayıları:")

for kelime in kelime_tekrar:
    print(kelime, ":", kelime_tekrar[kelime])
