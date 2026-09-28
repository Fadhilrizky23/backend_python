class Kampus : 
# def init ini methd yg otomatis jalan saat bikin Object Baru 
    def __init__(self,name): 
        self.name = name  
        print("Campus Baru telah di tambahkan!")
        

    nama =""
    alamat = ""


class Mahasiswa : 
    nim = 0
    name = "" 

# Method selalu ada paramter Self, self itu referensi ke objek saat ini self.(objectnya)
    def perkenalan(self):
        print(f"Halo nama saya {self.name}") 

    def hello(self,nama):
        print(f"Hello {nama}, nama saya {self.name}")



maba_baru = Mahasiswa()

maba_baru.name = "Miracle"
maba_baru.perkenalan() 


kampus_baru = Kampus("Trisakit")





# kampus1 = Kampus()
# kampus2 = Kampus()  

# print(type(kampus1))
# print(type(kampus2))



# mahasiswa1 = Mahasiswa()
# mahasiswa2 = Mahasiswa() 


# print(type(mahasiswa1))
# print(type(mahasiswa2)) 



# Instace Attribut 
mahasiswa1 = Mahasiswa()
# mahasiswa1.nim = 12345677
# mahasiswa1.name = "Fadhil" 

print(mahasiswa1.nim)
print(mahasiswa1.name) 

mahasiswa2 = Mahasiswa()
mahasiswa2.nim = 98765432
mahasiswa2.nama = "Budi" 

print(mahasiswa2.nama)
print(mahasiswa2.nim)


