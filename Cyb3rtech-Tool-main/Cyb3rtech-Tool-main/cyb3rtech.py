import os
import time
import shutil

# --- CONFIGURACIÓN DE COLOR ---
# \033[32m = Verde
COLOR_CODE = '\033[32m'
RESET_CODE = '\033[0m'

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    centered_lines = [line.center(width) for line in lines]
    return "\n".join(centered_lines)

def blinking():
    text = """
⠀⠀⠀⠀⠀⠀⠀⢀⠆⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡀⠀⠰⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡏⠀⢀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠀⢹⣄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⡟⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⢻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣿⠁⠀⣸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⠀⠈⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⣾⡇⠀⢀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⣿⡇⠀⠀⠀
⠀⠀⠀⣿⣿⠀⠀⣿⣿⣧⣤⣤⣤⡀⠀⣀⠀⠀⣀⠀⢀⣤⣤⣤⣤⣤⣤⣤⣤⣼⣿⣿⠀⠀⣿⣿⠀⠀⠀
⠀⠀⢸⣿⡏⠀⠀⠀⠙⢉⣉⣩⣴⣶⣤⣙⣿⣶⣯⣦⣴⣼⣷⣿⣋⣤⣶⣦⣍⣉⠉⠋⠀⠀⠀⢸⣿⡇⠀⠀
⠀⠀⢿⣿⣷⣤⣶⣶⠿⠿⠛⠋⣉⡉⠙⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡛⠛⢉⣉⠙⠛⠿⠿⣶⣶⣾⣿⡿⠀⠀
⠀⠀⠀⠙⠻⠋⠉⠀⠀⠀⣠⣾⡿⠟⠛⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠛⠻⢿⣷⣄⠀⠀⠀⠉⠙⠟⠋⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣤⣾⠿⠋⢀⣠⣾⠟⢫⣿⣿⣿⣿⣿⣿⣿⡍⠻⣷⣄⡀⠙⠿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⡿⠛⠁⠀⢸⣿⣿⠋⠀⢸⣿⣿⣿⣿⣿⣿⣿⡗⠀⠙⣿⣿⡇⠀⠈⠛⢿⣦⣄⠀⠀⠀⠀⠀
⢀⠀⣀⣴⣾⠟⠋⠀⠀⠀⠀⢸⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠙⠻⣷⣦⣀⠀⣀
⢸⣿⣿⠋⠁⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠈⠙⣿⣿⡟
⢸⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⢹⣿⣿⣿⣿⣿⡏⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡇
⢸⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⢿⣿⣿⡿⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡇
⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀⠀⠈⠿⠿⠁⠀⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀
⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀
⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠃⠀
⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣾⠏⠀⠀
⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠇⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀
⠀⠀⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠸⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠇⠀⠀⠀⠀⠀⠀⠀⡸⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀⠀⠜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
 (loading..)
    """
    terminal_size = get_terminal_size()
    centered_text = center_text(text, terminal_size.columns)
    
    for _ in range(3):
        os.system('cls' if os.name == 'nt' else 'clear')
        # CAMBIO: Color a Verde
        print(f"{COLOR_CODE}{centered_text}{RESET_CODE}")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

# --- BANNER 0NYX.DLL (Estilo Hacker/Glitch) ---
# Hemos eliminado el menu_ascii ya que el banner original era complejo.
# Para mantener la funcionalidad, usaremos 'menu' directamente
# y el banner nuevo se define dentro de la cadena de texto aquí.

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    blinking()
    
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # CAMBIO: Banner y colores actualizados a 0nyx.dll
    menu = f"""
                                        
                        ██████╗ ███╗   ██╗██╗   ██╗██╗
                       ██╔═══██╗████╗  ██║██║   ██║██║
                       ██║   ██║██╔██╗ ██║██║   ██║██║
                       ██║   ██║██║╚██╗██║██║   ██║██║
                       ╚██████╔╝██║ ╚████║╚██████╔╝███████╗
                        ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
                           ░           ░                         
                       ════════════════════════════════════════
                                0 N Y X . D L L   v2.6.0
                       ════════════════════════════════════════
                                   By Nandocn.555
                                        
      ╔══════════════════════════════════════════════════════════════════════════════════╗
      ║ 0nyx.dll Tool | v2.6.0 | By Nandocn.555                [ - ] [ □ ] [ X ]         ║
      ║══════════════════════════════════════════════════════════════════════════════════║
      ║                                                                                  ║
      ║ [1] > Tool Info                 [11] > Discord Token Info                        ║
      ║ [2] > IP Info                   [12] > Discord Token Nuker                       ║
      ║ [3] > DDOS (#soon)              [13] > Discord Token Joiner                      ║
      ║ [4] > Mass Report (#soon)       [14] > Discord Token BruteForce                  ║
      ║ [5] > Phone Number Lookup       [15] > N/A                                       ║
      ║ [6] > Mail Info                 [16] > Discord Token Generator                   ║
      ║ [7] > Username Tracker          [17] > Discord Nitro Generator                   ║
      ║ [8] > SQL Vulnerability         [18] > Discord Server Info                       ║
      ║ [9] > Discord Raid              [19] > Web Cloner (#soon)                        ║
      ║ [10] > Dmall                    [20] > Next Page (1/2) (#soon)                   ║
      ║                                                                                  ║
      ╚══════════════════════════════════════════════════════════════════════════════════╝
"""

    
    while True:
        # CAMBIO: Color a Verde
        print(f"{COLOR_CODE}{menu}{RESET_CODE}")

        try:
            choice = int(input(f"{COLOR_CODE}> Select an option: {RESET_CODE}"))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 1:
                    os.system('python ./tools/tool_info.py')
                elif choice == 2:
                    os.system('python ./tools/geoip.py')
                elif choice == 3:
                    # NOTA: Ejecutar el propio archivo principal aquí puede causar problemas
                    os.system('python ./cyb3rtech.py') 
                elif choice == 4:
                    os.system('python ./cyb3rtech.py')
                elif choice == 5:
                    os.system('python ./tools/phone_number.py')
                elif choice == 6:
                    os.system('python ./tools/mail_info.py')
                elif choice == 7:
                    os.system('python ./tools/username_tracker.py')
                elif choice == 8:
                    os.system('python ./tools/sql_vulnerability.py')
                elif choice == 9:
                    os.system('python ./tools/discord_raid.py')
                elif choice == 10:
                    os.system('python ./tools/dmall.py')
                elif choice == 11:
                    os.system('python ./tools/discord_token_info.py')
                elif choice == 12:
                    os.system('python ./tools/discord_token_nuker.py')
                elif choice == 13:
                    os.system('python ./tools/discord_token_joiner.py')
                elif choice == 14:
                    os.system('python ./tools/discord_token_bruteforce.py')
                elif choice == 15:
                    os.system('python ./cyb3rtech.py')
                elif choice == 16:
                    os.system('python ./cyb3rtech.py')
                elif choice == 17:
                    os.system('python ./tools/discord_nitro_generator.py')
                elif choice == 18:
                    os.system('python ./cyb3rtech.py')
                elif choice == 19:
                    os.system('python ./tools/web_cloner.py')
                elif choice == 20:
                    os.system('python ./nextpage.py')
                else:
                    raise ValueError
            
            choice_script(choice)
            break
        except ValueError:
            # CAMBIO: Usar COLOR_CODE (verde) para el error
            print(f"{COLOR_CODE}[!]{RESET_CODE} Opción inválida. Intenta con un número de la lista.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            
if __name__ == "__main__":
    main()