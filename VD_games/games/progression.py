import random

DESCRIPTION = "What number is missing in the progression?"


def generate_round():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    progression = [start + i * step for i in range(length)]

    idx = random.randint(0, length - 1)
    correct_answer = progression[idx]
    progression[idx] = ".."

    question = " ".join(map(str, progression))
    return question, str(correct_answer)
