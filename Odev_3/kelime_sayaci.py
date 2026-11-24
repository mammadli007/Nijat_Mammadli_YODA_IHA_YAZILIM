metin = input("Bir metin girin: ")

kelimeler = metin.lower().split()
en_uzun = 0
sayac = {}

# kelime uzunluklarını ve tekrarlarını bul
for k in kelimeler:
    if len(k) > en_uzun:
        en_uzun = len(k)

    if k in sayac:
        sayac[k] += 1
    else:
        sayac[k] = 1

print("\n--- Sonuçlar ---")
print(f"Toplam kelime: {len(kelimeler)}")
print(f"Toplam karakter: {len(metin)}")
print(f"En uzun kelime uzunluğu: {en_uzun}")

print("\nKelime tekrarları:")
for k, adet in sayac.items():
    print(f"{k}: {adet}")
