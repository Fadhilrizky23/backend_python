# Dictionary 

data = {
    "name" : "Fadhil",
    "age" : 26,
    "country" : "indonesia"
}

print(data) 

# Create dic 

a = {"x" : 1, "y" : 2} 
b = dict(name = "sam", age = 21)
print(a)
print(b) 

# Akses 

print(data["name"]) #fadhil 
print(data.get("age")) #26 

d = {"tgl" : 23, "bulan" : "november"} 
d["tahun"] = 1999 
print(d)
d["bulan"] = "september"
print(d) 

del d["tgl"] 
print(d) 


# POP 
# Apus, tapi return value dari key yg di call 
data_diri = {
    "nama" : "andrw",
    'age' : 124 
}
test1 = data_diri.pop("nama")
print(data_diri) 


test2 = {"a" : 1 ,"b" : 2,"c" : 3} 
print(test2.popitem()) #ambil key value yang terakhir di masukin, dan ngapus  
print(test2) 

test3 = {"a" : 1 ,"b" : 2,"c" : 3} 
test3.clear()
print(test3)


# Loopingg 
data_set = {"a" : 1, "b" : 2, "c" : 3}

for key,value in data_set.items() : #kalo mau value doang pake .values()
    print(f"{key} : {value}") 


# Nested Dictionary 
sma36 = {
    "Student" : {
        "name" : "Andrew",
        "age" : 20 
    }
} 

print(sma36["Student"]["age"])  


# SOAL CLAUDE 
print("==== SOAL CLAUDE =====") 
mahasiswa = {
    "nama": "Rina",
    "jurusan": "Teknik Informatika",
    "ipk": 3.75
} 

# 1 print nama 
print(mahasiswa["nama"]) 

# 2 Key baru 
mahasiswa["semester"] = 5
print(mahasiswa) 

# 3 ubah value IPK 
mahasiswa["ipk"] = 3.8
print(mahasiswa) 

# 4 Print dic
print(mahasiswa) 

# SOAL CLAUDE 
print("==== SOAL CLAUDE =====") 
list_mahasiswa = [
    {"nama": "Rina", "jurusan": "TI", "ipk": 3.75},
    {"nama": "Dodi", "jurusan": "SI", "ipk": 3.20},
    {"nama": "Sinta", "jurusan": "TI", "ipk": 3.90},
    {"nama": "Budi", "jurusan": "SI", "ipk": 2.80}
] 

# 1 Loop semua format nama - jurusan - IPK : nilai IPK 
for mhs in list_mahasiswa : 
    print(f"{mhs["nama"]} - {mhs["jurusan"]} - IPK : {mhs["ipk"]}") 

# 2 rata rata IPK 
average_ipk = 0 
for a in list_mahasiswa : 
    average_ipk += a["ipk"]
print(average_ipk/len(list_mahasiswa)) 

# 3 Print nama siswa yang IPK > 3.5 
for b in list_mahasiswa : 
    if b['ipk'] > 3.5 : 
        print(f"{b["nama"]} - IPK : {b['ipk']}") 

# SOAL CLAUDE 
print("==== SOAL CLAUDE =====") 
perusahaan = {
    "IT": {
        "Andi": {"posisi": "Backend Developer", "gaji": 8000000},
        "Rina": {"posisi": "Frontend Developer", "gaji": 7500000}
    },
    "Marketing": {
        "Budi": {"posisi": "Marketing Lead", "gaji": 9000000},
        "Citra": {"posisi": "Staff Marketing", "gaji": 5000000}
    }
}

# 1 Print posisi & gaji si Andi aja (akses langsung, gak usah loop) 
andi = perusahaan["IT"]["Andi"]
print(f"ANDI : {andi["posisi"]} - {andi["gaji"]}") 

# 2 Loop Format IT - Andi - Backend Developer - Rp8000000
for divisi, karyawan_dict in perusahaan.items() :
    for nama, data_dict in karyawan_dict.items():
        print(f"{divisi} - {nama} - {data_dict["posisi"]} - Rp{data_dict["gaji"]}") 

# 3 Total Gaji semua Karyawan 
total_gaji = 0 
for divisi,data_dict in perusahaan.items(): 
    for nama, data_karyawan in data_dict.items():
        total_gaji += data_karyawan["gaji"] 
print(total_gaji) 