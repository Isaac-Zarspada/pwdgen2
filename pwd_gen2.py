# password generator for ana 
import random

# list of characters
numbers = list('1234567890')
special_characters = list('!@#$^&*()')
low_char  = list("qwertyuiopasdfghjklzxcvbnm")
upper_char = list(map(lambda x:x.upper(), low_char))
complete_abc =  low_char+upper_char+special_characters+numbers

def passwordgen_2(length, char_bank, keyboard= "US", *space_exception:bool, **special_char:str, ):
    x = 0
    password = ""
    while x < length:
        next_char = random.choice(char_bank)
        password += next_char
        x += 1
    print(password)
char_length = int(input("How many characters does your password need?:"))
passwordgen_2(char_length, complete_abc)
