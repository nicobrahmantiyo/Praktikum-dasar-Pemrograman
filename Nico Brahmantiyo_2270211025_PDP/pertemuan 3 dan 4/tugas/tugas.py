# Tugas Akhir Praktikum
"""
Coffe Shop Nico

"""
import datetime
Tanggal = datetime.datetime.now()
print(Tanggal)
print("     ====== Ni coffe ==========       ")
print("     =========================        ")

nama = input("nama pelanggan : ")
alamat = input("alamat : ")
no_telp = input("no_telp : ")


print("     ========================        ")
print("         ======Menu======            ")
print("1. Cappucino         Rp.10000")
print("2. vanilla latte     Rp.12000")
print("3. Chocolate         Rp.11000")
print("4. ice tea           Rp.5000")
print("======Menu======")
h=[]
a=1

menu_pesanan = int(input("Masukan Menu Pesanan (Nomor Menu) : "))
if menu_pesanan == 1:
    harga = 10000
elif menu_pesanan == 2:
    harga = 12000
elif menu_pesanan == 3:
    harga = 11000
elif menu_pesanan == 4:
    harga = 5000
else:
    while True :
        print("====Menu Tidak Tersedia Silahkan Pilih Menu Lainnya====")
        if menu_pesanan == 1 or menu_pesanan == 2 or menu_pesanan ==3 or menu_pesanan ==4:
            if menu_pesanan == 1:
                harga = 10000
            elif menu_pesanan == 2:
                harga = 12000
            elif menu_pesanan == 3:
                harga = 11000
            elif menu_pesanan == 4:
                harga = 5000
                break

jumlah_pembelian = int(input("Masukan Jumlah Pembelian: "))
for i in range(jumlah_pembelian):
    h.append(harga)

while True:
    jawab = input("Apakah ada yang ingin ditambah/dikurangi ? tambah/kurang/tidak  : ")
    if jawab == "tambah" :
        tambah = int(input("Masukan Menu Pesanan (Nomor Menu): "))
        if tambah == 1:
            harga = 10000
        elif tambah == 2:
            harga = 12000
        elif tambah == 3:
            harga = 11000
        elif tambah == 4:
            harga = 5000
        jumlah_tambahan = int(input("Masukan Jumlah Pembelian : "))
        for i in range(jumlah_tambahan):
            h.append(harga)
        c = jumlah_tambahan + jumlah_pembelian
        print("Total Pesanan: ",c)
        bayar = sum(h)
        print("Total Pembayaran : Rp.{}".format(bayar))
        break

    elif jawab == "kurang" :
        kurang = int(input("berapa jumlah yang dikurangkan ? : "))
        for i in range(kurang):
            if kurang <= 1:
                a -= kurang
                del h[a]
                bayar = sum(h)
                break
            else:
                kurang -= a
                del h[kurang]
                if kurang < 0:
                    break
            c = jumlah_pembelian - kurang
            print("Total pemesanan: ",c)
            bayar = sum(h)
            print("TotalPembayaran : Rp.{}".format(bayar))
            break
        
        else:
            bayar = sum(h)
            c = jumlah_pembelian
            print(" Total Pemesanan : ",c)
            print(" Total Pembayaran : Rp. ".format(bayar))
            break
print("   ============    ")
print("Terimakasih atas kunjungan anda")
print("   ============    ")