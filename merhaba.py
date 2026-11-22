# Tarih bilgisini kullanabilmek için date sınıfını içe aktarır.
from datetime import date

# Kullanıcıdan adını ister.
ad = input("Adınız nedir? ")

# Kullanıcıdan doğum yılını ister ve gelen metni tam sayıya çevirir.
dogum_yili = int(input("Doğum yılınız nedir? "))

# Bugünün yılını öğrenir.
bu_yil = date.today().year

# Yaşı bugünün yılından doğum yılını çıkararak hesaplar.
yas = bu_yil - dogum_yili

# Kullanıcıya adı ve hesaplanan yaşıyla birlikte selam verir.
print(f"Merhaba, {ad}! {yas} yaşındasın.")
