#passwordgeneratorbyyashkumarsingh
import random as rd
l = int(input("ENTER THE DESIRED LENGTH OF PASSWORD : \t"))
arr = ["!","@","#","$","%","^","&","*","1","2","3","4","5","6","7","8","9","0"]
pwd = ""
for i in range(l):
    pwd = pwd + rd.choice(arr)
print("YOUR PASSSWORD IS : \t")
print(pwd)
    

