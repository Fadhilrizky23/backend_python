class Mahasiswa : 
    nim = 0 
    nama = "" 
    
    def setup(self,nama,nim) : #manual setup
        self.nama = nama 
        self.nim = nim 
        

mhs = Mahasiswa()
# Harus panggil si setupnya 
mhs.setup("Fadhil",123456)
print(mhs.nim)
print(mhs.nama) 



# Class dengan Constrcoter  
print("===== CONS  =====")


class Test : 
    nim = 0 
    nama = ""
    
    def __init__(self,nama,nim):
        self.nama = nama 
        self.nim = nim 


mhs1 = Test("Fadhil",1234)
mhs2 = Test("Rizky",4321) 

print(mhs1.nama)
print(mhs2.nim)



# Constructer dengan validasi 
# kita bisa cek nilai paramter, kalo gak sesuai kita bisa raise value 
print("===== CONS VALIDATE =====")


class BankAccount : 
    
    no = 0 
    saldo = 0 
    
    def __init__(self,no,saldo=0):
        if saldo < 0 : 
            raise ValueError("Saldo tidak bisa di bawah 0") 
    

budi = BankAccount(1234556789,1000)
# andi = BankAccount(123123123,-1000) #Error   


# METHOD __str__() 
# Method ini menentukan bagaimana object ditampilkan sebagai string
# Kalo tanpa ini kalo kita print dia doang jadinya <__main__.(nama classnya ) object at (nomor hex nya) 
print("===== STR =====")


class IotSensor : 
    no = 0 
    node = "" 
    
    def __init__(self,no,node):
        self.no = no 
        self.node = node 
        
    def __str__(self):
        return f"Sensor {self.no} adalah sensor bertipe {self.node}" 
    


sensor1 = IotSensor(1,"RTU")
sensor2 = IotSensor(2,"Nonmag")

print(sensor1) #ini sebenernya manggil fungsi __Str__(), karena kalo gak ada method ini dia hasilnya <__main__.IotSensor object at 0x000002047DC0B6E0>  



# METHOD __eq__() 
# Equality, digunakan untuk membandigkan object dengan object lainnya 
# Saat kita panggil operator ==, maka method ini akan ke panggil  
print("===== EQ =====")

class SensorIot : 
    deveui = 0 
    node = "" 
    
    def __init__(self,deveui,node):
        self.node = node 
        self.deveui = deveui 
    
    def __eq__(self, other):
        # Self = representasi object pertama, other = representasi object ke 2
        return self.deveui == other.deveui
        

rtu1 = SensorIot(1239854527362,"RTU")
rtu2 = SensorIot(1239854527361,"Nonmag")
print(rtu1 == rtu2)

        
        

        



