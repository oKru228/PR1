import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_round():
    num = random.randint(2, 100)
    question = str(num)
    correct_answer = "yes" if is_prime(num) else "no"
    return question, correct_answer
