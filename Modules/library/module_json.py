import json


file = open('contoh.json','r')
text = file.read()
file.close() 


print(text) 

siswa = json.loads(text) #jadiin dict s
print(type(siswa)) 
print(siswa['nama']) 


sekolah = {
    "nama" : "SMK BISA",
    "alamat" : "Jl. Raya Bogor",
    "jurusan" : [
        "Teknik Informatika",
        "Teknik Mesin"
    ]
}

jadiin_json = json.dumps(sekolah)
print(jadiin_json)
print(type(jadiin_json)) #sudah json, dia kebaca nya string




