import requests 
import sys

import os.path as op
from mastodon import Mastodon

# --------------------------------------------------

BAN_TAGS = [ 'no_panties', 'comic', 'nipples', 'unhappy' ]
UNSAFE_TAGS = [ 'swimsuit', 'underwear', 'ass', 'large_breasts' ]

def main():

    mastodon = Mastodon(
        access_token = 'token.dat',
        api_base_url = 'https://social.inex.rocks/'
    )

    URL    = "https://danbooru.donmai.us/posts.json"
    PARAMS = { 'tags': '1girl reisen_udongein_inaba',
               'limit': 1,
               'random': True } 

    b_success = False
    while not b_success:
        r = requests.get(url = URL, params = PARAMS) 
        data = r.json()

        fileurl    = data[0]['file_url']
        print('url ', fileurl)
        fileid     = data[0]['id']
        print('id ', fileid)
        filescore  = data[0]['fav_count']
        print('score ', filescore)
        filesafe   = data[0]['rating']
        print('rating ', filesafe)
        filetagstring = data[0]['tag_string']

        # we don't want comics, porn and lowscored arts
        if (filesafe != 'e' and filescore >= 25
            and any(tag not in filetagstring.strip().split() for tag in BAN_TAGS)):
            b_success = True

    fformat = op.splitext(fileurl)[1][1:]

    print(fformat)
    if (fformat == 'jpg'):
        fformat = 'jpeg'
    media = mastodon.media_post(requests.get(fileurl).content, f'image/{fformat}')

    tags = '#touhou #reisen '
    if ('s' == filesafe):
        tags += '#cuteposting'

    toot  = f'{tags}\nhttps://danbooru.donmai.us/posts/{fileid}'

    # is it 's'afe, free from swimsuits and underwear tags, etc
    b_sensetive = ('s' != filesafe
                   or any(tag in filetagstring.strip().split() for tag in UNSAFE_TAGS))

    mastodon.status_post(toot, media_ids=[media], visibility='unlisted', sensitive=b_sensetive)

if __name__ == '__main__':
    sys.exit(main())
