# List kosong 



angka = [1,2,3,4,5]

for data in angka : 
    print(data) 


nama = ["Lea","Alice","Anggie"]

for x in range(len(nama)):
    print(nama[x]) 


gabungan = ["Apple",12,"Jakarta","124"]

for dataSet in range(len(gabungan)) : 
    if dataSet % 2 == 1 : #ganjil only
        print(gabungan[dataSet])
    else : 
        continue


# Manipulasi List 
a = [1,2] 
a.append(3) #nambah di akhir
print(a)

a.insert(2,99) #nambah di index ke berapa, Nilainya 
print(a)

a.extend([4,5]) #gabungin 2 list, otomatis jd data yg belakang
print(a) 

# Update Element 
a = [10,20,30,40,50] 
a[1] = 25
print(a) 

x = [4,5,6,7]
x.remove(5) #hapus berdasarkan value(nilai) bukan index ataupun element
print(x)

x.pop()
print(x)


tes = [1,2,3,4,5,6,7,8,9,10] 
del tes[3] #hapus index ke 3 ( nilainya 4) 
print(tes) 
print(len(tes))
tes.clear()
print(tes) 


# NESTED LIST 
looping = [[1,2],[3,4]] 
print(len(looping))

a = 0;

for i in looping:
    for x in i : 
        print(x)
        

testi = [[1,2,3],[4,5]]

for list in testi : 
    for sub in list :
        print(sub) 


data = [[1, 2, 3], [4, 5], [6]]
total = 0

for i in data : 
    for x in i : 
        total += x 

print(total) 

# Pengecekan
banyak_buah = ["apple","mangga","jeruk","durian"]
input_buah = input("Masukan buah : ")

if input_buah.lower() in banyak_buah : 
    print(" Buah ini ada stock nya")
else : 
    print("Stock Habis")