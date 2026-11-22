# Tarih bilgisini kullanabilmek için date sınıfını içe aktarır.

from datetime import date

# Kullanıcıdan adını ister.

ad = input("Adınız nedir? ")

# BENİM DEĞİŞİKLİĞİM (seçtiğim hata kontrolü): Doğum yılını sayıya çevirmeyi dener.

try:

    # BENİM DEĞİŞİKLİĞİM (seçtiğim hata kontrolü): Kullanıcıdan doğum yılını alıp tam sayıya çevirir.

    dogum_yili = int(input("Doğum yılınız nedir? "))

# BENİM DEĞİŞİKLİĞİM (seçtiğim hata kontrolü): Sayı girilmediyse ValueError hatasını yakalar.

except ValueError:

    # BENİM DEĞİŞİKLİĞİM (seçtiğim hata mesajı): Kullanıcıya sayı girmesi gerektiğini söyler.

    print("Lütfen sayı girin.")

# BENİM DEĞİŞİKLİĞİM (seçtiğim hata kontrolü): Dönüşüm başarılıysa aşağıdaki bölümü çalıştırır.

else:

    # Bugünün yılını öğrenir.

    bu_yil = date.today().year

    # BENİM DEĞİŞİKLİĞİM (seçtiğim > koşulu): Doğum yılı bugünün yılından büyükse kontrol eder.

    if dogum_yili > bu_yil:

        # BENİM DEĞİŞİKLİĞİM (seçtiğim A uyarısı): Gelecekteki doğum yılı için uyarı gösterir.

        print("Uyarı: Doğum yılı gelecekte olamaz!")

    # BENİM DEĞİŞİKLİĞİM (seçtiğim > koşulu): Doğum yılı gelecekte değilse yaşı hesaplar.

    else:

        # Yaşı bugünün yılından doğum yılını çıkararak hesaplar.

        yas = bu_yil - dogum_yili

        # Kullanıcıya adı ve hesaplanan yaşıyla birlikte selam verir.

        print(f"Merhaba, {ad}! {yas} yaşındasın.")
