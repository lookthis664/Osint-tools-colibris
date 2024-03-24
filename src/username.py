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


                            [Made by 923974093915717632] | Vers: 1.1 | github: lookthis664{Fore.RESET}
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
    category1 = driver.find_elements(by=By.XPATH, value="//table[@id='collectiontable']//td[3]")

    href1 = []
    row3 = []
    e = 0
    for index, row2 in enumerate(category1):
        if index < len(links):
            href = links[index].get_attribute("href")
            href1.append(href)
            row3.append(row2.text)
            e += 1
            x = {
                "link": href1,
                "category": row3
            }
        nom_fichier_json = usernames+"_osint"+".json" 
        repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
        # Save the data to a JSON file with indentation
        with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
            json.dump(x, json_file, indent=4)
        href1.clear()
        row3.clear()
    os.system("cls" or "clear")
    print(f"""{Fore.YELLOW}[?]=> Link found:{Fore.RED} {e}{Fore.RESET}""")