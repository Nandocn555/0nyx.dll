import os
import time
import shutil

# --- CONFIGURACIÓN DE COLOR ---
# CAMBIO: Usaremos el color verde (32m) como color principal de la tool
COLOR_CODE = '\033[32m'
RESET_CODE = '\033[0m'

def get_terminal_size():
    return shutil.get_terminal_size()

def center_text(text, width):
    lines = text.splitlines()
    # Usaré 'line.center(width)' para centrar
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
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⠿⠋⢀⣠⣾⠟⢫⣿⣿⣿⣿⣿⣿⣿⡍⠻⣷⣄⡀⠙⠿⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⡿⠛⠁⠀⢸⣿⣿⠋⠀⢸⣿⣿⣿⣿⣿⣿⣿⡗⠀⠙⣿⣿⡇⠀⠈⠛⢿⣦⣄⠀⠀⠀⠀⠀
⢀⠀⣀⣴⣾⠟⠋⠀⠀⠀⠀⢸⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⣿⣿⡇⠀⠀⠀⠀⠙⠻⣷⣦⣀⠀⣀
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
    
    for _ in range(5):
        os.system('cls' if os.name == 'nt' else 'clear')
        # CAMBIO: Usar COLOR_CODE (verde)
        print(f"{COLOR_CODE}{centered_text}{RESET_CODE}")
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(0.5)

# La función center_text estaba duplicada, la he quitado de aquí para evitar redundancia

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
                                0 N Y X . D L L   v1.0.4
                       ════════════════════════════════════════
                                   By Nandocn.555
                                        
      ╔══════════════════════════════════════════════════════════════════════════════════╗
      ║ 0nyx.dll Tool | v1.0.4 | By Nandocn.555                [ - ] [ □ ] [ X ]         ║
      ║══════════════════════════════════════════════════════════════════════════════════║
      ║                                                                                  ║
      ║ [21] > Previous Page (2/2)           [31] >                                      ║
      ║ [22] >                               [32] >                                      ║
      ║ [23] >                               [33] >                                      ║
      ║ [24] >                               [34] >                                      ║
      ║ [25] >                               [35] >                                      ║
      ║ [26] >                               [36] >                                      ║
      ║ [27] >                               [37] >                                      ║
      ║ [28] >                               [38] >                                      ║
      ║ [29] >                               [39] >                                      ║
      ║ [30] >                               [40] >                                      ║
      ║                                                                                  ║
      ╚══════════════════════════════════════════════════════════════════════════════════╝
"""



    
    while True:
        # CAMBIO: Usar COLOR_CODE (verde) y cerrar la cadena con RESET_CODE
        print(f"{COLOR_CODE}{menu}{RESET_CODE}") 

        try:
            choice = int(input(f"{COLOR_CODE}Choice >> {RESET_CODE}"))
            def choice_script(choice):
                if choice == 0:
                    os.system('python ./tools/discord.py')
                elif choice == 21:
                    # NOTA: Ejecutar cyb3rtech.py aquí puede causar un bucle si este es cyb3rtech.py
                    # Asumo que quieres ir a la página anterior, que es el menú principal.
                    os.system('python ./cyb3rtech.py')
                elif choice == 22:
                    os.system('python ./nextpage.py')
                elif choice == 23:
                    os.system('python ./nextpage.py')
                elif choice == 24:
                    os.system('python ./nextpage.py')
                elif choice == 25:
                    os.system('python ./nextpage.py')
                elif choice == 26:
                    os.system('python ./nextpage.py')
                elif choice == 27:
                    os.system('python ./nextpage.py')
                elif choice == 28:
                    os.system('python ./nextpage.py')
                elif choice == 29:
                    os.system('python ./nextpage.py')
                elif choice == 30:
                    os.system('python ./nextpage.py')
                elif choice == 31:
                    os.system('python ./nextpage.py')
                elif choice == 32:
                    os.system('python ./nextpage.py')
                elif choice == 33:
                    os.system('python ./nextpage.py')
                elif choice == 34:
                    os.system('python ./nextpage.py')
                elif choice == 35:
                    os.system('python ./nextpage.py')
                elif choice == 36:
                    os.system('python ./nextpage.py')
                elif choice == 37:
                    os.system('python ./nextpage.py')
                elif choice == 38:
                    os.system('python ./nextpage.py')
                elif choice == 39:
                    os.system('python ./nextpage.py')
                elif choice == 40:
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