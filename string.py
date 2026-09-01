nama = "Zephyr"
umur = 21 

pesan = "nama saya " + nama + ", Umur " + str(umur)
print(pesan) 


# Panjang String 
nama_depan = "Fadhil "  
print(len(nama_depan)) 

# Indexing 

nama_1 = "Abc"
print(nama_1[0])
print(nama_1[1])
print(nama_1[2])

nama_2 = "Python"
print(nama_2[-1]) #langsung ambil si Karater paling terkahir ( n ) 
print(nama_2[-2])


# String slicing
# 0 : 3 = yang di ambil 0,1,2 
nama_3 = "testing"

print(nama_3[0:3]) #tes 
print(nama_3[:3]) #dari awal sampe index ke 2 = tes
print(nama_2[3:]) # dari index ke 3 sampai habis = hon 
print(nama_2[:]) #semua index = python 


# String Method 
test = "NAMA"
tes_lower = test.lower()
tes_kapital = tes_lower.capitalize()
print(tes_kapital)

title = "nama saya budi"
title_title = title.title() #kapital setiap kata
print(title_title)

kalimat = "Python Programming" 
posisi = kalimat.find("Programming")
print(posisi) 


kata_kata= "missisipi"
cari_huruf = kata_kata.count("i")
print(cari_huruf) 


kalimatt = "i Love Python" 
kalimat_baru = kalimatt.replace("Python","Javascript")
print(kalimat_baru)

# Escape Character 


# String Interpolition 
nama_depann = "Fadhil"
nama_belakang = "Rizky"
kota = "Jaktim" 

# Pakai Fstring 
profile = f"Halo, nama saya {nama_depan}{nama_belakang} saya ber asal dari {kota}" 
print(profile) 

print(f"nama saya {nama_depan}{nama_belakang}") 

harga = 100000
jumlah = 3 

# Eksekusi  Ekspresi di dalam Fstring 
print(f"hari ini saya beli ayam {jumlah} ekor, totalnya {jumlah*harga}")

# Call Method di Fstring
print(f"nama saya {nama_depan}".upper())



