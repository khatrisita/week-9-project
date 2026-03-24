

import sys
import requests
from requests.exceptions import SSLError, ConnectionError

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
                except SSLError:
                    print(f'{possible_url!r} has an SSL issue.')
                except ConnectionError:
                    print(f'{possible_url!r} did  not connect')
                except:
                    print(f'something unexpected happended with {possible_url!r}.')    
    except IndexError:
        print('Missing File name after command.')
    except FileNotFoundError:
        print(f'cannot open {sys.argv[1]!r}')     
                             
