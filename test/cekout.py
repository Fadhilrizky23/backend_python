#  Sistem Belanja Multi-Item 
# # Bikin function checkout yang:

# # Menerima 1 parameter: keranjang — berupa dictionary, isinya nama barang & jumlah yang mau dibeli. Contoh: 
# # keranjang = {
# #     "kaos": 2,
# #     "jaket": 5,
# #     "sandal": 1
# # } 

stock_barang = {
    "kaos": 10,
    "celana": 25,
    "jaket": 3,
    "topi": 50,
    "sepatu": 0
}

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