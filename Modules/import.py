# Import Full module seperti yang kemarin import mamematik 
# kalo mau pake, harus sebut nama module di depan

# Import salah satu function dari module matematik 
# from nama_module import nama_function
# kalo lebih dr 1, import nama_function1, variabl | gak perlu sebut nama module di depan 

# Import dengan alias, import nama_module as alias  | gak perlu lagi nyebut nama module nya 

import matematik as mt 


from matematik import bagi, kali 

from tes import *


if __name__ == "__main__": 
    print(kali(2,5))  


print(mt.tambah(5,12))
print(mt.pi)
print(greeting("Fadhil"))

