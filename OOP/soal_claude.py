#     Buat class Mobil dengan atribut merk dan harga. Implementasikan:

# __init__
# __eq__ (sama kalau merk dan harga sama)
# __lt__, __gt__, __le__, __ge__ (dibandingkan berdasarkan harga)
# python
# m1 = Mobil("Toyota", 300_000_000)
# m2 = Mobil("Honda", 350_000_000)

# print(m1 < m2)    # True
# print(m1 >= m2)   # False
# print(m1 == Mobil("Toyota", 300_000_000))  # True 



class Mobil : 
    merk = ""
    harga = 0 

    def __init__(self,merk,harga): 

        if harga < 0 : 
            raise ValueError("Harga tidak boleh Minus")

        self.merk = merk 
        self.harga = harga  

    def __eq__(self, value):
        return  self.merk == value.merk and self.harga == value.harga 

    def __lt__(self, other):
        return self.harga > other.harga 


    


m1 = Mobil("Toyota", 300_000_000)
m2 = Mobil("Honda", 350_000_000)

print(m1 > m2) #true 
# print(m1 >= m2 ) # perlu pake fungsi lain  
print (m1 == Mobil("Toyota", 300_000_000)) #True