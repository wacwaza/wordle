from colorama import Fore, init
import time, random
init(autoreset=True)

def main():
    rules()
    global wordle
    wordle = choose_wordle().rstrip().upper()
    attempts = 0
    while attempts < 6:
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
                    if attempts == 6:
                        print()
                        print("You lost, the word was", Fore.GREEN + wordle)
                else:
                    print("Not a valid word!")

def rules():
    print("Welcome to WORDLE in python!")
    time.sleep(3)
    print("HOW TO PLAY")
    time.sleep(3)
    print(" • Try to guess the word in 6 tries")
    time.sleep(0.5)
    print(" • All guesses should be valid five-letter words")
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
    time.sleep(0.5)

def choose_wordle():
    with open("possible-answers.txt", "r") as file:
        lines = file.readlines()
    wordle = random.choice(lines)
    return wordle

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
