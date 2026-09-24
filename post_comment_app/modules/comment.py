import requests 
from config.setting import BASE_URL,TYPE


def ambil_comment_post(post_id):
    # TODO: GET /posts/{post_id}/comments, return list of dict
    response =requests.get(f"{BASE_URL}/{TYPE}/{post_id}/comments")

    if response.status_code == 200: 
        content = response.json()
        return content
    else : 
        print("gagal mengambil data")
        return []


def tampilkan_daftar_comments(comments):
    # TODO: loop comments, print name, email, body
    for list_comment in comments : 
        print(f"Name : {list_comment["name"]} \nList : {list_comment["email"]} \nBody : {list_comment["body"]} \n ----------------") 

