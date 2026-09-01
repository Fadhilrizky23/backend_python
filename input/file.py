# OPEN FILE 

# file = open("geek.txt","r") 

# print("Filename = ", file.name)
# print("Content = ", file.read()) 
# print("Mode :", file.mode)
# print("is Closed ??", file.closed) 


# file.close()
# print("is Closed ??", file.closed)  


# WRITE FILE 

# with open('geek.txt',"w") as file : 
#     while True : 
#         data = input("masukan data (enter untuk stop)= ")

#         if data == "":
#             break 
#         file.write(data+"\n")

# print("File written success") 


# # WITH STEATMENT ( gak perlu pake .close())
# with open('data.txt','r') as file:
#     for line in file :
#         print(line.strip()) #Buang whitespace / enter di akhir kayak end=""  


# with open("data_siswa.txt", "r") as file:
#     for i in file : 
#         data = i.strip().split(",")
#         print(f"{data[0]} ={data[1]}")


# # Handling Exceptions
# try: 
#     with open("","r") as file : 
#         content = file.read()
#         print(content)


# except FileNotFoundError : 
#     print("file tidak di temukan") 

# finally : 
#     file.close() 


with open("data.txt","r") as file: 
    total = 0 
    for i in file : 
        for str in i.strip() :
            data_int = int(str)
            total+= data_int

    print(total)





