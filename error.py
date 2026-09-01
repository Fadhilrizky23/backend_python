# Error 

# print("Hello World" 

# print(nama) 


# TYPE ERROR 
# print(5 + '5') 

# value Error 
# angka = int('abc')


# # Index Error 
# list_data = [1,2,3]
# print(list_data[5])


# # key Error 
# data = {
#     "nama" : "Fadhil"
# } 

# print(data["umur"])

# ZeroDivisiion 0 
# print(10/0) #tidak bisa di bagi 0 karena tidak terhingga  


# TRY EXCEPT 

print("=== Kalkulator Sederhana ===") 

# try : 
#     angka1 = int(input("Angka Pertama : ")) 
#     angka2 = int(input("Angka Kedua : ")) 
#     hasil = angka1 / angka2 
#     print(f"hasil : {hasil}")
# except : 
#     print("Terjadi error dalam perhitungan")

# print("=== Program Selesai ===") 


# try : 
#     angka1 = int(input("Angka Pertama : ")) 
#     angka2 = int(input("Angka Kedua : ")) 
#     hasil = angka1 / angka2 
#     print(f"hasil : {hasil}")
# except ValueError: 
#     print("Masukan Angka yang valid")
# except ZeroDivisionError : 
#     print("pembagi tidak bisa 0 ")
# except : 
#     print("Terjadi Error") 


# # TRY EXPECT Else 
# try : 
#     angka = int(input("Masukan Angka : "))
# except ValueError: 
#     print("Masukan Angka yang benar!!") 
# else : 
#     print("Angka yang anda masukan : ", angka)
#     if angka > 0 : 
#         print("Angka Positif")
#     elif angka < 0 : 
#         print("Angka Negatif")
#     else : 
#         print("Angka Nol") 


# TRY EXPECT Finally 
try : 
    angka = int(input("Masukan Angka : "))
except ValueError: 
    print("Masukan Angka yang benar!!") 
else : 
    print("Angka yang anda masukan : ", angka)
    if angka > 0 : 
        print("Angka Positif")
    elif angka < 0 : 
        print("Angka Negatif")
    else : 
        print("Angka Nol")
finally : 
    print("==== PROGRAM SELESAI DIJALNKAN =====")

