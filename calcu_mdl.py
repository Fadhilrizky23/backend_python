from calculator import operasi


if __name__ == "__main__" : 
    while True : 
        print("=== PROGAM CALCULATOR SEDERHANA ===")
        print("1. Penjumlahan")
        print("2. Pengurangan")
        print("3. Perkalian")
        print("4. Pembagian")g
        print("5. keluar")
        print("=== PROGAM CALCULATOR SEDERHANA ===")

        try : 
            pilihan = int(input("Pilihan : "))

            if pilihan == 1 : 
                operasi.tambah()
            elif pilihan == 2:
                operasi.kurang()
            elif pilihan == 3:
                operasi.kali()
            elif pilihan == 4:
                operasi.bagi()
            elif pilihan == 5:
                print("=== THANK YOU ===")
                break 
            else : 
                print("Error, pilihan tidak valid")
        except ValueError : 
            print("Masukan nomor yang valid")




