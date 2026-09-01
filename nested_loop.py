
# Nested LOOP 

for i in range(1,6):
    for j in range(1,6):
        print("i:",i,"j:",j)




# kasih end= biar dia di baris yang sama

kata  = "buah"
for i in range (len(kata)) : 
    print(kata[i], end="")   

# # Segitiga siku 
print("Segitiga Siku")

for i in range (1,5):
    for j in range(i):
        print("*", end="")
    print() 


# # Segitiga Kebalik 
print("Segitiga Kebalik")

for i in range (4,0, -1): 
    for j in range (i):
        print("*", end="")
    print()
 

# # Piramid 
print("Piramid")

for i in range(1, 5):
    for x in range(4 - i):      
        print(" ", end="")
    for y in range(2*i - 1):    
        print("*", end="")
    print()



# # Belah Ketupat 
print("Belah Ketupat")

for i in range(1, 5):
    for x in range (4 - i ):
        print(" ",end="")
    for y in range (2*i - 1):
        print("*",end="")
    print()

for i in range (3,0,-1):
    for x in range (4 - i):
        print(" ",end="")
    for y in range (2*i - 1 ):
        print("*", end="")
    print() 


# # Setengah piramid siku 
print("Piramid Siku")

for i in range (1,5):
    for j in range (i):
        print("*", end="")
    print()
for i in range(5,0,-1):
    for j in range (i):
        print("*",end="")
    print() 

# ADVANCE 
print("121 piramid") 

for i in range (1,5):
    for x in range ( 5 - i):
        print(" ",end="")
    for naik in range (1,i+1):
        print(naik,end="")
    for turun in range (i-1,0,-1):
        print(turun,end="")
    print()  

# for i in range (4,0,-1):
#     print(i)