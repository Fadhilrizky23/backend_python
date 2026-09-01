# SET 

# Tidak ada data duplikat, dan gak urutan jd gak bisa di akses lewat index 

s = {10,50,20} 
print(s)
print(type(s)) 

# SET METHOD 
a = {1,2,3}
b = {3,4,5}  

# ADD 
a.add(6)
print(a) 

# Union
# Gabung tanpa Duplikat 
print(a.union(b))

# Intersection
# Yang muncul di 2 set 
print(a.intersection(b))


# Difference
# ambil semua yang ada di a, TAPI buang yang juga ada di b
print(b.difference(a)) 

# symmetric_difference 
# Bener bener cuman yang muncul di salah satu doang 
print(a.symmetric_difference(b)) #1,2,5,6


# SOAL CLAUDE 
print("==== SOAL CLAUDE ====") 
list_pembeli = ["Andi", "Budi", "Andi", "Citra", "Budi", "Andi"] 

# 1 ubah list_pembeli jadi set (biar dobelnya ilang), simpan di variabel pembeli_unik, terus print
pembeli_uniqe = set(list_pembeli)
print(pembeli_uniqe) 

# 2 Print jumlah pembeli unik-nya (pakai len(), sama kayak di list) 
print(len(pembeli_uniqe))

# 3 Cek apakah "Citra" ada di pembeli_unik pakai in — print hasilnya (True/False) 
print("Citra" in pembeli_uniqe)

# 4 Tambahin nama baru "Dedi" ke pembeli_unik pakai method .add(), terus print lagi 
pembeli_uniqe.add("Dedi")
print(pembeli_uniqe)


# SOAL CLAUDE 
print("==== SOAL CLAUDE ====") 
pembeli_senin = {"Andi", "Budi", "Citra", "Dedi"}
pembeli_selasa = {"Citra", "Dedi", "Eka", "Fira"} 

# 1 cari semua pembeli yang datang (baik senin maupun selasa, tanpa duplikat) 
all_pembeli = pembeli_senin.union(pembeli_selasa)
print(all_pembeli) 


# 2 cari pembeli yang datang di kedua hari (loyal customer). 
pembeli_loyal = pembeli_senin.intersection(pembeli_selasa)
print(pembeli_loyal) 

# 3 cari pembeli yang cuma datang hari Senin doang 
print(pembeli_senin.difference(pembeli_selasa))  

# 4 cari pembeli yang datang cuma salah satu hari aja (gak di kedua-duanya) 
print(pembeli_senin.symmetric_difference(pembeli_selasa)) #Andi budi eka firA 
