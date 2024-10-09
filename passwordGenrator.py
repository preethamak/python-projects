import random
import string

def password(min_length, numbers=True, characters= True):
    letters= string.ascii_letters
    digits = string.digits
    char= string.punctuation
    
    characters = letters
    if numbers:
        characters+=digits
    if char:
        characters+=char
        
    pwd =""
    has_number = False
    has_char = False
    criteria = False

    while not criteria or len(pwd)<min_length:
        Nchar = random.choice(characters)
        pwd+= Nchar
        
        if Nchar in digits:
            has_number = True
        elif Nchar in char:
            has_char = True
            
        criteria = True
        if numbers:
            criteria= has_number
        if char:
            criteria= criteria and has_char
    
    return pwd

pwd = password(10)      
print(pwd)