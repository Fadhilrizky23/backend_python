import random

bank_soal = []

print("==== SOAL LATIHAN ====")
with open("bank_soalSD.txt","r") as file :
    baris = 1
    file_soal = file.readlines()[1:]
    
    for i in file_soal : 
        # print(f"Baris {baris} : {i.strip()}")
        # baris += 1
        pertanyaan_pilihan = i.strip().split("|")
        Pertanyaan = pertanyaan_pilihan[0].strip()
        jawaban = pertanyaan_pilihan[1].strip().split(',')
        jawaban_benar = jawaban[0]


        soal = {
            "Pertanyaan" :Pertanyaan,
            "Jawaban" :jawaban,
            "Jawaban_benar" :jawaban_benar
        } 

        bank_soal.append(soal) 

nomor = 1 
score = 0 

random.shuffle(bank_soal)

for soal in bank_soal :  

    print(f"{nomor}. {soal["Pertanyaan"]}")

    random.shuffle(soal["Jawaban"]) 

    # Nampilin jawaban pake Label ABCD 
    labels = ["A","B","C","D"] 
    for index, label in enumerate(soal["Jawaban"]):
        print(labels[index], label) 



    # Input dr siswa 
    jawaban_siswa = input("Masukan jawaban (A/B/C/D) : ").upper() 

    # validasi ABCD 
    while jawaban_siswa not in labels : 
        print("Input Tidak valid")
        jawaban_siswa = input("Masukan jawaban (A/B/C/D) : ").upper() 

    
    idx_jwb = labels.index(jawaban_siswa)

    nomor += 1 

    if soal["Jawaban"][idx_jwb] == soal["Jawaban_benar"]: 
        score +=1  


def writeUser(nama) : 
    with open("hasil_ujian.txt","a") as file :
        file.write(f"{nama},{score},{score/len(bank_soal) *100:.2f} \n")

print("==== HASIL AKHIR ====")
nama_siswa = input("Masukan nama kamu = ") 
writeUser(nama_siswa)
print(f"kamu betul {score} dari total {len(bank_soal)}") 
print(f"{nama_siswa} Nilai kamu {score / len(bank_soal) *100:.2f}")


