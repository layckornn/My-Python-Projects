# THIS IS HOW THE PASSWORD GENERATOR WORKS.

# Welcome to the Password Generator 

# How many Letters would you want in your password?

# How Many Symbols would you like?

# How Many numbers would you like?

#The give output based on the imputs provided.



import random

letters = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F',
           'G', 'H','I','J','K','L','M','N','O','P','Q','R','S','T','U',
           'V','W','X','Y','Z']

numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = [ '!', '@', '#', '$', '%', '&', '*', '(', ')', '?', '>', '+']

print("Welcome to the Password generator")

n_letters = int(input("How many letters you want in your password?\n"))

n_numbers = int(input("How many letters you want in your numbers?\n"))

n_symbols = int(input("How many letters you want in your symbols?\n"))

password_list = []

for i in range(1, n_letters+1): #We want 1 to n_letters number to be generated
    char = random.choice(letters)
    password_list += char

for i in range(1, n_symbols+1):
    char = random.choice(symbols)
    password_list += char

for i in range(1, n_numbers+1):
    char = random.choice(numbers)
    password_list += char

random.shuffle(password_list)

password = ""

for char in password_list:
    password += char

print(password)