from VD_games.games import calc, gcd, prime, progression
from VD_games.engine import run_game
import prompt

def main():
    print("Welcome to the VD Games Portal!")
    print("Available games:")
    print("1. calc (Calculator)")
    print("2. gcd (Greatest Common Divisor)")
    print("3. progression (Arithmetic Progression)")
    print("4. prime (Prime Number)")

    choice = prompt.string("Choose a game (write name or number): ")
    choice = choice.strip().lower()

    if choice == "calc" or choice == "1":
        run_game(calc)
    elif choice == "gcd" or choice == "2":
        run_game(gcd)
    elif choice == "progression" or choice == "3":
        run_game(progression)
    elif choice == "prime" or choice == "4":
        run_game(prime)
    else:
        print(f"Unknown game: '{choice}'. Goodbye!")


if __name__ == "__main__":
    main()
