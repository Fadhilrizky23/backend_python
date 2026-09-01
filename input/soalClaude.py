# Baca file absensi.txt
# Hitung total masing-masing status: Hadir, Izin, Sakit, Alpa
# Tampilkan hasilnya kayak gini:
#    === REKAP ABSENSI ===
#    Hadir : 4
#    Izin  : 1
#    Sakit : 1
#    Alpa  : 1 
# Kalau file gak ketemu, tangkap error-nya (FileNotFoundError) dan tampilkan pesan yang jelas. 

print("=== REKAP ABSENSI ===")
with open('absensi.txt','r') as file:
    data_karyawan={} 

    for i in file :
        data = i.strip().split(',')
        # in ini kondisi kalau TRUE 
        if data[1] in data_karyawan : 
            data_karyawan[data[1]].append(data[0]) 
        # ini kondisi kalo blm ada, kita tambahin key nya 
        else:
            data_karyawan[data[1]] = [data[0]] 


    for key,nama_list in data_karyawan.items():
        print(f"{key} = {len(nama_list)}")

# print(f"Total Karyawan : {len(data_karyawan["Hadir"])+len(data_karyawan["Izin"])+len(data_karyawan["Sakit"])+len(data_karyawan["Alpa"])}") 

# print(data_karyawan)
# print(data_karyawan.values())
# print(len(data_karyawan.values())) 

total = 0 
for i in data_karyawan.values() : 
    total += len(i)

print(f"Total Karyawan = {total}")



