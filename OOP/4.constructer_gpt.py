# SOAL 1 

class Employee : 
    name = ""
    position = ""
    salary = 0 
    
    def __init__(self,name,position,salary):
        self.name = name 
        self.position = position
        self.salary = salary 
        
    def __str__(self):
        return f"Employee: {self.name} | {self.position} | {self.salary}"  
    
    # SOAL 2 
    def __eq__(self, other):
        return self.name == other.name and self.position == other.position
    

karyawan1 = Employee("Fadhil","Project Controller",8500000)
karyawan2 = Employee("Budi","Software Engineer",9500000)

print(karyawan1)
print(karyawan2)



emp1 = Employee("Fadhil", "Engineer", 8500000)
emp2 = Employee("Fadhil", "Engineer", 10000000)
emp3 = Employee("Budi", "Engineer", 8500000) 

print(emp1 == emp2) #True 
print(emp1 == emp3) # False


# SOAL 3 
print("===== SOAL 3 =====")

class WaterMeter : 
    
    serial_number = ""
    brand = "" 
    total_volume = 0 
    
    def __init__(self,serial_number,brand,total_volume):
        self.serial_number = serial_number
        self.brand = brand 
        self.total_volume = total_volume
        
    def __str__(self):
        return f"Water Meter: {self.serial_number} | {self.brand} | {self.total_volume} m3" 

    def __eq__(self, other):
        return self.serial_number == other.serial_number 
    
    
meter1 = WaterMeter("WM001", "Itron", 150)
meter2 = WaterMeter("WM001", "Sensus", 200)
meter3 = WaterMeter("WM002", "Itron", 150)


print(meter1)
print(meter1 == meter2)
print(meter1 == meter3)
    

# SOAL 4 
print("===== SOAL 4 =====")

class ElectricityMeter : 
    meter_id = ""
    voltage = 0 
    current = 0 
    
    def __init__(self,meter_id,voltage,current):
        self.meter_id = meter_id
        self.voltage = voltage
        self.current = current 
        
    def calculate_power(self) : 
        return self.voltage * self.current 
    
    def __str__(self):
        return f"Electricity Meter: {self.meter_id} | {self.voltage} V | {self.current} A" 
    
    def __eq__(self, other):
        return self.meter_id == other.meter_id 
    

kwh1 = ElectricityMeter("KWH001", 220, 10)
kwh2 = ElectricityMeter("KWH001", 220, 15) 

print(kwh1)
print(kwh1.calculate_power())
print(kwh1 == kwh2) 


# SOAL 5 
print("===== SOAL 5 =====") 

class IotDevice : 
    device_id = ""
    device_name = ""
    location = ""
    status = "" 
    
    def __init__(self,device_id,device_name,location,status):
        self.device_id = device_id
        self.device_name = device_name
        self.location = location
        self.status = status 
        
    def __str__(self):
        return f"Device: {self.device_id} | {self.device_name} | {self.location} | {self.status}"

    def __eq__(self, other):
        return self.device_id == other.device_id 
    
    def update_status(self,new_status):
        self.status = new_status 
    
    
device1 = IotDevice("DEV001", "Water Meter", "Jakarta", "Online")
device2 = IotDevice("DEV001", "Gas Meter", "Surabaya", "Offline") 

print(device1)
print(device1 == device2)

device1.update_status("Maintenance")
print(device1)

        
# TEST AJA 
print("===== TEST AJA =====") 

class Test : 
    def __init__(self,name,nik,salary = 5000000) : 
        self.name = name 
        self.nik = nik 
        self.salary = salary        
    def __str__(self):
        return f"Nama : {self.name}, NIK : {self.nik}, Gaji : {self.salary}"

orang1 = Test("Zephyr",12345)
orang2 = Test("Aomine",54321)
orang3 = Test("Aomine",54321,950000)


print(orang1)
print(orang2)
print(orang3)



