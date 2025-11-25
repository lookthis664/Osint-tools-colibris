from time import sleep
import random
import os
import asyncio
import time
import json
from colorama import Fore, Style
from os import path
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import re
from mdt import usernames_folder

async def username_search_playwright(usernames=None):
    os.system('cls')
    if not usernames:
        print(f"""{Fore.LIGHTRED_EX}   
           [Last UPDATE : 25/11/2025]{Fore.LIGHTMAGENTA_EX} 
    +-------------------+------------------+
    
          {Style.RESET_ALL}Tips: After the search, you 
          can use the .json file to 
          have all the results in a 
          file.{Fore.LIGHTMAGENTA_EX}          
    
           {Fore.LIGHTRED_EX}Made By 923974093915717632{Fore.LIGHTMAGENTA_EX} 
    +-------------------+------------------+""")
        usernames = input(f"""{Fore.YELLOW}\n-> Enter username to search: {Style.RESET_ALL}""")
        print(f"""{Fore.LIGHTYELLOW_EX}\n"L" = 704 webshearch (good for deep searching)
Default = limited to 100 websearch (fastest)""")

        limite_mode = input(f"""{Fore.YELLOW}[?]=> Enter L or return empty:{Style.RESET_ALL} """)
        os.system('cls')

        if limite_mode == "L":
            limite_mode = 704
            print(f"{Fore.LIGHTMAGENTA_EX}\n[INFO]{Style.RESET_ALL} Limite, set to {limite_mode}")

        else:
            limite_mode = 100
            print(f"{Fore.LIGHTMAGENTA_EX}\n[INFO]{Style.RESET_ALL} Limite, set to {limite_mode}")



    print(f"\n{Fore.YELLOW}[?]=> Searching for username: {Fore.WHITE}{usernames}{Style.RESET_ALL}\n")


    NEW_TIMEOUT = 65000

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=['--no-sandbox', '--disable-dev-shm-usage']
            )
            page = await browser.new_page(
                user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
            )
            page.set_default_timeout(NEW_TIMEOUT)

            print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Navigating to site...")
            await page.goto('https://whatsmyname.me/', wait_until="networkidle")


            await page.evaluate('''() => {
                const overlay = document.querySelector('.fc-dialog-overlay');
                if (overlay) overlay.remove();
                const dialog = document.querySelector('.fc-consent-root');
                if (dialog) dialog.remove();
            }''')

            print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Navigated to site. Attempting to close cookie banner...")

            try:
                await page.click('button:has-text("Autoriser")', timeout=5000)
                print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Cookies accepted.")
            except PlaywrightTimeoutError:
                print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Cookie banner not found or already closed (Timeout: 5s).")
            except Exception:
                print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Cookie banner click failed or not present.")


            input_selector = '//*[@id="username-input"]'


            print(f"{Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} Waiting for input field to be visible...")
            await page.wait_for_selector(input_selector, state="visible", timeout=NEW_TIMEOUT)
            await page.fill('#username-input', usernames)
            await asyncio.sleep(0.5)
            await page.click('#search-button')
            os.system('cls')

            a = 0
            f = limite_mode-20
            href1 = []
            time.sleep(10)
            while a != 1:
                text = await page.locator('#social-progress-text').text_content()
                ntm2 = await page.locator('#social-progress-tips').text_content()
                time.sleep(0.5)
                os.system('cls')
                match = re.search(r'(\d+)\s*/\s*(\d+)', text)
                if match:
                    current = int(match.group(1))
                    total = int(match.group(2))
                    print(f"""    
                       {Fore.RED} Target: {usernames}{Fore.LIGHTMAGENTA_EX}   
        +-----------------------+----------------------+
                                                                                                       
                        {Fore.RED}[TESTING WEBSITE]{Style.RESET_ALL}
              {Fore.LIGHTMAGENTA_EX}[INFO]{Style.RESET_ALL} ~/{ntm2} ({current}/{total}){Fore.LIGHTMAGENTA_EX}
                                                                                                                                                                                                                          
              {Fore.YELLOW}         While stop at {limite_mode}
                    {Fore.LIGHTRED_EX}Made By 923974093915717632{Fore.LIGHTMAGENTA_EX} 
        +-----------------------+----------------------+{Style.RESET_ALL}""")
                    if current >= f:
                        print(f"{Fore.LIGHTGREEN_EX}[INFO]{Style.RESET_ALL} Limite atteinte ({current}/{total}), arrÃªt du test.")
                        a = 1
                else:
                    print(f"{Fore.YELLOW}[WARN]{Style.RESET_ALL} Impossible de lire la progression ({text})")


            links_elements = await page.locator('#social-results-list .social-result-item').all()
            if links_elements:
                for link_element in links_elements:
                    await link_element.locator("h3").wait_for(state="visible", timeout=15000)
                    site = await link_element.locator("h3").text_content()
                    href = await link_element.locator("a").get_attribute("href")
                    href1.append({
                        "Site: ": site,
                        'Lien: ': href
                    })

            e = len(href1)
            x1 = [{"link": href1}]

            if e > 0:
                nom_fichier_json = f"{usernames}_osint_temp.json"
                chemin_du_fichier = os.path.join(os.getcwd(), nom_fichier_json)

                existing_data = []
                if path.exists(chemin_du_fichier):
                    try:
                        with open(chemin_du_fichier, 'r') as file:
                            existing_data = json.load(file)
                    except json.JSONDecodeError:
                        print(f"{Fore.YELLOW}[WARN]{Style.RESET_ALL} Existing file is empty or corrupted. Overwriting...")

                users = existing_data + x1

                with open(chemin_du_fichier, 'w', encoding='utf-8') as file:
                    json.dump(users, file, indent=4)

                print(f"\n{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Found {e} links for '{usernames}'.")
                print(f"{Fore.GREEN}[SUCCESS]{Style.RESET_ALL} Links save -> JSON file: {usernames}_osint_safe.json.")


            print(f"\n{Fore.YELLOW}--- Social Media Links Found ({e}) ---{Style.RESET_ALL}")

        if e > 0:
            for href in href1:
                print(f"{Fore.WHITE}{href}{Style.RESET_ALL}")
            usernames_folder(usernames)
        else:
            print(f"{Fore.YELLOW}[END]{Style.RESET_ALL} No links found by Playwright Web Scraper for '{usernames}'.")
        print(f"\n{Fore.CYAN}--- End of Alias Search ---{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}A critical error occurred: {e}{Style.RESET_ALL}")
    finally:
        if browser:
            await browser.close()


if __name__ == "__main__":
    try:
        asyncio.run(username_search_playwright())
    except KeyboardInterrupt:
        print("\nSearch interrupted by user.")
