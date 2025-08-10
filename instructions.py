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
    print("   ↳ A", Fore.WHITE + "WHITE", "letter means it is not in the word in any spot")
    time.sleep(0.5)
    print("   ↳ A", Fore.YELLOW + "YELLOW", "letter means it is in the word, but in the wrong spot")
    time.sleep(0.5)
    print("   ↳ A", Fore.GREEN + "GREEN", "letter means both the letter and spot are correct")
    time.sleep(0.5)
    print(" • Green mode - The feedback is limited, only green letter will be displayed")
    time.sleep(0.5)
    print(" • Strict mode - You cannot use letters that you already know are not in the word")
    time.sleep(2)

def options():
    list = ["1", "2", "3", "4", "5", "6"]
    N = 6 
    gm = False
    sm = False
    while True:
        print("--- WORDLE ---")
        print("")
        print("1) Original WORDLE")
        print("2) Thematic mode")
        print("3) Custom attempts - Number of attempts:", N)
        print("4) Green mode -", gm)
        print("5) Strict mode -", sm)        
        print("6) How to play?")
        print("")
        option = input("Select an option (1-6): ").strip()
        if option in list:
            if option == "6":
                rules()
                continue
            elif option == "5":
                if sm == False:
                    sm = True
                else:
                    sm = False
            elif option == "4":
                if gm == False:
                    gm = True
                else:
                    gm = False
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
                return option, int(N), gm, sm
        else:
            print("That's not a valid option!")
            time.sleep(1)
            continue
