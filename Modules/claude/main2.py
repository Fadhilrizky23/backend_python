import utils.konversi as kv
import utils.matematika
from utils.matematika import tambah



# if ini cuman di pake di py yang bakal di Run aja, kalo yg kayak konversi / matematika tado. Kecuali mau di testing 
if __name__== "__main__": #best practice 
    print(utils.matematika.kurang(10,5))
    print(utils.matematika.pi)
    print(kv.celc_to_farh(20))
    print(tambah(10,5))
    print("ini akan ke print kalo dia langsung di run, tapi kalo di import dia ga bakal ke print") 



