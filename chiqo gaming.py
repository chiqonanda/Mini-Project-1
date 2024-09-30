print('\nLogin Akun')
while True:
    akun = input('Masukan Nama: ')
    nim = input("Masukkan NIM: ")
    nim = int(nim)

    if nim >= 2500000000:
        print("NIM tidak valid. Silahkan coba kembali!")
    elif nim >= 2000000000:
        print(" Login anda berhasil!")
        break
    else:
        print("NIM tidak valid. Silahkan coba kembali!")

print("=== Hitung Total Harga ===")

while True:
    harga_barang = float(input("Masukkan harga barang: Rp. "))
    jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))
    total_harga = harga_barang * jumlah_pembelian

    if total_harga > 250000:
        diskon = total_harga * 0.25
        total_setelah_diskon = total_harga - diskon
        print(f"Total harga sebelum diskon: Rp. {total_harga}")
        print(f"Diskon 25%: Rp. {diskon}")
        print(f"Total harga setelah diskon: Rp. {total_setelah_diskon}")
    elif total_harga == 250000:
        print(f"Total harga: Rp. {total_harga}")
        print("Total harga anda tepat Rp. 250.000, maaf ya anda tidak mendapatkan diskon.")
    else:
        print(f"Total harga: Rp. {total_harga}")
        print("Total harga anda di bawah Rp. 250.000, maaf yaa anda tidak mendapatkan diskon.")

#Hasil 
    
    if input("Apakah Anda ingin menghitung total harga lagi? (iya/tidak): ").strip().lower() != "iya":
        print("Terima kasih telah menggunakan program ini.")
        break

print ('------------------------------------------------------------------------------------')
print ('Nama : Chiqo Nanda Rial Pratama                                                     ')
print ('NIM  : 2409116046                                                                   ')
print ('program menghitung total harga barang berdasarkan harga barang dan jumlah pembelian.')
print ('------------------------------------------------------------------------------------')
