import random

DESCRIPTION = "What is the result of the expression?"


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2}"

    if operator == "+":
        correct_answer = num1 + num2
    elif operator == "-":
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    return question, str(correct_answer)
