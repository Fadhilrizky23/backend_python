# Import full module matematik (jangan alias), terus panggil tambah() dan pi pakai nama module di depan.
# Import alias untuk konversi jadi kv, terus panggil celsius_ke_fahrenheit() pakai alias itu.
# Import spesifik function kali dan bagi aja dari matematik (langsung, tanpa nama module di depan). 


import claude.utils.konversi as kv
import matematik
from matematik import kali, bagi


if __name__ == "__main__":

    print(matematik.tambah(10,23)) 
    print(matematik.pi) 
    print(kv.celc_to_farh(20)) 
    print(kali(10,5))
    print(bagi(12,4))