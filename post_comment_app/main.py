from modules import post
from modules import comment 


def main():
    while True : 
        print("1. Daftar Post")
        print("2. Detail Post")
        print("3. comment di post")
        print("0. keluar")

        pilihan = int(input("Pilihan : ")) 

        try :
            id_input = int(input("Masukan id : "))
        except ValueError : 
            print("Id harus berupa angka!")
            # balik ke awal While, kalo mau balik di bagian ini doang, si Minta ID ini di bikin func kecil sendiri 
            continue

        # TODO: if/elif sesuai pilihan
        # 1 -> tampilkan_daftar_post(ambil_semua_post())
        # 2 -> input id, tampilkan_detail_post(ambil_detail_post(id))
        # 3 -> input id, tampilkan_daftar_comment(ambil_comment_post(id))
        # 0 -> break 


        if pilihan == 1 : 
            post.tampilkan_daftar_post(post.ambil_semua_post()) 
        elif pilihan == 2:
            post.tampilkan_detail_post(post.ambil_detail_post(id_input))
        elif pilihan == 3:
            comment.tampilkan_daftar_comments(comment.ambil_comment_post(id_input))
        elif pilihan == 0 :
            print(" === Sign out === ")
            break;
        else : 
            print("Bukan input yang valid.....") 


if __name__ == "__main__":
    main()
