# Cara menggunakan Module import + nama module (nama file tanpa py)
import matematik


# urutan 
# 1. Import 
# 2. consta /variabel 
# 3. function 
# 4. _main_ 


if __name__ == "__main__" : 
    hasil1 = matematik.tambah(1,2)
    hasil2 = matematik.kali(10,23) 

    print(f"Hasil dari 1 + 2 = {hasil1}")
    print(f"Hasil dari 10 * 23 = {hasil2}") 
    print(f"Nilai Pi = {matematik.pi}")
    print(f"Hasil dari 10 * 23 = {hasil2}")
    print(f"Dibuat oleh {matematik.nama_pembuat}")








