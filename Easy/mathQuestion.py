import random
from datetime import datetime

min = 1
max = 10
num_problems = 2

operator = ["+", "-", "*"]


def generate_question_answer():
    num1 = random.randint(min, max)
    num2 = random.randint(min, max)

    ran_num = random.randint(0, 2)
    rand_operator = operator[ran_num]

    equation = str(num1) + str(rand_operator) + str(num2)
    answer = eval(equation)
    return equation, answer


for i in range(num_problems):
    equation, answer = generate_question_answer()

    print("Problem #" + str(i + 1) + ": " + equation)

    start_time = datetime.now()
    while True:
        user_input = input("Enter your result: \n")

        try:
            user_number = int(user_input)
        except ValueError:
            print("Invalid Input. This is not a number")
            continue

        if user_number == int(answer):
            print("You got it right")
            break
        else:
            continue

    end_time = datetime.now()

duration = end_time - start_time

print(f"You take {duration.total_seconds()} seconds to finish the game")
