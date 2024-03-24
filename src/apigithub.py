import os
from tqdm import tqdm
import random
import time
from requests import get
import requests
import json
from colorama import Fore

async def username_search(usernames):
    os.system("cls" or "clear")
    r=requests.get(
        f"https://api.github.com/users/{usernames}/events/public")
    if r.status_code == 200:
        jsonn = json.loads(r.text)

        print(f'''{Fore.LIGHTMAGENTA_EX}
                                                ,_
                                                 :`.            .--._
                                                  `.`-.        /  ',-""""'
                                                    `. ``~-._.'_."/
                                                      `~-._ .` `~;
                                                           ;.    /
                                                          /     /
                                                     ,_.-';_,.'`
                                                      `"-;`/
                                                        ,'`colibris


                            [Made by 923974093915717632] | Vers: 1.1 | github: lookthis664{Fore.RESET}
''')
        print(f"""{Fore.YELLOW}[?]=> Searching for the username in github:{Fore.RESET} {usernames}\n""")
        duration = 20
        start_time = time.time()
        end_time = start_time + duration

        for _ in tqdm(range(duration), desc="Processed: ", unit="sec"):
            progress = random.randint(1, 5)
            time.sleep(0.03)
        os.system("cls" or "clear")
        user_idd = []
        content = []
        e = 0
        try:
            for v in jsonn:
                if 'payload' in v and 'commits' in v['payload'] and v['payload']['commits']:
                    user_idd.append(v["actor"]["login"])
                    content.append(v["payload"]["commits"][0]["author"]["email"])
                    content.append(v["payload"]["commits"][0]["author"]["name"])
                    e += 1
            x = {
                'User': user_idd,
                'Mail + name': content
            }
            nom_fichier_json = usernames + "_github" + ".json"
            repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
            chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
            with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
                json.dump(x, json_file, indent=4)
            print(f"""{Fore.YELLOW}[?]=> Github found !{Fore.RESET}""")

        except:
            print(f"{Fore.RED}[?]=> No data found for this username{Fore.RESET}")

    elif r.status_code == 404:
        print(f"{Fore.RED}[?]=> Github not found !{Fore.RED}{Fore.RESET}")
    else:
        print(f"{Fore.RED}[?]=> An error occurred: {r.status_code} {r.text}{Fore.RESET}")
