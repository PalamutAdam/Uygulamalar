# Gelişmiş Hesap Makinesi (0-100.000 arası sayılar)
import math

def hesap_makinesi():
    while True:
        print("\n=== Hesap Makinesi ===")
        print("1. Toplama (+)")
        print("2. Çıkarma (-)")
        print("3. Çarpma (*)")
        print("4. Bölme (/)")
        print("5. Üs Alma (**)")
        print("6. Karekök")
        print("7. Mod Alma (%)")
        print("8. Çıkış")

        secim = input("Bir işlem seçin (1-8): ")

        if secim == "8":
            print("Hesap makinesinden çıkılıyor. Görüşürüz!")
            break

        if secim not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Geçersiz seçim! Lütfen 1-8 arasında bir sayı girin.")
            continue

        try:
            if secim == "6":
                sayi1 = float(input("Karekökü alınacak sayıyı girin (0-100000): "))
                if sayi1 < 0:
                    print("Hata: Negatif sayının karekökü alınamaz!")
                    continue
                if sayi1 > 100000:
                    print("Hata: Sayı 100.000’den büyük olamaz!")
                    continue
                sonuc = math.sqrt(sayi1)
                print(f"Sonuç: √{sayi1} = {sonuc:.2f}")
            else:
                sayi1 = float(input("İlk sayıyı girin (-100000 ile 100000 arası): "))
                if abs(sayi1) > 100000:
                    print("Hata: Sayı -100.000 ile 100.000 arasında olmalı!")
                    continue

                sayi2 = float(input("İkinci sayıyı girin (-100000 ile 100000 arası): "))
                if abs(sayi2) > 100000:
                    print("Hata: Sayı -100.000 ile 100.000 arasında olmalı!")
                    continue

                if secim == "1":
                    sonuc = sayi1 + sayi2
                    if abs(sonuc) > 100000:
                        print("Hata: Sonuç 100.000’den büyük olamaz!")
                    else:
                        print(f"Sonuç: {sayi1} + {sayi2} = {sonuc}")
                elif secim == "2":
                    sonuc = sayi1 - sayi2
                    if abs(sonuc) > 100000:
                        print("Hata: Sonuç 100.000’den büyük olamaz!")
                    else:
                        print(f"Sonuç: {sayi1} - {sayi2} = {sonuc}")
                elif secim == "3":
                    sonuc = sayi1 * sayi2
                    if abs(sonuc) > 100000:
                        print("Hata: Sonuç 100.000’den büyük olamaz!")
                    else:
                        print(f"Sonuç: {sayi1} * {sayi2} = {sonuc}")
                elif secim == "4":
                    if sayi2 == 0:
                        print("Hata: Sıfıra bölme işlemi yapılamaz!")
                    else:
                        sonuc = sayi1 / sayi2
                        if abs(sonuc) > 100000:
                            print("Hata: Sonuç 100.000’den büyük olamaz!")
                        else:
                            print(f"Sonuç: {sayi1} / {sayi2} = {sonuc:.2f}")
                elif secim == "5":
                    sonuc = sayi1 ** sayi2
                    if abs(sonuc) > 100000:
                        print("Hata: Sonuç 100.000’den büyük olamaz!")
                    else:
                        print(f"Sonuç: {sayi1} ** {sayi2} = {sonuc}")
                elif secim == "7":
                    if sayi2 == 0:
                        print("Hata: Sıfıra mod işlemi yapılamaz!")
                    else:
                        sonuc = sayi1 % sayi2
                        print(f"Sonuç: {sayi1} % {sayi2} = {sonuc}")

        except ValueError:
            print("Hata: Lütfen geçerli bir sayı girin!")

if __name__ == "__main__":
    hesap_makinesi()