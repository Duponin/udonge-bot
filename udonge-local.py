import requests 
import sys
import random
import os
import os.path as op

from mastodon import Mastodon
from datetime import datetime

# --------------------------------------------------

DIR = 'sources/'

def main():

    mastodon = Mastodon(
        access_token = 'token.dat',
        api_base_url = 'https://social.inex.rocks/'
    )

    onlyfiles = [f for f in os.listdir(DIR) if op.isfile(op.join(DIR, f))]

    art = DIR + random.choice(onlyfiles)

    fformat = op.splitext(art)[1][1:]

    if (fformat == 'jpg'):
        fformat = 'jpeg'

    with open(art, 'rb') as picture:
        data = picture.read()

    media = mastodon.media_post(data, f'image/{fformat}')
    tags = '#touhou #udongein #reisenbot'

    toot  = f':love_reisen: {tags}'

    mastodon.status_post(toot, media_ids=[media], visibility='unlisted', sensitive=True)
    print(str(datetime.now()) + ': ' + art)

if __name__ == '__main__':
    sys.exit(main())
