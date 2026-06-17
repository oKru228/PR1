from VD_games.games import calc, gcd
from VD_games.engine import run_game
import prompt

def main():
    print("Welcome to the VD Games Portal!")
    print("Available games:")
    print("1. calc (Calculator)")
    print("2. gcd (Greatest Common Divisor)")
	
    choice = prompt.string("Choose a game (write name or number): ")
    choice = choice.strip().lower()
	
    if choice == "calc" or choice == "1":
        run_game(calc)
    elif choice == "gcd" or choice == "2":
        run_game(gcd)
    else:
        print(f"Unknown game: '{choice}'. Goodbye!")

if __name__ == "__main__":
    main()
