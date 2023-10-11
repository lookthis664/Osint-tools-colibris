import os 
import argparse
import webhook
import myemail
import username
import banners
import pastedump
import gs
import asyncio

def main():
    loop = asyncio.get_event_loop()
    descriptions = loop.run_until_complete(banners.menu_help())
    parser = argparse.ArgumentParser(description=descriptions)
    parser.add_argument('-u', '--username', help="it gives you all the links attached to the username")
    parser.add_argument('-e', '--email', help="it gives you all the links attached to the email")
    parser.add_argument('-w', '--webhook', help="Change your webhook")
    args = parser.parse_args()

    if args.username:
        os.system('cls' or 'clear')
        usernames = args.username
        loop = asyncio.get_event_loop()
        loop.run_until_complete(username.username_search(usernames))
        loop.run_until_complete(gs.gs_search(usernames))

    elif args.email:
        mails = args.email
        loop = asyncio.get_event_loop()
        myemail.email_search(mails)
        pastedump.pastebin_dump(mails)

    elif args.webhook:
        wbh = args.webhook
        loop = asyncio.get_event_loop()
        loop.run_until_complete(webhook.change_the_webhook(wbh))
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()
