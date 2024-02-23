import random

random_num=random.random()
value=""

if 0<=random_num<=(1/3):
    value="R"
elif (1/3)<=random_num<=(2/3):
    value="P"
else:
    value="S" 

print(value)

print("Hello to Rock Paper Scissor game")
guess = 0

while True:
    input_v=input("Please enter your guess: R for Rock, P for Paper, S for Scissor\n")
    
    if input_v not in ['R', 'P', 'S']:
        print("Invalid input. Please enter R, P, or S.")
        continue
    
    if input_v == value:
        print("You got it right!")
        break
    else:
        guess+=1 

print(f'You are wrong {guess} times')