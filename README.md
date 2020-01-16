# udonge-bot

Another bot for posting arts to your timeline. 

Currently posting on: https://social.inex.rocks/@ReisenBot

### How to run ###
* First of all, you must have `python3`, `pip` and `venv` already installed.
* Clone the repository:
```bash
git clone https://github.com/WizardNaiJi/udonge-bot
cd udonge-bot
```
* Create a bot account on your Mastodon instance.
* [Edit Profile] -> [Appearance] -> Check: `This is a bot account`
* [Edit Profile] -> [Development] -> [New Application]
* Fill the meta-data forms
* Check:
```
write
write:statuses
```
* Submit!
* [Edit Profile] -> [Development] -> Choose your application
* Copy your access token.
* Go to /udonge-bot directory and save the token:
```bash
echo "YOURTOKENYOURTOKENYOURTOKENYOURTOKEN" > token.dat
````
* Setup virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```
### For posting you have two ways: ###
* First way: use arts from local folder /sources. In this case you should either manually move them to the destination or
* (venv) ...download them by:
```bash
python3 download.py
deactivate
``` 
* Next, save the script as `runner`:
```bash
#!/bin/bash
venv/bin/python3 post-local.py
```
* Second way: repost each art from danbooru! In this case you don't have to story anything on your local storage, but this way it's much harder to control quality of arts!
* Save the script as `runner`:
```bash
#!/bin/bash
venv/bin/python3 post-danbooru.py
```
* Edit tags.dat file. You can look at already defined tags and use it as example
```
#first line is for tags you want to search the arts with (must be exactly 2)
#second line is for tags you decline from posting completely (as many as you want)
#third line is for tags you want mastodon to mark as sensitive (as many as you want)
```
### Either way you have chosen before, now: ###
* Setup cron:
```bash
crontab -e
```
* Append to end of the file:
```bash
0,30 * * * * cd <fullpath>/udonge-bot && sh <fullpath>/udonge-bot/runner
# where <fullpath> is ... well.., the full path from /home/ to the following folder
# if you don't know it, just use pwd command
```
* Save your changes and make sure the message appeared:
```bash
crontab: installing new crontab
```
* That's all!
