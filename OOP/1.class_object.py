# Class adalah blue print atau cetakannya 
# Object adalah instance dari class ( Hasil produksi ), setiap object punya data dan behavior yg sama. tapi nilainya bisa beda 


class Kampus : 
    nama = ""
    alamat = ""

class Mahasiswa : 
    nim = 0
    nama = "" 
    
    # Function di dalam Class  
    # Self adalah parameter khusus yang merujuk ke instance/object yang sedang memanggil method, bisa lebih dari 1 parameter 
    def perkenalan(self,nama):
        print(f"Halo nama saya {self.nama}")
        print(f"Hello {nama}, nama saya {self.nama}")



kampus1 = Kampus()
kampus2 = Kampus() 

print(type (kampus1))
print(type (kampus2))


mahasiswa1 = Mahasiswa()
mahasiswa1.nim = 12345
mahasiswa1.nama = "Fadhil"
mahasiswa1.perkenalan("Zephyr")


