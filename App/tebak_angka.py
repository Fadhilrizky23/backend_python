# TEBAK ANGKA 

# 1. BIKIN ANGKA RANDOM
# 2. HINT TERLALU BESAR / TERLALU KECIL 
# 3. JUMLAH TEBAKAN 
# 4. MAKSIMAL JUMLAH TEBAKAN ( 3x ) 

import random

angka = random.randint(1,100)

count = 3
def hitung() : 
    global count
    count -= 1 
    return int(count)


while True : 
    print("=== TEBAK ANGKA ====")
    angka_tebakan = input("Masukan Angka ( kesempatan 3x ): ")
    sisa_kesempatan = hitung()

    if int(angka_tebakan) > angka : 
        print(f"Angka terlalu besar, kesempatan {sisa_kesempatan} kali")
        if sisa_kesempatan == 0 : 
            print(f"kamu gagal, angka yang benar adalah {angka}")
            break
    elif int(angka_tebakan) < angka : 
        print(f"Angka terlalu kecil , sisa kesempatan {sisa_kesempatan} kali")
        if sisa_kesempatan == 0 : 
            print(f"kamu gagal, angka yang benar adalah {angka}")
            break
    elif int(angka_tebakan) == angka : 
        print("SELAMAT TEBAKAN KAMU BENAR !!!")
        break 






