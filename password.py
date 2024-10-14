from random import *
import os
import string
your_password = input("enter your password: ")
letters= string.ascii_letters

    
pw=""
while pw!= your_password:
    pw=""
    for letter in range(len(your_password)):
        guess_pwd = letters[randint(0,27)]
        pw = str(guess_pwd)+str(pw)
        print(pw)
        print("cracking password..... please wait")
        os.system("cls")
print("your password is: ",pw)

    