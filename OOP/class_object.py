# Class adalah blue print atau cetakannya 
# Object adalah instance dari class ( Hasil produksi ), setiap object punya data dan behavior yg sama. tapi nilainya bisa beda 


class Kampus : 
    pass 

class Mahasiswa : 
    pass 

kampus1 = Kampus()
kampus2 = Kampus() 

print(type (kampus1))
print(type (kampus2))


mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.name = "Fadhil"


mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 54321
mahasiswa2.name = "Rizky"

print(mahasiswa1.name)
print(mahasiswa2.name)

print(type(mahasiswa1))
print(type(mahasiswa2))

# Lanjut menit 8:55 Class & Object 
