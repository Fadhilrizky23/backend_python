import math
from package.metematika_package import dasar
from package.metematika_package.geometri import luas_lingkaran 
import package.metematika_package.test as testing


a = 12 
b = 4 

hasil = dasar.kali(a,b)
print(f"Hasil perkalian = {hasil}") 

jari_jari = b+3 

luas = luas_lingkaran(jari_jari)
print(f"Luas lingkaran dengan jari-jari {jari_jari} = {luas}") 

watt = 800
time = 5 #waktu dalam jam


nilai_kwh = testing.kvar(watt,time)
print(f"Nilai kWh = {math.ceil(nilai_kwh)} kWh")


