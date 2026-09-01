# matematika.py 

# ini namanya doc string
""" penjumlahan 2 angka """
def tambah (a,b) : 
    return a + b 

def kurang(a,b):
    return a - b 


""" 
kali 2 angka 
"""
def kali(a,b):
    return a - b 


def bagi(a,b):
    if b != 0 : 
        return a / b 
    else :
        return "Tidak bisa di bagi 0" 

# VARIABEL yang bisa di pake 
pi = 3.141516 
nama_pembuat = "Fadhil Rizky" 

# Pattern name 
# ini akan jalan kalo ini di jalanin langsung, bkn di import ke file lain 

if __name__ == "__main__":
    print("ini di jalanin langsung, bkn di import") 
