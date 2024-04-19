import random

"Declare the characters you want in your password"
uppercase_letters = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.:;-_/\\?*# "

'''Change to false to disable characters, and change to true to enable characters.'''
upper, lower, nums, syms = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if nums:
    all += digits
if syms:
    all += symbols

'''Here you can change the length of the password, and/or the amount of passwords created.'''
length = 20
amount = 10


for x in range(amount):
    password = "".join(random.sample(all, length))


    print(password)