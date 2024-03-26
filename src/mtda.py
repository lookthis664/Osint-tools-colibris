from requests import get
from bs4 import BeautifulSoup
import json
import os
from tqdm import tqdm
from colorama import Fore
import time
import random

async def meta_donnee(url):
    response = get(url)
    metadata = {}
    try:
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            metadata['title'] = soup.title.text.strip() if soup.title else "None"
            metadata['description'] = soup.find("meta", attrs={"name": "description"})['content'].strip() if soup.find("meta", attrs={"name": "description"}) else "None"
    except Exception as e:
        print(f"{Fore.RED}[?]=> Error fetching metadata for the link: {Fore.RESET}{url}")
    return metadata

async def withopen(lien_de_passage):
    #print(lien_de_passage) my debug
    with open(lien_de_passage, 'r+') as file:
        data = file.read()
        a = json.loads(data)

    for lienn in a:
        try:
            links = lienn.get('link', [])
            for link in links:
                url = link
                metadata = await meta_donnee(url)
                os.system("cls" or "clear")
                print(f"""{Fore.YELLOW}
[?]=> Collects metadata from links...{Fore.RESET}
{link}""")
                duration = 1
                start_time = time.time()
                end_time = start_time + duration

                for _ in tqdm(range(duration), desc="Processed: ", unit="sec"):
                    progress = random.randint(1, 5)
                    time.sleep(0.5)
                x1 = []
                x = { 
                'Metadata: ' : metadata,
                'link: ' : link
                }
                x1.append(x)
                nom_fichier_json = "metadata_&_link_found"+".json" 
                repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
                chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
                with open(chemin_du_fichier, 'a', encoding='utf-8') as json_file:
                    json.dump(x1, json_file, indent=4)
        except:
            os.system("cls" or "clear")
            print(f"""{Fore.RED}[?]=> Can't get metadata from: {Fore.RESET}{link}""")
async def jsonfichier(usernames):
        repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        try:
            await withopen(os.path.join(repertoire_parent, '{}_googlesearch_temp.json'.format(usernames)))
        except:
            print(f"""{Fore.RED}[?]=> Error/no links found, for the '{usernames}_googlesearch_temp.json' !{Fore.RESET}""")

        try:
            await withopen(os.path.join(repertoire_parent, '{}_osint_temp.json'.format(usernames)))
        except:
            print(f"""{Fore.RED}[?]=> Error/no links found, for the '{usernames}_osint_temp.json' !{Fore.RESET}""")