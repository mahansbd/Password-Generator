import random

uppercase_letters = "ABCDEFGHIJkLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "()[]{},.:;-_/\\?*# "

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

length = 40
amount = 20

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)