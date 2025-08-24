import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 1
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("There are 10 Questions to answer\nPress enter to start!")
print("----------------------")

start_time = time.time()

for i in range(1,TOTAL_PROBLEMS+1):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i) + " : " + expr + " = ")
        if guess == str(answer):
            break
        print("Wrong Answer!!!")
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print("Nice work! You finished in", total_time, "seconds!")
print(wrong,"Wrong answeres were guessed")