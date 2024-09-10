import json
import os
from colorama import Fore
import time

async def delete_fichiertemp(usernames):
    os.system("cls" or "clear")
    print(f"""{Fore.YELLOW}[?]=> Deleting temporary files...{Fore.RESET}""")
    time.sleep(0.50)
    nom_repetoire = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    try:
        os.remove(os.path.join(nom_repetoire, '{}_osint_temp.json'.format(usernames)))
    except:
        print(f"""{Fore.RED}[?]=> Error/File not found ! {Fore.RESET}({usernames}_osint_temp.json)""")
    time.sleep(1.3)
    try:
        with open("metadata_&_link_found.json", 'r+') as file:
            data = json.load(file)
        filtered_data = [entry for entry in data if entry.get('Metadata')]
        if len(filtered_data) != len(data):
            print(f"{Fore.YELLOW}[?]=> Removing entries with empty metadata...{Fore.RESET}")
            with open("metadata_&_link_found.json", 'w', encoding='utf-8') as file:
                json.dump(filtered_data, file, indent=4)

        print(f"{Fore.GREEN}[?]=> Cleaned metadata file successfully.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}[?]=> Error processing the file: {e}{Fore.RESET}")