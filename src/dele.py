import os
from colorama import Fore
import time

async def delete_fichiertemp(usernames):
    os.system("cls" or "clear")
    print(f"""{Fore.YELLOW}[?]=> Deleting temporary files...{Fore.RESET}""")
    time.sleep(0.50)
    nom_repetoire = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    try:
        os.remove(os.path.join(nom_repetoire, '{}_googlesearch_temp.json'.format(usernames)))
    except:
        print(f"""{Fore.RED}[?]=> Error/File not found ! {Fore.RESET}({usernames}_googlesearch_temp.json)""") 
    try:
        os.remove(os.path.join(nom_repetoire, '{}_osint_temp.json'.format(usernames)))
    except:
        print(f"""{Fore.RED}[?]=> Error/File not found ! {Fore.RESET}({usernames}_osint_temp.json)""")
    print(f"""{Fore.YELLOW}
[?]=> End of the program.{Fore.RESET}""")