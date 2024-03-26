import os
from tqdm import tqdm
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore
import json
import asyncio

async def username_search(usernames):
    os.environ['WDM_LOG_LEVEL'] = '0'
    option = webdriver.ChromeOptions()
    option.add_argument('--headless=new')
    option.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=option)
    os.system("cls" or "clear")
    driver.get("https://whatsmyname.app/")
    driver.find_element(by=By.XPATH, value='//*[@id="targetUsername"]').send_keys(usernames)
    await asyncio.sleep(0.50)
    driver.find_element(by=By.XPATH, value="//*[@id='main']/div/div/div[3]/div[2]/div/div[1]/button").click()
    await asyncio.sleep(0.50)
    driver.find_element(by=By.XPATH, value='//*[@id="filters"]/a[2]').click()
    await asyncio.sleep(0.50)
    driver.find_element(by=By.XPATH, value="//button[@class='btn btn-success']").click()
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


                            [Made by 923974093915717632] | Vers: 1.3 | github: lookthis664{Fore.RESET}
''')

    print(f"""
{Fore.YELLOW}[?]=> Searching for the username:{Fore.RESET} {usernames}
""")
    duration = 625
    start_time = time.time()
    end_time = start_time + duration

    for _ in tqdm(range(duration), desc="Processed: ", unit="sec"):
        progress = random.randint(1, 5)
        time.sleep(0.02)
    links = driver.find_elements(by=By.XPATH, value="//table[@id='collectiontable']/tbody//tr//following::td[4]/a")
    #category1 = driver.find_elements(by=By.XPATH, value="//table[@id='collectiontable']//td[3]")

    href1 = []
    x1 = []
    e = 0
    for index, row2 in enumerate(links):
        if index < len(links):
            href = links[index].get_attribute("href")
            href1.append(href)
            e += 1
    x = {
        "link": href1
    }
    x1.append(x)
    if e != 0:
        nom_fichier_json = usernames+"_osint_temp"+".json" 
        repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
        # Save the data to a JSON file with indentation
        with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
            json.dump(x1, json_file, indent=4)
        os.system("cls" or "clear")
        print(f"""{Fore.YELLOW}[?]=> Link found:{Fore.RED} {e}{Fore.RESET}""")

    elif e == 0:
        os.system("cls" or "clear")
        print(f"""{Fore.RED}[?]=> Unable to find any link !{Fore.RED}{Fore.RESET}""")