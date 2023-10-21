import requests
from colorama import Fore
import time 
import random 
from discord_webhook import DiscordWebhook, DiscordEmbed
import os
import json
import asyncio


async def pastebin_dump(mails):
    response = requests.get("https://psbdmp.ws/api/v3/search/{}".format(mails)).json()
    print(f"{Fore.YELLOW}[?]=> Searching for pastebin dump...{Fore.RESET}")
    duration = 7
    start_time = time.time()
    end_time = start_time + duration
    progress = 0
    while time.time() < end_time:
        random_progress = random.randint(1, 5)
        progress += random_progress
        if progress > 100:
            progress = 100
        bar = f"{Fore.YELLOW}[" + "=" * (progress // 3) + " " * ((100 - progress) // 3) + f"]{Fore.RESET}"
        print(f"{Fore.RED}\rLoading: {bar} {progress}%", end="", flush=True)
        await asyncio.sleep(0.17)

    os.system('cls' or 'clear')
    
    if response and isinstance(response, list):
        e=0
        id=[]
        href1 = ""
        for result in response:
            ids = result.get('id')
            id.append(ids)
            href1 += ids
            e+=1
        
            x = {
            "pastebin_dump_link": f"https://psbdmp.ws/api/v3/dump/{href1}"
            }
            nom_fichier_json = mails+"_pastedump"+".json" 
            repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
            chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
            # Save the data to a JSON file with indentation
            with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
                json.dump(x, json_file, indent=4)
            href1 = ""

        with open(r'config\webhook.txt', 'r', encoding='utf-8') as file:
            wbh = file.read().strip()


        if e !=0:
            webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
            embed = DiscordEmbed(title="Pastebin", description=f"I found {e} pastebin", color="e003f8")
            embed.set_author(name=mails, icon_url="https://media.tenor.com/1OrBi43clj4AAAAM/troll-face-troll.gif")
            embed.set_footer(text="Win")
            embed.set_timestamp()
            for i in range(e):
                field_value = f"https://psbdmp.ws/api/v3/dump/{id[i]}"
                embed.add_embed_field(name=f"---------", value=field_value, inline=False)  # Ajoutez le nom du champ ici

        else:
            print(f"{Fore.RED}[?]=> Request failed!{Fore.RESET}")
            webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
            embed = DiscordEmbed(title="Bruh", description=f"No pastebin dump!", color="e003f8")
            embed.set_author(name=mails, icon_url="https://media.tenor.com/cA-veoQn3RIAAAAM/troll-sad.gif")
            embed.set_footer(text="Not today")
            embed.set_timestamp()

        r = requests.post(wbh)
        if r.status_code != 404:
            webhook.add_embed(embed)
            response = webhook.execute()
        else:
            print(f'{Fore.RED}[?]=> Webhook isn\'t working: {r.text}{Fore.RESET}')

        print(f"""{Fore.YELLOW}[?]=> Pastebin found:{Fore.RED} {e}{Fore.RESET}""")
