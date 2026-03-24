

import sys
import requests

if __name__ =='__main__':

    try:
        print(f'Reading URLs from {sys.argv[1]!r}...')

        with open(sys.argv[1], 'r') as f:
            for possible_url in f:
                try:
                    possible_url = possible_url.strip()
                    r = requests.get(possible_url)
                    if r.status_code != 200:
                        print(f'{possible_url} responded, but source not there.')
                except:
                    print(f'{possible_url} did not respond.')
    except IndexError:
        print('Missing File name after command.')
    except FileNotFoundError:
        print(f'cannot open {sys.argv[1]!r}')     
                             
