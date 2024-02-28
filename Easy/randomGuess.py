from test import function

import random

min=input("Enter Min Number")
max=input("Enter Max Number")

num=random.randint(int(min), int(max))
guess=0
while num != int(input("Enter your number:")):
    guess+=1
    
print(f'You guessed {guess} times, last time was correct')
