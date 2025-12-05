import os

menu = "\033[32m" + """
         ██▀███   ▄▄▄       ██▓▓█████▄
         ▓██ ▒ ██▒▒████▄    ▓██▒▒██▀ ██▌
         ▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒░██   █▌
         ▒██▀▀█▄  ░██▄▄▄▄██ ░██░░▓█▄   ▌
         ░██▓ ▒██▒ ▓█   ▓██▒░██░░▒████▓
         ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓   ▒▒▓  ▒
           ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░ ░ ▒  ▒
           ░░   ░   ░   ▒    ▒ ░ ░ ░  ░
               ░           ░  ░ ░     ░
                        ░

                >>  0 N Y X   R A I D  <<
""" + "\033[0m"

menu2 = "\033[32m" + """
     ┌───────────────────────────┐
     │        RAID OPTIONS       │
     └───────────────────────────┘

  [0] ► Back to Main Menu
  [1] ► Bot Raid 
  [2] ► SelfBot Raid
""" + "\033[0m"



def show_menu():
    print(f"\033[32m{menu}")
    print(f"\033[32m{menu2}\033[0m")
    
def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        show_menu()
        try:
            choice = int(input('\033[32m> Choose an option: \033[0m'))
            if choice == 0:
                os.system('python cyb3rtech.py')
                break
            elif choice == 1:
                os.system('python ./tools/bot_raid.py')
            elif choice == 2:
                os.system('python ./tools/self_raid.py')                
            else:
                print("\033[32m[!]\033[0m Invalid choice \033[32m[!]\033[0m")
        except ValueError:
            print("\033[32mPlease enter a valid number\033[0m")
        input("\n\033[32mPress Enter to return to the menu...\033[0m")

if __name__ == "__main__":
    main()
