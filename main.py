import os 
from colorama import Fore
import argparse
from modules import webhook, myemail, username, banners, pastedump, gs

descriptions = banners.menu_help()
parser = argparse.ArgumentParser(description=descriptions)
parser.add_argument('-u', '--username', help="it gives you all the links attached to the username")
parser.add_argument('-e', '--email', help="it gives you all the links attached to the email")
parser.add_argument('-w', '--webhook', help="Change your webhook")
args = parser.parse_args()

if args.username:
    os.system('cls' or 'clear')
    usernames = args.username
    username.username_search(usernames)
    gs.gs_search(usernames)
    
elif args.email:
    mails = args.email
    myemail.email_search(mails)
    pastedump.pastebin_dump(mails)
    
elif args.webhook:
    wbh = args.webhook
    webhook.change_the_webhook(wbh) 
else:
    print("No arguments provided.")
