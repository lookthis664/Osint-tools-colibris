![menu](photo/help_menu.png)


**Features**
- [x] Get links & category from a username
- [X] Know if an email address has been breached
- [X] Reactive to command

**How do I install it? First of all, you need to launch the config file and then run "Setup.bat "**.

**How do I use it? First you need to set up a discord webhook with the following command:**
```
py main.py -w {enter your webhook}
```
The help command is as follows:
```
py main.py -h
```

To search you have 2 commands, here they are:
```
py main.py -u {username}
py main.py -e {email}
```
![new2](photo/new2.png)


!!UPDATE ON 16/09/2023!! 
Addition of a printout of the results provided by the software in a json file (A backup of the results in bulk) and a new grey interface.

!!UPDATE ON 20/09/2023!! 
I fixed the following problem: "pastebin_dump_link": "https://pastebin.com/['XXXXXX']" which is written in the json file during pastebin. Now it will write you correctly without the "['...']".

If you have any questions or special requests, please send a message to the following discord number: 923974093915717632


