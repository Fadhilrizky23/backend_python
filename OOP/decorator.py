
# Static Method Decorator  

class Matematika: 

# Kita gak perlu lagi bikin Class 
    @staticmethod
    def tambah(a,b):
        return a + b 


hasil = Matematika().tambah(5,10)
print(hasil) 



# Factory Method ( membuat Class dari Class itu sendiri ) 

class BankAccount : 
    no = ""
    balance = 0
    status = True 

    def __init__(self,no,balance = 0):
        self.no = no 
        self.balance = balance


    # Bikin Factory Method untuk bikin Active ini bisa jadi False 
    # bkn pakai self tapi pake cls 
    @classmethod 
    def disabled(cls,no,balance=0):
        result = cls(no,balance) #se olah olah kita bikin Class dari BankAccount 
        result.status = False 
        return result 



akun1 = BankAccount("001",100_000_000_000)
akun2 = BankAccount.disabled("002",50_000_000_000)
print(f"Bank Account {akun1.no} has balance {akun1.balance} and status {akun1.status}")
print(f"Bank Account {akun2.no} has balance {akun2.balance} and status {akun2.status}")


