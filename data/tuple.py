# TUPLE 

point = (5,10)
print(point[0])
print(point[1]) 

# dipakai untuk data yang tidak pernah berubah 
tanggal_lahir = (23,11,1999)

print("Tanggal Lahir : ", tanggal_lahir) 


tup = ("Geeks", "For")
print(tup) 

# Tup using List 
li = [1,2,3,4,5]
print(tuple(li)) 

# Built in Function 
tupe = tuple("String") #akan di iterasi, jadi cuman yang bisa di iterasi yang masuk ke BIF 
print(tupe) 

for e in tanggal_lahir:
    print(e) 


# Many data Type 

tup = (5, "welcome", 7.5, False, [4,5,6], {"key" : "value"}) 
print(tup)


print("=========== Accesing Tuple =========== ")

tup = tuple("Geeks")
print(tup[0])
print(tup[:4])
print(tup[1:5])
print(tup[::-1]) #Reverse

tup = ("geeks", "for", "GEEKS") 

# Tuple Unpacking 
a,b,c = tup 
print(a)
print(b)
print(c)

tupe1 = (1,2,3)
tupe2 = (4,5,6)
print(tupe1+tupe2)


# Del tup 
tp = (1,2,3,4,5)
del tp
# print(tp) #error not defined  


tup = (1,2,3,4,5,6,7,8,9)

c,*d,e = tup 

print(c)
print(d) # asteriks * bikin dia jadi 1 list 
for i in d : 
    print(i)
print(e)  


# SOAL CLAUDE 
print("==== SOAL CLAUDE ====") 
data_karyawan = ("Andi", "Backend Developer", 5000000, "Jakarta") 

print(data_karyawan[0])
print(data_karyawan[2])

# data_karyawan[2] = 60000000
print(data_karyawan[2])

print("==== SOAL CLAUDE ====")  
transaksi = [
    ("Andi", "Beli Baju", 150000),
    ("Budi", "Beli Sepatu", 300000),
    ("Citra", "Beli Tas", 250000),
    ("Andi", "Beli Topi", 50000)
] 

nomimal_transaksi = 0 
# Tuple Unpacking bisa langsung di bongkar semua for nama, jenis, harga in transaksi 

# 1 Loop semua dengan format nama - jenis - harga 
for nama, jenis, harga in transaksi : 
    print(f"{nama} - {jenis} - {harga}")  

# 2 Total Transaksi semua 
for a,b,c in transaksi : 
    nomimal_transaksi += c
print(nomimal_transaksi) 

# 3 Total khusus Andi
total_andi = 0
for a,b,c in transaksi : 
    if a == "Andi" : 
        total_andi += c
print(total_andi)



