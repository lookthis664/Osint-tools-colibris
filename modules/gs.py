from googlesearch import search
import os
import time
from colorama import Fore
import random
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

def gs_search(usernames):
    os.environ['WDM_LOG_LEVEL'] = '0'
    option = webdriver.ChromeOptions()
    option.headless = True
    option.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=option)
    os.system("cls" or "clear")
    driver.get("https://www.google.com/")
    driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]').send_keys(usernames)
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]').send_keys(Keys.ENTER)
    time.sleep(1)
    print(f"""{Fore.YELLOW}[?]=> Searching in google...{Fore.RESET}""")
    duration = 3
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
        time.sleep(0.07)
    os.system('cls' or 'clear')
    liens = driver.find_elements(by=By.XPATH, value="//*[@id='rcnt']//span/a")
 
    c = []
    d = []
    e=0
    tab = {}
    for result in liens:
        if usernames in result.text:
            results = result.get_attribute("href")
            c.append(results)
            d.append(results)
            e+=1
            tab["link for {}".format(usernames)] = c
    
    nom_fichier_json = usernames+"_googlesearch"+".json" 
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
    # Save the data to a JSON file with indentation
    with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
        json.dump(tab, json_file, indent=4)
    
    with open(r'config\src\webhook.txt', 'r') as file:
        wbh = file.read().strip()


    if e != 0:
        webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
        embed = DiscordEmbed(title="Google search", description=f"I found {e} link", color="e003f8")
        embed.set_author(name=usernames, icon_url="https://media.tenor.com/1OrBi43clj4AAAAM/troll-face-troll.gif")
        embed.set_footer(text="Win")
        embed.set_timestamp()

        for i in range(e):
            field_value = f"link: {d[i]}"
            embed.add_embed_field(name=f"---------", value=field_value, inline=False)  # Ajoutez le nom du champ ici
    else:
        webhook = DiscordWebhook(url=wbh, username="Colibris | [Made by 923974093915717632]")
        embed = DiscordEmbed(title="Bruh", description=f"I found no link", color="e003f8")
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

    print(f"""{Fore.YELLOW}[?]=> Link found in google search:{Fore.RED} {e}{Fore.RESET}""")