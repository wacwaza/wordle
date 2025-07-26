from colorama import Fore, init
from instructions import options 
import time, random
init(autoreset=True)

def main():
    number, N = options()
    if number == "1":
        original_wordle(att=N)
    elif number == "2":
        txt = choose_txt()
        original_wordle(N, txt)

def original_wordle(att=6, txt="possible-answers.txt"):
    global wordle
    wordle = choose_wordle(txt).rstrip().upper()
    attempts = 0
    while attempts < att:
        guess = input("Word: ").upper()
        if len(guess) != 5:
            print("Not a five-letter word! Try again.")
            continue
        else:
            if guess == wordle:
                for a in wordle:
                    print(Fore.GREEN + f" {a}", end="")
                    time.sleep(0.5)
                print() 
                print("You guessed the word!")
                break
            else:
                if check_valid_guess(guess):
                    for a in range(5):
                        print(f" {check_letter(guess, a)}", end="")
                        time.sleep(0.5)
                    attempts += 1
                    print()
                    if attempts == att:
                        print("You lost, the word was", Fore.GREEN + wordle)
                else:
                    print("Not a valid word!")

def choose_wordle(txt):
    with open(txt, "r") as file:
        lines = file.readlines()
    wordle = random.choice(lines)
    return wordle

def choose_txt():
    lists = ["FRUITS-VEGGIES", "ANIMALS", "COUNTRIES"]
    while True:
        print("Categories: Fruits-Veggies, Animals, Countries")
        x = input("Choose a category: ").upper()
        if x in lists:
            if x == "ANIMALS":
                return "animals-list.txt"
            elif x == "FRUITS-VEGGIES":
                return "fruit-veggies-list.txt"
            elif x == "COUNTRIES":
                return "countries-list.txt"
        else:
            continue

def check_valid_guess(guess):
    with open("valid-wordle-words.txt", "r") as file:
        lines = file.readlines()    
        for line in lines:
            if guess.lower() == line.rstrip():
                return True
            else:
                continue

def check_letter(guess, a):
    if guess[a] == wordle[a]:
        return Fore.GREEN + f'{guess[a]}'
    else:
        if guess[a] in wordle:
            return Fore.YELLOW + f'{guess[a]}'
        else:
            return Fore.WHITE + f'{guess[a]}'

main()
