#ROCK PAPERS SCISSORS BY YASH KUMAR SINGH
import random as rd
print("-------------ROCK PAPERS SCISSORS GAME------------------")
A = input("ENTER YOUR MOVE : \t")
B = rd.choice(["ROCK","PAPERS","SCISSORS"])
print("COMPUTER'S CHOICE IS : \t",B)
if (A == "ROCK")and (B == "SCISSORS"):
    print("YOU WIN!!")
elif (A == "ROCK") and (B == "PAPERS"):
    print("....COMPUTER WINS....")
elif (A == "PAPERS") and (B == "ROCK"):
    print("YOU WIN!!!")
elif (A == "PAPERS") and (B == "SCISSORS"):
    print("....COMPUTER WINS....")
elif (A == "SCISSORS") and (B == "PAPERS"):
    print("YOU WIN!!!")
elif (A == "SCISSORS") and (B == "ROCK"):
    print("....COMPUTER WINS....")
else:
    print("....DRAW....")
