import getpass 


password = "" 

nama = getpass.getuser()    

while password != "12345":  #kalo dia == dia langsung False, jadi gak ada yg di eksekusi
    password = input("Masukin Pass : ")
    if password != "12345":
        print("Password salah, coba lagi") 

print(f"selamat datang {nama}")