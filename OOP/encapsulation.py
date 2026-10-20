# Encapsultion 

#adalah prinsip OOP yang gabungin data dan method dalam satu unit (class) dan kontrol akses ke data tersebut.  
# kayak storage aman, dan cuman bisa di akses pake cara yang udah di kontrol  


# data protection 
# data validation 
# interface control 
# Maintenance 
# security   

# Access Modifiers 
# nama = public bebas di akses 
# _nama =  protected bisa di akses di class itu sendiri dan turunannya 
# __nama = private cuman bisa di akses di class  


# TANPA ENCAPSULATION 
class Sensor : 
    def __init__(self,name,suhu):
        self.name = name 
        self.suhu = suhu 

s = Sensor("Sensor-001",30)
print(s.suhu)
s.suhu = -9999
print(s.suhu) #data gak jelas, gak ada yg cegah dia  


# DENGAN ENCAPSULATION 

class Sensor2 :
    def __init__(self,name,suhu):
        self.name = name 
        # self.__suhu = suhu 
        self.suhu = suhu 


    @property 
    def suhu(self):
        return self.__suhu
    

    @suhu.setter
    def suhu(self,suhu):
        if not -50 <= suhu <= 100 : 
            raise ValueError("Range suhu tidak valid")
        self.__suhu = suhu 


# a = Sensor2("Sensor-002",999)
# a.suhu = 60 
# print(a.suhu)
# a.suhu = -100 
# print(a.suhu) 



class Meter : 
    def __init__(self,id_meter):
        self.id_meter = id_meter
        self.__kwh = 0.0  

    @property
    def kwh(self):
        return self.__kwh #read only dr luar 


    # untuk set tambah KWH  
    def tambah_kwh(self,jumlah):
        if jumlah < 0 :
            raise ValueError("Pemakaian harus Pos")
        self.__kwh += jumlah 


fadil = Meter("KWH-001")
fadil.tambah_kwh(100)
fadil.tambah_kwh(150)
print(fadil.kwh)
fadil.kwh = 0 
print(fadil.kwh)

