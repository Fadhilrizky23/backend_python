umur = int(input("Masukan Umur anda : "))
status_sim = input("Punya SIM (Y/N) : ")


if(umur >= 17 and status_sim.upper() == "Y"):
    print("Road Legal")
else:
    print("Road Illegal") 

