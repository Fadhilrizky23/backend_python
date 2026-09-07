# Pyton module standart Lib 
# Module bawaan Python 


# Math Module 
import math


list = [2.1,4.1,6.1,8.1,10.1,12.1,14.1,16.1,18.1,20.1] 

for x in list : 
    print(math.ceil(x)) #pembulatan ke atas

print(math.pi)


def cosinus(a,b,c):
    return f"nilai cosinus adalah : {math.cos(b/c)}" 


lebar = int(input("Masukan A :"))
tinggi = int(input("Masukan B :"))
miring = int(input("Masukan C :"))
        
print(cosinus(tinggi,lebar,miring)) 

