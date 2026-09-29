# Constructor adalah method __init__() 

# Tanpa Constructer 

# class Mahasiswa : 
#     nim = 0 
#     nama = "" 

#     def setup(self,nama,nim) : 
#         self.nama = nama
#         self.nim = nim



# # harus di panggil manual 
# mhs = Mahasiswa()
# mhs.setup("Rizky",1234456) 


# print(mhs.nama)
# print(mhs.nim) 

# ================================================================

# Dengan Constructor 

class Mahasiswa :
    name = ""
    nim = 0 

    def __init__(self,name,nim):
        self.name = name 
        self.nim = nim 


mhs = Mahasiswa("Fadhil",987654)
print(mhs.name)
print(mhs.nim)  



class BankAccount : 
    no = ""
    saldo = 0 

    def __init__(self,no,saldo = 0):
        if saldo < 0 : 
            raise ValueError("Saldo tidak boleh negatif")
        self.no = no 
        self.saldo = saldo


budi = BankAccount("1234567890",1000) #sukses 
# eko = BankAccount("12345678910",-1000) #error 

print(budi.no)
print(budi.saldo)  



class Karyawan : 
    nip = 0
    departemen = ""

    def __init__(self,nip,departemen):
        self.nip = nip 
        self.departemen = departemen 

    def __str__(self):
        return f"karyawan {self.nip} ada di departemen {self.departemen}"  

    def __eq__(self, value):
        return self.nip == value.nip and self.departemen == value.departemen 


sekar1 = Karyawan(1347278,"Sekar")
sekar2 = Karyawan(1347278,"Sekar")

print(sekar1 == sekar2) # True 
print(sekar1)


# Method Object Comparasion 

# __eq__ Equality ini di panggil saat kita pakai operator ==  



