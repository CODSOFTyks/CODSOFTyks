#calculatorbyyashkumarsingh
a = int(input("Enter a number:"))
b = int(input("Enter a number:"))
print("1 => PRESS 1 FOR MULTIPLICATION")
print("2 => PRESS 2 FOR DIVISION")
print("3 => PRESS 3 FOR ADDITION")
print("4 => PRESS 4 FOR SUBSTRACTION")
print("5 => PRESS 5 FOR MODULUS")
c = int(input("ENTER YOUR CHOICE:"))
if c == 1:
    print(a*b)
elif c == 2:
    print(a/b)
elif c == 3:
    print(a+b)
elif c == 4:
    print(a-b)
elif c == 5:
    print(a%b)
else:
    print("ENTER A VALID CHOICE!!!")
    
