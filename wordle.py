from colorama import Fore, init
import time
import random

init(autoreset=True)

def main():
    category = rules()
    global wordle
    wordle = choose_wordle(category)
    attempts = 0
    print(wordle)
    while attempts < 6:
        guess = input("Word: ").upper()
        if len(guess) != 5:
            print("Not a five-letter word! Try again.")
            continue
        else:
            if guess == wordle:
                print("You guessed the word!", Fore.GREEN + "{wordle.upper()}")
                break
            else:
                for a in range(5):
                    print(f" {check_letter(guess, a)}", end="")
                attempts += 1
                print()

def rules():
    print("Welcome to WORDLE in python!")
    time.sleep(3)
    print("HOW TO PLAY")
    time.sleep(3)
    print(" • Try to guess the word in 6 tries")
    time.sleep(0.5)
    print(" • All guesses should be five-letter words")
    time.sleep(0.5)
    print(" • All of your inputs are case-insensitive")
    time.sleep(0.5)
    print(" • The color of the letters will change as follows")
    time.sleep(0.5)
    print("   ↳ A", Fore.WHITE + "WHITE", Fore.RESET + "letter means it is not in the word in any spot")
    time.sleep(0.5)
    print("   ↳ A", Fore.YELLOW + "YELLOW", Fore.RESET + "letter means it is in the word, but in the wrong spot")
    time.sleep(0.5)
    print("   ↳ A", Fore.GREEN + "GREEN", Fore.RESET + "letter means both the letter and spot are correct")
    time.sleep(3)
    global categories
    categories = ["FRUITS", "COLORS", "ANIMALS", "RANDOM"]
    while True:
        print("Categories: FRUITS, COLORS, ANIMALS, RANDOM")
        category = input("Choose a category: ").strip()
        if category.upper() in categories:
            return category.upper()
        else:
            print("Invalid category")
            time.sleep(1)
            continue

def choose_wordle(category):
    if category == "RANDOM":
        category = random.choice(categories)
    with open(category + ".txt", "r") as file:
        lines = file.readlines()
        wordle = random.choice(lines)
    return wordle

def check_letter(guess, a):
    if guess[a] == wordle[a]:
        return Fore.GREEN + f'{guess[a]}'
    else:
        if guess[a] in wordle:
            return Fore.YELLOW + f'{guess[a]}'
        else:
            return Fore.WHITE + f'{guess[a]}'

main()
