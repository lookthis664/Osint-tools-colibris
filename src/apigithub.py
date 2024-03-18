import os
from tqdm import tqdm
import random
import time
from requests import get
import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore

async def username_search(usernames):
    os.system("cls" or "clear")
    r=requests.get(
        f"https://api.github.com/users/{usernames}/events/public")
    jsonn=json.loads(r.text)
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


                            [Made by 923974093915717632] | Vers: 1.0 | github: lookthis664{Fore.RESET}
''')
    print(f"""{Fore.YELLOW}[?]=> Searching for the username in github:{Fore.RESET} {usernames}
""")
    duration = 20
    start_time = time.time()
    end_time = start_time + duration

    for _ in tqdm(range(duration), desc="Processed: ", unit="sec"):
        progress = random.randint(1, 5)
        time.sleep(0.03)
    os.system("cls" or "clear")
    u = []
    m = []
    n = []
    user_idd = []
    content = []
    e=0
    for v in jsonn:
        if 'message' in v and v['message'] == "Not Found":
            print(f"{Fore.RED}[?]=> Github not found !{Fore.RED}{Fore.RESET}")
            break
        else:
            if 'actor' in v:
                u.append(v['actor']['login'])
                user_idd.append(v['actor']['login'])

            if 'payload' in v and 'commits' in v['payload'] and v['payload']['commits']:
                m.append(v["payload"]["commits"][0]["author"]["email"])
                n.append(v["payload"]["commits"][0]["author"]["name"])
                content.append(v["payload"]["commits"][0]["author"]["email"])
                content.append(v["payload"]["commits"][0]["author"]["name"])
                e+=1    
        
    x = {
        'User': user_idd,
        'Mail + name': content
        }       
    nom_fichier_json = usernames+"_github"+".json" 
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
    with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
        json.dump(x, json_file, indent=4)

    with open(r'config\webhook.txt', 'r', encoding='utf-8') as file:
        wbh = file.read().strip()

    try:
        if e != 0:
            webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
            embed = DiscordEmbed(title="Github information", description=f"I found mail and name from {usernames}", color="e003f8")
            embed.set_author(name=usernames, icon_url="https://media.tenor.com/1OrBi43clj4AAAAM/troll-face-troll.gif")
            embed.set_footer(text="Win")
            embed.set_timestamp()
    
            for i in range(e):
                field_value = f"user: {u[i]}\nmail: {m[i]}\nname: {n[i]}"
                embed.add_embed_field(name=f"---------", value=field_value, inline=False)  # Ajoutez le nom du champ ici
        else:
            webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
            embed = DiscordEmbed(title="Bruh", description=f"Github not found", color="e003f8")
            embed.set_author(name=usernames, icon_url="https://media.tenor.com/cA-veoQn3RIAAAAM/troll-sad.gif")
            embed.set_footer(text="Not today")
            embed.set_timestamp()

        os.system("cls" or "clear")
        r = requests.post(wbh)
        if r.status_code != 404:
            webhook.add_embed(embed)
            response = webhook.execute()
        else:
            print(f'{Fore.RED}[?]=> Webhook isn\'t working: {r.text}{Fore.RESET}')
    except:
        print(f"{Fore.RED}[?]=> No webhook")
    print(f"""{Fore.YELLOW}[?]=> Github found !{Fore.RED}{Fore.RESET}""")