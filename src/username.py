import os
from tqdm import tqdm
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from colorama import Fore
import json

async def username_search(usernames):
    os.environ['WDM_LOG_LEVEL'] = '0'
    option = webdriver.ChromeOptions()
    option.add_argument('--headless=new')
    option.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=option)
    wait = WebDriverWait(driver, 160)
    os.system("cls" or "clear")
    driver.get("https://instantusername.com/")
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/button[1]/p"))).click()
    send_leys_targetUsername = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/astro-island/div/div[1]/form/div/input'))).send_keys(usernames)
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/astro-island/div/div[2]/div[3]/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/astro-island/div/div[2]/div[4]/button'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/astro-island/div/div[2]/div[7]/button"))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/astro-island/div/div[2]/div[10]/button"))).click()
    driver.execute_script("window.scrollBy(0, -document.body.scrollHeight)")
    time.sleep(5)
    driver.execute_script("""
        var scrollHeight = document.documentElement.scrollHeight;
        window.scrollTo({
            top: scrollHeight,
            behavior: 'smooth'
        });
    """)

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


                            [Made by 923974093915717632] | Vers: 1.8 | github: lookthis664{Fore.RESET}
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
    links = driver.find_elements(by=By.CSS_SELECTOR, value="div._container_tzb67_1._taken_tzb67_36._disabled_tzb67_68 a")

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
