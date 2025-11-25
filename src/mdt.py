import requests
from bs4 import BeautifulSoup
import json
import os

def usernames_folder(usernames):
    with open(f"{usernames}_osint_temp.json", "r+") as f:
        abc = json.load(f)
        tab = []
        for item in abc:
            for item_link in item["link"]:
                url = item_link["Lien: "]
                response = requests.get(url)
                soup = BeautifulSoup(response.text, features="html.parser")

                meta_desc = soup.find('meta', attrs={'name': 'description'})  # UNE seule
                if meta_desc and meta_desc.get('content'):
                    desc = meta_desc.get('content')
                else:
                    desc = "No metadata scrape"

                tab.append({'Lien': url,
                            'Metadata': desc})
        print(tab)
        with open(f"{usernames}_osint_safe.json", "w+") as f:
            json.dump(tab, f, indent=4)
    os.remove(f"{usernames}_osint_temp.json")

