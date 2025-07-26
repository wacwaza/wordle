from colorama import Fore, init
import time
init(autoreset=True)

def rules():    
    print("=== HOW TO PLAY ===")
    time.sleep(2)
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
    time.sleep(2)

def options():
    list = ["1", "2", "3", "4"]
    N = 6 
    while True:
        print("--- WORDLE ---")
        print("")
        print("1) Original WORDLE")
        print("2) Thematic mode", Fore.GREEN + "NEW!")
        print("3) Custom attempts - Number of attempts:", N)
        print("4) How to play?")
        print("")
        option = input("Select an option (1-4): ").strip()
        if option in list:
            if option == "4":
                rules()
                continue
            elif option == "3":
                while True:
                    a = input("Choose the number of tries: ").strip()
                    if a.isdigit():
                        if a == "0":
                            print("That's not a valid number!")
                            time.sleep(1)
                            continue
                        else:
                            N = a
                            break
                    else:
                        print("That's not a valid number!")
                        time.sleep(1)
                        continue
            else:
                return option, int(N)
        else:
            print("That's not a valid option!")
            time.sleep(1)
            continue

