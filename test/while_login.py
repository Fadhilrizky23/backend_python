import getpass 


password = "" 

# while password == "12345":  kalo kayak gini dia akan nulis ulangi kalo password == 12345 tapi di awal dia langsung false jadi gak jalan apa apaan 

# jadinya harus pake != selama dia blm 12345 pass nya, dia jalan terus 
nama = getpass.getuser() 

while password != "12345": 
    password = input("Masukin Pass : ")
    if password != "12345":
        print("Password salah, coba lagi") 

print(f"selamat datang {nama}")




