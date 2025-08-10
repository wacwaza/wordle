from colorama import Fore, init
from instructions import options 
import time, random
init(autoreset=True)

def main():
    number, N, gm, sm = options()
    if number == "1":
        original_wordle(att=N, greenmode=gm, strict=sm)
    elif number == "2":
        txt = choose_txt()
        original_wordle(N, txt, gm, sm)

def original_wordle(att=6, txt="possible-answers.txt", greenmode=False, strict=False):
    wordle = choose_wordle(txt).rstrip().upper()
    global l_y
    l_y = []
    attempts = 0
    while attempts < att:
        left = att - attempts
        tries = "tries"
        if left == 1:
            tries = "try"
        guess = input(f"{left} {tries} - Word: ").upper()
        value = False
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
                    if strict:
                        for a in range(5):
                            if guess[a] in l_y:
                                print(f"You can't use the letter {guess[a]}!")
                                value = True
                                time.sleep(0.5)
                                break
                    if not value:
                        for a in range(5):
                            print(f" {check_letter(guess, wordle, a, greenmode, strict)}", end="")
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
    lists = ["FRUITS-VEGGIES", "ANIMALS", "COUNTRIES", "COLORS"]
    while True:
        print("Categories: Fruits-Veggies, Animals, Countries, Colors")
        x = input("Choose a category: ").upper()
        if x in lists:
            if x == "ANIMALS":
                return "animals-list.txt"
            elif x == "FRUITS-VEGGIES":
                return "fruit-veggies-list.txt"
            elif x == "COUNTRIES":
                return "countries-list.txt"
            elif x == "COLORS":
                return "colors.txt"
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

def check_letter(guess, wordle, a, greenmode, strict):
    if guess[a] == wordle[a]:
        return Fore.GREEN + f'{guess[a]}'
    else:
        if greenmode:
            if strict:
                l_y.append(guess[a])
            return Fore.WHITE + f'{guess[a]}'
        else:            
            if guess[a] in wordle:
                return Fore.YELLOW + f'{guess[a]}'
            else:
                if strict:
                    l_y.append(guess[a])
                return Fore.WHITE + f'{guess[a]}'

main()
