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
    
    with open('tags.dat', 'rb') as dat:
        tags = dat.read()

    URL = "https://danbooru.donmai.us/posts.json"
    LIMIT = 10
    MIN_SCORE = 25
    SAFETY = 's'
    TAGS_POST = tags[0].strip().split()
    TAGS_FORBID = tags[1].strip().split()
    TAGS_SENSITIVE = tags[2].strip().split()
    
    PARAMS = { 'tags': TAGS_POST,
               'limit': LIMIT,
               'random': True } 
    
    print('[start] Settings:')
    print('LIMIT = ' + str(LIMIT) + ' | MIN_SCORE = ' + str(MIN_SCORE) + ' | SAFETY = ' + SAFETY)
    print('TAGS_POST=' + str(TAGS_POST))
    print('TAGS_FORBID=' + str(TAGS_FORBID))
    print('TAGS_SENSITIVE=' + str(TAGS_SENSITIVE))
               
# --------------------------------------------------

    counter = 1
    b_search = True
    while b_search:
        r = requests.get(url = URL, params = PARAMS)
        print('[get] Attempt N' + str(counter) + '.')
        data = r.json()
        for i in range(0, LIMIT):
            fileurl = data[i]['file_url']
            print('url ', fileurl)
            fileid = data[i]['id']
            print('id ', fileid)
            filescore = data[i]['fav_count']
            print('score ', filescore)
            filesafe = data[i]['rating']
            print('rating ', filesafe)
            filetagstring = data[i]['tag_string']

            if (filesafe == SAFETY and filescore >= MIN_SCORE
                and not set(filetagstring).intersection(TAGS_FORBID):
                print('[success] Found ' + fileurl)
                b_search = False
                break;
        print('[fail] No acceptable arts.')
                
# --------------------------------------------------

    fformat = op.splitext(fileurl)[1][1:]
    if (fformat == 'jpg'):
        fformat = 'jpeg'
        
    media = mastodon.media_post(requests.get(fileurl).content, f'image/{fformat}')
    toot  = f':love_reisen: \nhttps://danbooru.donmai.us/posts/{fileid}'

    b_sensetive = set(filetagstring).intersection(TAGS_SENSITIVE)
                    
    if (b_sensetive):
        print('[success] Marked as sensitive.')

    mastodon.status_post(toot, media_ids=[media], visibility='unlisted', sensitive=b_sensetive)
    print('[success] Posted!\n----------------------------------\n')

if __name__ == '__main__':
    sys.exit(main())
