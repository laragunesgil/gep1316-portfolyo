# Kullanıcının karşılaştırma yaptığı sektör veya durumu sorar.

sektor = input("Sektör veya karşılaştırma açıklaması: ")

# Sayısal dönüşüm hatalarını yakalamak için giriş işlemlerini başlatır.

try:

    # Kullanıcıdan verilerin ait olduğu yılı tam sayı olarak alır.

    veri_yili = int(input("Veri yılı: "))

    # Kullanıcıdan erkek çalışanların ortalama brüt saatlik ücretini ondalıklı sayı olarak alır.

    erkek_ucreti = float(input("Erkek çalışanların ortalama brüt saatlik ücreti: "))

    # Kullanıcıdan kadın çalışanların ortalama brüt saatlik ücretini ondalıklı sayı olarak alır.

    kadin_ucreti = float(input("Kadın çalışanların ortalama brüt saatlik ücreti: "))

    # Erkek ücreti sıfır olduğunda formülde sıfıra bölme yapılmasını önler.

    if erkek_ucreti == 0:

        # Kullanıcıya hesaplamanın neden yapılamadığını bildirir.

        print("Erkeklerin ortalama ücreti sıfır olamaz.")

    # Ücretlerden biri negatifse anlamlı bir ücret karşılaştırması yapılmasını önler.

    elif erkek_ucreti < 0 or kadin_ucreti < 0:

        # Kullanıcıya ücretlerin negatif olamayacağını bildirir.

        print("Ücretler negatif olamaz.")

    # Ücretler geçerliyse farkı hesaplar ve sonuçları gösterir.

    else:

        # HATA DÜZELTME: Eurostat formülünde payda erkek çalışanların ortalama ücretidir.

        fark_yuzdesi = (erkek_ucreti - kadin_ucreti) / erkek_ucreti * 100

        # Kadınların ortalama ücretinin daha düşük olup olmadığını bool değeriyle belirler.

        kadin_ucreti_dusuk = kadin_ucreti < erkek_ucreti

        # Karşılaştırma açıklamasını ve yılı f-string ile ekrana yazdırır.

        print(f"Karşılaştırma: {sektor} ({veri_yili})")

        # Erkeklerin ortalama ücretini iki ondalık basamakla yazdırır.

        print(f"Erkeklerin ortalama ücreti: {erkek_ucreti:.2f}")

        # Kadınların ortalama ücretini iki ondalık basamakla yazdırır.

        print(f"Kadınların ortalama ücreti: {kadin_ucreti:.2f}")

        # Hesaplanan ücret farkını yüzde işaretiyle yazdırır.

        print(f"Cinsiyete göre brüt saatlik ücret farkı: %{fark_yuzdesi:.2f}")

        # Bool karşılaştırmasının sonucunu ekrana yazdırır.

        print(f"Kadınların ortalama ücreti daha düşük mü? {kadin_ucreti_dusuk}")

# Yıl veya ücret alanına sayı yerine metin girilirse oluşan hatayı yakalar.

except ValueError:

    # Kullanıcıya yıl ve ücret alanlarına geçerli sayılar girmesi gerektiğini bildirir.

    print("Yıl ve ücret alanlarına geçerli bir sayı girin.")
