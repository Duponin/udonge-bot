import requests 
import sys

import os.path as op
from mastodon import Mastodon

# --------------------------------------------------

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
        b_still_e = 'no panties' not in filetagstring and 'comic' not in filetagstring and 'nipples' not in filetagstring
        if b_still_e and filesafe != 'e' and filescore >= 10:
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

    # is it 's'afe, free from swimsuits and underwear tags
    b_sensetive = 's' != filesafe or 'swimsuit' in filetagstring or 'underwear' in filetagstring
    mastodon.status_post(toot, media_ids=[media], visibility='unlisted', sensitive=b_sensetive)

if __name__ == '__main__':
    sys.exit(main())