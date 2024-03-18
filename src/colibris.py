import os 
import argparse
import webhook
import username
import banners
import gs
import asyncio
import apigithub

def main():
    loop = asyncio.get_event_loop()
    descriptions = loop.run_until_complete(banners.menu_help())
    parser = argparse.ArgumentParser(description=descriptions)
    parser.add_argument('-u', '--username', help="it gives you all the links attached to the username")
    parser.add_argument('-g', '--github', help="it gives you the email + name + GitHub username of a person")
    parser.add_argument('-w', '--webhook', help="Change your webhook")
    args = parser.parse_args()

    if args.username:
        os.system('cls' or 'clear')
        usernames = args.username
        loop = asyncio.get_event_loop()
        loop.run_until_complete(username.username_search(usernames))
        loop.run_until_complete(gs.gs_search(usernames))
        loop.run_until_complete(apigithub.username_search(usernames))
        
    elif args.github:
        os.system('cls' or 'clear')
        usernames = args.github
        loop = asyncio.get_event_loop()
        loop.run_until_complete(apigithub.username_search(usernames))

    elif args.webhook:
        os.system('cls' or 'clear')
        wbh = args.webhook
        loop = asyncio.get_event_loop()
        loop.run_until_complete(webhook.change_the_webhook(wbh))

    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()
