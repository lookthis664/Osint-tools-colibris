import os 
import argparse
import username
import banners
import gs
import asyncio
import mtda
import dele

def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    descriptions = loop.run_until_complete(banners.menu_help())
    parser = argparse.ArgumentParser(description=descriptions)
    parser.add_argument('-u', '--username', help="it gives you all the links & metadata attached to the username")
    #parser.add_argument('-h', '--help', help="Help command")
    args = parser.parse_args()

    if args.username:
        os.system('cls' or 'clear')
        usernames = args.username
        loop = asyncio.new_event_loop()
        loop.run_until_complete(username.username_search(usernames))
        loop.run_until_complete(gs.gs_search(usernames))
        loop.run_until_complete(mtda.jsonfichier(usernames))
        loop.run_until_complete(dele.delete_fichiertemp(usernames))

    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main()