# FUNCTION 

def fungsi_test(nama):
    print(f"Hello {nama}") 


fungsi_test("Fadhil")
fungsi_test("Sekar")  

def volume(panjang, lebar, tinggi):
    total_volume = panjang*lebar*tinggi 

    return (f"{total_volume} m^3")  


print(volume(1,2,3)) 

# Default Parameter 

def luas_lingkaran (r,pi=3.14):
    return pi*r*r 

print(luas_lingkaran(10)) 

# Keyword Argument 
# Biasanya kita masukin nilai parameter nya urutan 

def perkenalan (nama,umur,kota):
    print(f"Nama : {nama}")
    print(f"Umur : {umur}")
    print(f"Kota : {kota}") 


# Positional Argument 
perkenalan("Fadhil",25,"Jakarta")

# Keyword argument ( urutan bebas) 
perkenalan(kota="Bandung", nama="Reizik",umur=21) 


# Lokal variabel 

def test():
    x = 5 
    print(f"nilai x adalah {x}")

test()
# print(x) # ini Error karena X itu variabel lokal di dlm def test 


# GLOBAL VARIABEL 
nama_global = "Lea" 
nama_diubah = "Leo"


def ubah_nama():
    nama_global = "Lea 2"
    return nama_global 




print(ubah_nama())
print(nama_global)   #gak berubah jadi lea2  


def ubah_nama2():
    global nama_diubah
    nama_diubah = "Zephyr"
    return nama_diubah 

print(ubah_nama2())
print(nama_diubah) 


# Parameter Dinamis 
# kasih * untuk kasih tau dia list 
# kasih ** untuk kasih tau dia dictionary 

def cetak_list(*list_item):
    for item in list_item : 
        if item % 2 == 0 : 
            print(item) 

cetak_list(1,2,3,4,5,6,7,8,9,10) 


def cetak_dict(**diksi):
    for key,value in diksi.items():
        print(f"key = {key} - Value = {value}")

cetak_dict(nama="Fadhil", kota = "Bandung", umur = 26) 


# SOAL CLAUDE 
print("==== SOAL CLAUDE =====")

# Bikin Function Cek transaksi 
# Menerima 2 parameter: saldo dan nominal_tarik
# Kalau nominal_tarik lebih besar dari saldo → return string "Saldo tidak cukup"
# Kalau nominal_tarik lebih kecil atau sama dengan saldo → return sisa saldo setelah ditarik (saldo - nominal_tarik)
# Ada default value untuk parameter nominal_tarik = 50000 (jadi kalau function dipanggil tanpa nominal_tarik, otomatis narik 50000)


def cek_transaksi(saldo,nominal_tarik = 50000):
    if nominal_tarik > saldo : 
        return("Saldo tidak cukup") 
    else : 
        return saldo - nominal_tarik


print(cek_transaksi(100000,30000)) #70.000
print(cek_transaksi(20000,30000)) #saldo tidak cukup
print(cek_transaksi(100000)) #50.000 


# SOAL CLAUDE 
print("==== SOAL CLAUDE =====")
stock_barang = {
    "kaos": 10,
    "celana": 25,
    "jaket": 3,
    "topi": 50,
    "sepatu": 0
}

def cek_stock(nama_barang):
        if nama_barang.lower() in stock_barang : 
            return stock_barang[nama_barang.lower()]
        else : 
            return "Barang belum Tersedia" 

input_barang = input("Masukan Nama Barang : ") 
print(f"Stock = {cek_stock(input_barang)} Unit ") 


# SOAL CLAUDE 
print("==== SOAL CLAUDE =====") 
# Sistem Belanja Multi-Item 
# Bikin function checkout yang:

# Menerima 1 parameter: keranjang — berupa dictionary, isinya nama barang & jumlah yang mau dibeli. Contoh: 
# keranjang = {
#     "kaos": 2,
#     "jaket": 5,
#     "sandal": 1
# } 

def checkout(item): 
    # Return itu langsung selesain Loop makanya itu beda sama Print 
    hasil = {"berhasil" : {} , "gagal" : {}}
    for key,value in item.items():
        if key in stock_barang : 
            hasil["berhasil"][key] = value
            if stock_barang[key] > hasil["berhasil"][key] : 
                stock_barang[key] = stock_barang[key] - hasil["berhasil"][key]
                print(f"{key} - barang ada, Stock sisa = {stock_barang[key]}")
            else : 
                print(f"{key} - stock tidak cukup")
        else : 
            hasil["gagal"][key] = value
            print(f"{key} - barang tidak ditemukan")

keranjang = {
    "kaos": 9,
    "jaket": 1,
    "sepatu": 1,
    "celana" : 10
}

checkout(keranjang)








