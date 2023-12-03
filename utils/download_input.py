import requests
import os


def download_input(day: int, directory: str = 'inputs'):
    url = f'https://adventofcode.com/YEAR/day/{day}/input'
    cookie_value = ''

    s = requests.Session()

    r = s.get(url, cookies={'session': cookie_value})
    content = str(r.content)[2:]
    content = content.split('\\n')

    with open(os.path.join(directory, f'day{day}.txt'), 'w') as f:
        for n in content:
            if n == "'":
                continue
            f.write(n)
            f.write('\n')
