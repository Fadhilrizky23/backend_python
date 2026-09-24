import requests
from config.setting import BASE_URL

def ambil_semua_post():
    # TODO: GET /posts, return list of dict
    response = requests.get(f"{BASE_URL}/posts")

    # cek status 
    if response.status_code == 200 : 
        data = response.json()
        return data
    # kalo gagal ambil data
    else : 
        print("gagal ambil data")
        return[] 

def ambil_detail_post(post_id):
    # TODO: GET /posts/{post_id}, return dict
    response = requests.get(f"{BASE_URL}/posts/{post_id}") 

    if response.status_code == 200 : 
        return response.json()
    else :
        print("gagal mengambil data")
        return {}

def tampilkan_detail_post(posts): 
    # TODO: print title dan body
    print(f"{posts["title"]} : {posts["body"]}")


def tampilkan_daftar_post(posts):
    # TODO: loop posts, print id dan title 
    for data in posts : 
        print(f"{data["id"]} : {data["title"]}") 
