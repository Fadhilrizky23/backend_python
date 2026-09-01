# NESTED IF 
import getpass

username = input("username : ")
password = getpass.getpass("password : ")

if username == "admin" : 
    if password == "12345":
        print("Login berhasil")
        print("Welcome Admin")
    else :
        print("Password Salah") 
else : 
    print("Username Tidak Ditemukan")


