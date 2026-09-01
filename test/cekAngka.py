def cekAngka(x): 
    match x : 
        case 1|2|3 : 
            print("kecil")
        case int()|float() : #ini dia cek ini instance dari class ini / bukan  
            print("masuk tipe Data",type(x))
        case _:
            print("Bukan Angka")

cekAngka(23.1) #float 
cekAngka(23) #int
cekAngka(False) #Bool, karena bool itu turunan dari int, jadi masuk ke case int()
cekAngka("Lima") #Bukan Angka 





