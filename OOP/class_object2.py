
# CLASS = BLUE PRINT NYA 
# OBJECT = CETAKAN DARI BLUE PRINTNYA


class Mahasiswa :  

    kampus = "UI" # Attribut yang nempel di class nya 

    def __init__(self,nim,name):
        self.nim = nim # attribut yang nempel di Objectnya 
        self.name = name # attribut yang nempel di Objectnya 

    def perkenalan(self):
        return f"Halo, saya {self.name}, NIM {self.nim}, Kuliah di {self.kampus}"


andi = Mahasiswa(123456,"Andi")
budi = Mahasiswa(987654, "Budi")

print("=== CLASS ATTRIBUT ===")
print(andi.kampus)
print(budi.kampus)



print("=== ATTRIBUT METHOD ===")
print(andi.name)
print(andi.nim) 
print(andi.perkenalan())

budi.name = "Budi Baru"
print(budi.name) #hanya Object Andi yang berubah
print(budi.nim) 





