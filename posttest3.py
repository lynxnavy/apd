def kasir():
    print("berikut kue yang tersedia di toko sule:")
    print("1 kue keju = 6000")
    print("1 kue coklat = 3500")
    print("perharinya hanya memproduksi 25 kue keju")
    print("perharinya hanya memproduksi 35 kue coklat")
    print("kami memiliki promo sebagai berikut:")
    print("jika membeli 5 kue coklat hingga 20 mendapat diskon 7%")
    print("jika membeli 21 kue coklat hingga 35 mendapat diskon 12%")
    print("jika membeli 4 kue keju hingga 15 mendapat diskon 10%")
    print("jika membeli 16 kue keju hingga 25 mendapat diskon 25%")
    jumlah_kue_coklat = int(input("mau beli berapa kue coklat? "))
    jumlah_kue_keju = int(input("mau beli berapa kue keju? "))
    if(jumlah_kue_coklat >= 1 and jumlah_kue_coklat <= 4):
        harga_kue_coklat = 3500*jumlah_kue_coklat
        print("total pembelian kue coklat: %d" % (jumlah_kue_coklat))
        print("total harga kue coklat: Rp. %d" % (harga_kue_coklat))
    elif(jumlah_kue_coklat >= 5 and jumlah_kue_coklat <= 20):
        harga_kue_coklat = 3500*jumlah_kue_coklat
        diskon_kue_coklat = harga_kue_coklat*7/100
        total_harga_kue_coklat = harga_kue_coklat-diskon_kue_coklat
        print("total pembelian kue coklat: %d" % (jumlah_kue_coklat))
        print("total harga kue coklat: Rp. %d" % (harga_kue_coklat))
        print("potongan diskon kue coklat: Rp. %d" % (diskon_kue_coklat))
        print("total harga setelah potongan diskon kue coklat; Rp. %d" % (total_harga_kue_coklat))
    elif(jumlah_kue_coklat >= 21 and jumlah_kue_coklat <= 35):
        harga_kue_coklat = 3500*jumlah_kue_coklat
        diskon_kue_coklat = harga_kue_coklat*12/100
        total_harga_kue_coklat = harga_kue_coklat-diskon_kue_coklat
        print("total pembelian kue coklat: %d" % (jumlah_kue_coklat))
        print("total harga kue coklat: Rp. %d" % (harga_kue_coklat))
        print("potongan diskon kue coklat: Rp. %d" % (diskon_kue_coklat))
        print("total harga setelah potongan diskon kue coklat; Rp. %d" % (total_harga_kue_coklat))
    elif(jumlah_kue_coklat == 0):
        total_harga_kue_coklat = 0
        print("tidak membeli kue coklat")    
    else:
        print("jumlah kue tidak tersedia")
        kasir()

    if(jumlah_kue_keju >= 1 and jumlah_kue_keju <= 3):
        harga_kue_keju = 6000*jumlah_kue_keju
        print("total pembelian kue keju: %d" % (jumlah_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
    elif(jumlah_kue_keju >= 4 and jumlah_kue_keju <= 15):
        harga_kue_keju = 6000*jumlah_kue_keju
        diskon_kue_keju = harga_kue_keju*10/100
        total_harga_kue_keju = harga_kue_keju-diskon_kue_keju
        print("total pembelian kue keju: %d" % (jumlah_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
        print("potongan diskon kue keju: Rp. %d" % (diskon_kue_keju))
        print("total harga setelah potongan diskon kue keju: Rp. %d" % (total_harga_kue_keju))
    elif(jumlah_kue_keju >= 16 and jumlah_kue_keju <= 25):
        harga_kue_keju = 6000*jumlah_kue_keju
        diskon_kue_keju = harga_kue_keju*25/100
        total_harga_kue_keju = harga_kue_keju-diskon_kue_keju
        print("total pembelian kue keju: %d" % (jumlah_kue_keju))
        print("total harga kue keju: Rp. %d" % (harga_kue_keju))
        print("potongan diskon kue keju: Rp. %d" % (diskon_kue_keju))
        print("total harga setelah potongan diskon kue keju; Rp. %d" % (total_harga_kue_keju))
    elif(jumlah_kue_keju == 0):
        total_harga_kue_keju = 0
        print("tidak membeli kue keju")
    else:
        print("jumlah kue tidak tersedia")
        kasir()
    total_semua_kue = total_harga_kue_coklat+total_harga_kue_keju
    print("jumlah total harga semua kue: Rp. %d" % (total_semua_kue)) 
    bayar = float(input("bayar> "))
    kembalian = bayar-total_semua_kue
    if(bayar >= total_semua_kue):
        print("kembalian: Rp. %d" % (kembalian))

kasir()
