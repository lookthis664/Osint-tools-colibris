from requests import get
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json
import os
from colorama import Fore, init
import asyncio
import time

init(autoreset=True)


async def meta_donnee(url):
    metadata = {}
    try:
        response = get(url)
        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, "html.parser")
            metadata['title'] = soup.title.text.strip() if soup.title else "None"
            metadata['description'] = soup.find("meta", attrs={"name": "description"})['content'].strip() if soup.find("meta", attrs={"name": "description"}) else "None"
            return metadata
    except RequestException as e:
        os.system("cls" or "clear")
        print(f"{Fore.RED}[?]=> Error fetching metadata for the link: {Fore.RESET}{url}")
        time.sleep(1)
    except Exception as e:
        print(f"{Fore.RED}[?]=> Unexpected error: {e} for the link: {Fore.RESET}{url}")
    return metadata


async def withopen(lien_de_passage):
    try:
        with open(lien_de_passage, 'r+') as file:
            data = file.read()
            a = json.loads(data)
    except Exception as e:
        print(f"{Fore.RED}[?]=> Error reading file: {e}{Fore.RESET}")
        return

    vrais2vrais = []
    for lienn in a:
        links = lienn.get('link', [])
        for link in links:
            try:
                metadata = await meta_donnee(link)
                os.system("cls" or "clear")
                print(f"""{Fore.YELLOW}
[?]=> Collects metadata from links...{Fore.RESET}
{link}""")
                vrais2vrais.append({
                    'Metadata': metadata,
                    'link': link
                })
            except Exception as e:
                print(f"""{Fore.RED}[?]=> Error processing link: {e}{Fore.RESET}""")

    try:
        nom_fichier_json = "metadata_&_link_found.json"
        repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
        chemin_du_fichier = os.path.join(repertoire_parent, nom_fichier_json)
        with open(chemin_du_fichier, 'a+', encoding='utf-8') as json_file:
            json.dump(vrais2vrais, json_file, indent=4)
    except Exception as e:
        print(f"""{Fore.RED}[?]=> Error writing JSON file: {e}{Fore.RESET}""")


async def jsonfichier(usernames):
    repertoire_parent = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    try:
        await withopen(os.path.join(repertoire_parent, '{}_osint_temp.json'.format(usernames)))
    except Exception as e:
        print(f"""{Fore.RED}[?]=> {e}, for the '{usernames}_osint_temp.json' !{Fore.RESET}""")