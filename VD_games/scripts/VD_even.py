import random
import prompt
from VD_games.cli import welcome_user

def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answers = 0
    
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        answer = prompt.string('Your answer: ')
        
        is_even = (number % 2 == 0)
        correct_answer = 'yes' if is_even else 'no'
	
        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print("Let's try again!")
            return
            
    print("Congratulations!")

if __name__ == "__main__":
    main()
