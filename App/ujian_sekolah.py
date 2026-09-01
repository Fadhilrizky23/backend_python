# UJIAN SEKOLAH 

# 1. Membaca soal dari File 
# 2. Mengacak soal Ujian 
# 3. Mengacak posisi jawaban 
# 4. Hasil Score murid 
import random

print("=== UJIAN SEKOLAH ===") 

daftar_soal = []

with open('bank_soal.txt','r') as file:
    baris_file = file.readlines()[1:]  # skip header
    for baris in baris_file : 
        bagian = baris.strip('').split('|')
        pertanyaan = bagian[0].strip()
        pilihan = bagian[1].strip().split(',') 

        jawab_benar = pilihan[0] #store jawaban benar sebelum di shuffle 

        soal = {
            "pertanyaan" : pertanyaan,
            "pilihan" : pilihan,
            "jawaban" : jawab_benar
        } 

        daftar_soal.append(soal) 


# Pertanyaan 

skor = 0 
nomor = 1

for soal in daftar_soal : #daftar soal bentuknya list, jadi pas di looping udah isinya ( dict langsung )
    print(f"{nomor}. {soal["pertanyaan"]}") 

    random.shuffle(soal['pilihan']) #random jawaban 

    label = ["A","B","C","D"]
    for i, pilihan in enumerate(soal["pilihan"]) : #ngasih index 0,1,2,3 otomatis sambil looping, dipakai buat mapping ke label
        print(f"{label[i]}. {pilihan}") 


    # input jawaban 
    jawaban_siswa = input("jawaban kamu (a/b/c/d) = ").strip().upper() 

    # Convert jawaban 
    index_jawaban = label.index(jawaban_siswa) #cari posisi huruf yang diketik siswa (misal "B" → index 1), lalu dipakai buat ambil teks pilihan yang sesuai. 
    teks_jawaban = soal["pilihan"][index_jawaban] 

    # VALIDASI 
    if teks_jawaban == soal["jawaban"]:
        skor += 1

    nomor +=1 


print("==== HASIL AKHIR =====")
print(f"Kamu betul {skor} dari {len(daftar_soal)}")
print(f"Nilai kamu {skor/len(daftar_soal) * 100:.2f}")

   


