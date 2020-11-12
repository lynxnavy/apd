import os
import time

costumer = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print("Muhammad Fajrianur_2009106040")
    print("---Aplikasi Penghitung Biaya Ojek Online---")
    print("1. Biodata Costumer")
    print("2. Hitung Biaya")
    print("0. Keluar")
    pilih_menu = str(input("Pilih menu> "))

    if(pilih_menu == "1"):
        biodata_customer()
    elif (pilih_menu == "2"):
        biaya_costumer()
    elif (pilih_menu == "0"):
        close()
    else:
        print("Kamu memilih menu yang salah!")
        back_to_menu()
        
def biodata_customer():
    clear_screen()
    print("---Biodata Costumer--")
    nama = str(input("Masukkan Nama Anda: "))
    costumer.insert(0,nama)
    hp = int(input("Masukkan Nomor HP Anda: "))
    costumer.insert(1,hp)
    email = str(input("Masukkan Email Anda: "))
    costumer.insert(2,email)
    tl = str(input("Masukkan Tanggal Lahir Anda: "))
    costumer.insert(3,tl)
    gender = str(input("Masukkan Jenis Kelamin Anda: "))
    costumer.insert(4,gender)
    alamat = str(input("Masukkan Alamat Anda: "))
    costumer.insert(5,alamat)
    clear_screen()
    print("---Biodata Costumer--")
    print("Nama: %s" % (costumer[0]))
    print("Nomor HP: %s" % (costumer[1]))
    print("Email: %s" % (costumer[2]))
    print("Tanggal Lahir: %s" % (costumer[3]))
    print("Jenis Kelamin: %s" % (costumer[4]))
    print("Alamat: %s" % (costumer[5]))
    back_to_menu()

def biaya_costumer():
    clear_screen()
    print("---Biaya Costumer--")
    dari = str(input("Masukkan Lokasi Anda: "))
    costumer.insert(6,dari)
    tujuan = str(input("Masukkan Tujuan Anda: "))
    costumer.insert(7,tujuan)
    jarak = float(input("Masukkan Jarak Tempuh: "))
    costumer.insert(8,jarak)
    jenis = str(input("Masukkan Jenis Kendaraan (2/4): "))
    costumer.insert(9,jenis)
    clear_screen()
    print("---Biaya Costumer--")
    print("Lokasi Awal: %s" % (costumer[6]))
    print("Tujuan Akhir: %s" % (costumer[7]))
    print("Jarak Tempuh: %0.1f km" % (costumer[8]))
    print("Jenis Kendaraan: %s" % (costumer[9]))
    if(costumer[9] == "2"):
        total = 4000*costumer[8]
        costumer.insert(10,total)
        print("Total: %d" % (total))
    elif(costumer[9] == "4"):
        total = 6000*costumer[8]
        costumer.insert(10,total)
        print("Total: %d" % (total))
    bayar = float(input("Bayar> "))
    if(bayar >= costumer[10]):
        print("Kembalian: Rp. %d" % (bayar-costumer[10]))
        print("Keterangan: Lunas")
        print("--Semoga Selamat Sampai Tujuan--")
        back_to_menu()
    else:
        print("Uang Anda Tidak Cukup!")
        time.sleep(2)
        biaya_costumer()

def close():
    clear_screen()
    print("---Terima kasih telah menggunakan Aplikasi Penghitung Biaya Ojek Online--")
    time.sleep(3)
    exit()

def back_to_menu():
    print("\n")
    input("Tekan Enter untuk kembali...")
    show_menu()
    
if __name__ == "__main__":
    while True:
        show_menu()
