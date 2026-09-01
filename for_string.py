nama = ["Apple","mangga","pisang","anggur"]

for buah in nama: #buah disini isi elemennya, bkn indexnya 
    print(buah) 


for buah in range(len(nama)): #buah disini isinya index
    print(nama[buah],buah) #jadi kalo mau akses harus nama[buah]