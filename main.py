import os 
from colorama import Fore
import argparse
from modules import days, webhook, myemail, username, banners, pastedump, gs

descriptions = banners.menu_help()
parser = argparse.ArgumentParser(description=descriptions)
parser.add_argument('-u', '--username', help="it gives you all the links attached to the username")
parser.add_argument('-e', '--email', help="it gives you all the links attached to the email")
parser.add_argument('-w', '--webhook', help="Change your webhook")
parser.add_argument('-d', '--days', action='store_true', help="Show days left")
args = parser.parse_args()

if args.username:
    os.system('cls' or 'clear')
    remaining_days = days.get_remaining_days()
    if remaining_days <= 0:
        print(f"{Fore.YELLOW}[?]=> No more days left or upgrade the version!{Fore.RESET}")
    else:
        usernames = args.username
        username.username_search(usernames)
        gs.gs_search(usernames)
    
elif args.email:
    os.system('cls' or 'clear')
    remaining_days = days.get_remaining_days()
    if remaining_days <= 0:
        print(f"{Fore.YELLOW}[?]=> No more days left or upgrade the version!{Fore.RESET}")
    else:
        mails = args.email
        myemail.email_search(mails)
        pastedump.pastebin_dump(mails)
    
elif args.webhook:
    remaining_days = days.get_remaining_days()
    if remaining_days <= 0:
        print(f"{Fore.YELLOW}[?]=> No more days left or upgrade the version!{Fore.RESET}")
    else:
        wbh = args.webhook
        webhook.change_the_webhook(wbh)

elif args.days:
    os.system("cls" or "clear")
    remaining_days = days.get_remaining_days()
    print(f"{Fore.YELLOW}[?]=> {remaining_days} days left.{Fore.RESET}")
    if remaining_days <= 0:
        print(f"{Fore.YELLOW}[?]=> No more days left or upgrade the version!{Fore.RESET}")
    
else:
    print("No arguments provided.")
