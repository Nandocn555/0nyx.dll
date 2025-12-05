import pywebcopy
from pywebcopy import save_website
import os
import time

menu = """
         █     █░▓█████  ▄▄▄▄       ▄████▄   ██▓     ▒█████   ███▄    █ ▓█████  ██▀███
        ▓█░ █ ░█░▓█   ▀ ▓█████▄    ▒██▀ ▀█  ▓██▒    ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
        ▒█░ █ ░█ ▒███   ▒██▒ ▄██   ▒▓█    ▄ ▒██░    ▒██░  ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
        ░█░ █ ░█ ▒▓█  ▄ ▒██░█▀     ▒▓▓▄ ▄██▒▒██░    ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄
        ░░██▒██▓ ░▒████▒░▓█  ▀█▓   ▒ ▓███▀ ░░██████▒░ ████▓▒░▒██░   ▓██░░▒████▒░██▓ ▒██▒
        ░ ▓░▒ ▒  ░░ ▒░ ░░▒▓███▀▒   ░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
          ▒ ░ ░   ░ ░  ░▒░▒   ░      ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
          ░   ░     ░    ░    ░    ░          ░ ░   ░ ░ ░ ▒     ░   ░ ░    ░     ░░   ░
              ░       ░  ░ ░         ░ ░          ░  ░    ░ ░           ░    ░  ░   ░
                      ░    ░
                                >>  0 N Y X   C L O N E R <<
                      """
menu2 = """
     ┌───────────────────────────┐
     │    WebCloner Options      │
     └───────────────────────────┘

  [0] ► Back to Menu
  [1] ► Clone website
"""

def show_menu():
    print(f"\033[32m{menu}\033[0m")
    print(f"\033[32m{menu2}\033[0m")

def clone():
    print("\033[32mCreation in progres... (redirection)\033[0m")
    time.sleep(2)
    os.system('python cyb3rtech.py')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('\033[32m> Select an option: \033[0m'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            elif choice == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\033[32m{menu}\033[0m")
                clone()
            else:
                print("\033[32m[!]\033[0m Invalid choice \033[32m[!]\033[0m")
                input("\n\033[32mPress Enter to return to the menu...\033[0m")
        except ValueError:
            print("\033[32mPlease enter a valid number\033[0m")
            input("\n\033[32mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()
