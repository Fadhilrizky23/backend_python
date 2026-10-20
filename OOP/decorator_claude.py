# Instance Method 
# Method biasa, parameter pertama self 

class Meter : 
    def __init__(self,serial,voltage):
        self.serial = serial 
        self.voltage = voltage 

    def is_overvoltage(self):
        return self.voltage > 20_000 


m1 = Meter("KWH-001",26_000) #bikin class kayak biasa 
print(m1.is_overvoltage()) 


# Class Method 
# Dipakai ketika si Methodnya mau akses kelas itu sendiri 
class Meteran : 
    def __init__(self,serial,voltage):
        self.serial = serial 
        self.voltage = voltage 


    @classmethod
    def from_string(cls,data):
        serial,voltage = data.split(",")
        return cls(serial,int(voltage)) 


m2 = Meteran.from_string("KWH-002,30_000") 
print(m2.serial,m2.voltage) 



# Static Method 
# ungsi utilitas/helper yang tidak butuh data objek maupun class, tapi secara logika “milik” class tersebut

class Meter2: 
    @staticmethod
    def kv_to_volt(kv):
        return kv * 1000  



    # Lanjut decorator menit 9:33  


# Property Method untuk kontrol Akses 
class Category : 

    _name = ""

    def set_name(self,name):
        if name == "" : 
            raise ValueError("Name tidak boleh kosong")
        self._name = name 

    def get_name(self):
        return self._name 


category1 = Category()
category1.set_name("Elektronik")
print(category1.get_name())  


# Lanjut 11:49  


# Property Decorator

class Category2 :

    _name = ""

    @property
    def nama(self):
        return self._name

    @nama.setter
    def nama(self,name):
        if name == "":
            raise ValueError("Name tidak boleh kosong")
        self._name = name 

category22 = Category2()
category22.nama = "Meja gaming"
print(category22.nama)
