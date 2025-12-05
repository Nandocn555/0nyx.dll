import os
import webbrowser
import time

menu = """
             ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄
             ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌
             ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌
             ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌
             ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓
             ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒
             ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒
             ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░
             ░     ░        ░  ░ ░          ░ ░     ░        ░
             ░                   ░
"""
menu2 = """
[0] Back to main
"""

def show_menu():
    print(f"\033[32m{menu}")
    print(f"{menu2}")

time.sleep(1)
webbrowser.open('https://discord.gg/mP6NvAgF2q')

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('\033[32m> Select an option: '))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            else:
                print("\033[32m[!] >\033[0m Invalid choice \033[32m< [!]\033[0m")
        except ValueError:
            print("\033[32m[!] Please enter a valid number\033[0m")
        input("\n\033[32mPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()
