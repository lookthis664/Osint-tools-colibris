from googlesearch import search
from tqdm import tqdm
import os
import time
from colorama import Fore
import random
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

async def gs_search(usernames):
    os.environ['WDM_LOG_LEVEL'] = '0'
    option = webdriver.ChromeOptions()
    option.add_argument('--headless=new')
    option.add_argument('--log-level=1')
    driver = webdriver.Chrome(options=option)
    os.system("cls" or "clear")
    driver.get("https://www.google.com/")
    try:
       click_L2AGLb = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="L2AGLb"]/div'))).click()
    except:
        print("Cookie not requested")
    driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]').send_keys(usernames)
    driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]').send_keys(Keys.ENTER)
    print(f"""{Fore.YELLOW}[?]=> Searching in google...{Fore.RESET}""")
    duration = 10
    start_time = time.time()
    end_time = start_time + duration

    for _ in tqdm(range(duration), desc="Processed: ", unit="sec"):
        progress = random.randint(1, 5)
        time.sleep(0.2)
    liens = driver.find_elements(by=By.XPATH, value="//*[@id='rcnt']//span/a")
 
    c = []
    e=0
    tab = []
    for result in liens:
        if usernames in result.text:
            results = result.get_attribute("href")
            c.append(results)
            e+=1
    x = {
        "link": c
    }
    tab.append(x)
    if e != 0:
        nom_fichier_json = usernames+"_googlesearch_temp"+".json" 
        repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
        # Save the data to a JSON file with indentation
        with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
            json.dump(tab, json_file, indent=4)
        os.system("cls" or "clear")
        print(f"""{Fore.YELLOW}[?]=> Link found in google search:{Fore.RED} {e}{Fore.RESET}""")
    elif e == 0:
        os.system("cls" or "clear")
        print(f"""{Fore.RED}[?]=> Unable to find any link on Google!{Fore.RED}{Fore.RESET}""")