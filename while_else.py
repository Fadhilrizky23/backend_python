import getpass

password_benar = "python123"
percobaan = 0
max_percobaan = 3 

while percobaan < max_percobaan : 
    password = getpass.getpass("Masukan Password : ")
    percobaan += 1 

    if password == password_benar : 
        print(f"Login berhasil, selamat datang {getpass.getuser()}")
        break 
    else : 
        print("Password Salah ,sisa percobaan : ",max_percobaan - percobaan) 
else : 
    print("Batas percobaan gagal, silahkan coba lagi minggu depan")