kalimat = input("masukan Kata kata hari ini : ")
huruf_find = input("Masukan 1 Huruf yg mau di cari :")

for huruf in kalimat:

    if huruf == huruf_find :
        print(huruf)
        break
else : #kalo nulis Else nya sejajar sama if dia Iterasi semua, jadi B cek, U cek, D Cek gitu  
        print("gak ketemu brooo")