import requests
import json

cache = {}
url = 'http://www.floatrates.com/daily/{}.json'


def retrieve_info(code, to=''):
    req = requests.get(url.format(code))
    if req:
        res = req.text
        obj = json.loads(res)
        if to == '':
            if code != 'eur':
                cache['eur'] = obj['eur']
            if code != 'usd':
                cache['usd'] = obj['usd']
        else:
            cache[to] = obj[to]
    else:
        return False


def main():
    f = input().lower()
    retrieve_info(f)
    while True:
        to = input().lower()
        if len(to) == 0:
            break
        amount = float(input())
        print('Checking the cache...')
        if to in cache:
            print('Oh! It is in the cache!')
        else:
            print('Sorry, but it is not in the cache!')
            retrieve_info(f, to)
        print('You received {:.2f} {}'.format(amount * cache[to]['rate'], to))


if __name__ == '__main__':
    main()
