class Laptop : 
    brand = ""
    ram = 0
    processor = 0


laptop1 = Laptop()
laptop2 = Laptop() 

laptop1.brand = "Lenovo"
laptop1.ram = 16 
laptop1.processor = 5 

print(laptop1.brand)
print(f"{laptop1.ram} GB")
print(f"Intel Core i{laptop1.processor}") 


# SOAL 2 

class Employee : 
    name = ""
    position = ""
    salary = 0
    
    def introduce(self):
        print(f"Nama : {self.name}")
        print(f"Position : {self.position}")
        print(f"Gaji : {self.salary}") 
        

fadhil = Employee()
fadhil.name = "Fadhil"
fadhil.position = "Project Controller"
fadhil.salary = 8500000
fadhil.introduce()
        
# SOAL 3 

class WaterMeter : 
    brand = ""
    serial_number = "" 
    total_volume = 0 
    
    def add_volume(self,volume):
        self.total_volume += volume 
    
meter = WaterMeter()
meter.brand = "Itron"
meter.serial_number = "WM001"
meter.total_volume = 100
meter.add_volume(50)
meter.add_volume(25)

print(f"{meter.total_volume} m^3")

# SOAL 4 

class ElectricityMeter : 
    meter_id = ""
    voltage = 0
    current = 0 
    
    def show_data(self) : 
        print(f"Meter ID : {self.meter_id}")
        print(f"Voltage : {self.voltage} V")
        print(f"Current : {self.current} A")
        
    def calculate_power(self):
        return f"{self.voltage*self.current} Watt"  
    
    
kwh1 = ElectricityMeter() 
kwh1.meter_id = "KWH001"
kwh1.voltage = 200 
kwh1.current = 10
daya = kwh1.calculate_power()

kwh1.show_data()
print(f"Power : {daya}")


# SOAL 5 

class IotSensor : 
    device_name = ""
    location = ""
    temperature = 0 
    humidity = 0  
    
    def show_status(self):
        print(f"Device : {self.device_name}")
        print(f"Location : {self.location}")
        print(f"Temperature : {self.temperature}")
        print(f"Humidity : {self.humidity}") 
        
    def update_temperature(self,new_temp):
        self.temperature = new_temp 
        
    def check_temperature(self):
        if self.temperature >= 35 : 
            return "WARNING: High Temperature!"
        elif self.temperature >= 20 and self.temperature < 35 : 
            return "Temperature Normal" 
        else :
            return "WARNING: Low Temperature!" 
        
        
        
sensor1 = IotSensor()
sensor2 = IotSensor() 

sensor1.device_name = "temp sensor"
sensor1.location = "Jakarta"
sensor1.temperature = 50
sensor1.show_status()
cek = sensor1.check_temperature()
print(cek)
        

sensor2.device_name = "temp sensor"
sensor2.location = "Surabaya"
sensor2.temperature = 25
sensor2.show_status()
cek = sensor2.check_temperature()
print(cek)
    

        


