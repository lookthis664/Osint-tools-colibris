import os 
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore
from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import requests
import asyncio

async def email_search(mails):
    os.environ['WDM_LOG_LEVEL'] = '0'
    option = webdriver.ChromeOptions()
    option.headless = True
    option.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=option)
    os.system("cls" or "clear")
    driver.get("https://haveibeenpwned.com/")
    driver.find_element(by=By.XPATH, value='//*[@id="Account"]').send_keys(mails)
    await asyncio.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="searchPwnage"]').click()
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


                            [Made by 923974093915717632] | Vers: 2.1.4 | github: lookthis664{Fore.RESET}
''')

    with open(r"config\webhook.txt", "r", encoding='utf-8') as file:
        wbh = file.read()
    print(f"""{Fore.RED}Webhook: {Fore.RESET}{wbh[:5]}(...){wbh[-5:]}
{Fore.YELLOW}[?]=> Searching for the email:{Fore.RESET} {mails}
""")
    duration = 15
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
        await asyncio.sleep(0.4)
    links = driver.find_elements(By.XPATH, "//*[@id='pwnedSites']//div[2]//span")
    print("\n")

    s = [link.text.replace(":", "") for link in links]
    href1 = [link.text.replace(":", "") for link in links]
    e = 0
    for item in s:
        e += 1
    result_dict = {
        "website_breached": href1
    }

    nom_fichier_json = mails + "_breached" + ".json"
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)

    # Sauvegarder les données dans un fichier JSON avec indentation
    with open(chemin_du_fichier, 'w', encoding='utf-8') as json_file:
        json.dump(result_dict, json_file, indent=4)

    with open(r'config\webhook.txt', 'r', encoding='utf-8') as file:
        wbh = file.read().strip()
    
    if e != 0:
        webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
        embed = DiscordEmbed(title="Website", description=f"I found {e} website", color="e003f8")
        embed.set_author(name=mails, icon_url="https://media.tenor.com/1OrBi43clj4AAAAM/troll-face-troll.gif")
        embed.set_footer(text="Win")
        embed.set_timestamp()
        for i in range(e):
            field_value = f"{s[i]}.com" # enlever le ":"
            embed.add_embed_field(name=f"---------", value=field_value, inline=False)  # Ajoutez le nom du champ ici
    else:
        webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
        embed = DiscordEmbed(title="Bruh", description=f"I found no website", color="e003f8")
        embed.set_author(name=mails, icon_url="https://media.tenor.com/cA-veoQn3RIAAAAM/troll-sad.gif")
        embed.set_footer(text="Not today")
        embed.set_timestamp()
    
    os.system("cls" or "clear")
    r = requests.post(wbh)
    if r.status_code != 404:
        webhook.add_embed(embed)
        response = webhook.execute()
    else:
        print(f'{Fore.RED}[?]=> Webhook isn\'t working: {r.text}{Fore.RESET}')
    
    print(f"""{Fore.YELLOW}[?]=> Website found:{Fore.RED} {e}{Fore.RESET}""")
    await asyncio.sleep(3.5)
    