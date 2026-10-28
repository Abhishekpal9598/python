from random import*
import os 
u_pwd=input("enter a password:")
pwd=['a','b''c','d','e','f','e','1','2','3','4','5','7','8','9']
pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(len(u_pwd)):
        guess_pwd=pwd[randint(0,17)]
        pw=str(guess_pwd)+str(pw)
        print(pw)
        print("cracking passwordd...please")
        os.system("cls")
print("your password is :",pw)        