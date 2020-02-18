# udonge-bot

Another bot for posting arts to your timeline. 

Currently posting on: https://social.inex.rocks/@ReisenBot

### For posting you have two ways: ###
* First way: use arts from local folder /sources. In this case you should either manually move them to the destination or
* ...download them by:
```bash
python3 download.py
``` 
* To make a post the local-way, use the `post-local.py` script!
* Second way: repost each art from danbooru! In this case you don't have to store anything on your local storage, but this way it gets much harder to control quality of posts!
* To make a post danbooru-way, use the `post-danbooru.py` script!
* Edit tags.dat file. You can look at already defined tags and use it as example
```
#first line is for tags you want to search the arts with (must be exactly 2)
#second line is for tags you decline from posting completely (as many as you want)
#third line is for tags you want mastodon to mark as sensitive (as many as you want)
```
* Don't forget to setup your bot account, get access tokens and establish the environment around it. I am not providing any instructions of how to do it, since all the steps are different and depend on what, where and how you want to run the bot.

* That's all!
