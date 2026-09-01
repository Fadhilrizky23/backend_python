def tambah():
    print("=== FUNGSI PERTAMBAHAN ===")
    angka1 = input("Masukan Angka 1 : ")
    angka2 = input("Masukan Angka 2 : ") 
    return int(angka1) + int(angka2) 

def kurang():
    print("=== FUNGSI PENGURANGAN ===")
    angka1 = input("Masukan Angka 1 : ")
    angka2 = input("Masukan Angka 2 : ") 
    return int(angka1) - int(angka2) 

def kali():
    print("=== FUNGSI PERKALIAN ===")
    angka1 = input("Masukan Angka 1 : ")
    angka2 = input("Masukan Angka 2 : ") 
    return int(angka1) * int(angka2) 

def bagi():
    print("=== FUNGSI PEMBAGIAN ===")
    angka1 = input("Masukan Angka 1 : ")
    angka2 = input("Masukan Angka 2 : ") 
    return int(angka1) / int(angka2) 

while True : 
    data = input("Masukan menu yang mau di pilih ( 1 -4 ), Enter untuk stop : ") 

    if data == "" : 
        break
    elif data == "1" : 
        print(f"Total : {tambah()}") 
    elif data == "2" : 
        print(f"Total : {kurang()}")
    elif data == "3" : 
        print(f"Total : {kali()}")
    elif data == "4" : 
        print(f"Total : {bagi()}") 
    else : 
        print("Bukan Bagian dari kalulator")
    

