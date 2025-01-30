import requests
import json
import time
import os

from get_data import fetch_html
from bs4 import BeautifulSoup


user = '' # Change this
data_name = 'cookies.json'
challenge_api = 'https://www.codewars.com/api/v1/code-challenges/'
url = f'https://www.codewars.com/users/{user}/completed_solutions'



def load_cookie(file=data_name) -> dict:
    try:
        with open(file, 'r') as r:
            return json.loads(r.read()) # dictionary
    except FileNotFoundError:
        print(f'File not found {file}')
    except json.JSONDecodeError as e:
        print(f'Invalid JSON syntax: {e}')


def create_dirs() -> None:
    # create directories for each coding challenge difficulty + retired ones
    try:
        os.mkdir('Retired')
        for n in range(1,8+1): os.mkdir(f'{n}_kyu')

    except FileExistsError: print('Directory already exists')
    except PermissionError: print('Permission denied unable to create directories'); exit(1)
    except Exception as er: print(f'Error occurred {er}'); exit(1)


def parse(data):
    # beautiful soup html parsing for challenge solutions
    soup = BeautifulSoup(data, 'html.parser')
    return soup.find_all('div', class_='list-item-solutions')


def get_description(kata_id, api=challenge_api) -> str | None:
    # fetch text description of coding challenges via API url and kata id num
    time.sleep(0.5) # anti dos measures
    resp = requests.get(api+kata_id)

    if resp.status_code != 200: return None

    return resp.json()['description']


def write_file(path, text) -> True | False:
    # Write content to a file in a given path
    try:
        with open(path, 'w', encoding='utf-8') as file:
            os.utime(path, None)
            file.write(text)
            return True

    except FileExistsError:
        print(f'File already exists {path}')
    except Exception as err:
        print(f'Failed to write to {path}, {err}')

    return  False


def cleanup_filename(file_name: str) -> str:
    # remove illegal windows filename characters
    illegal_characters = [
        '#', '%', '&', '{', '}', '\\', '<', '>', '*', '?', '/', ' ', '$', '!', "'", '"', ':', '@', '+', '`', '|', '=',
    ]
    return ''.join([ char for char in file_name if char not in illegal_characters ])


def main():
    # cleanup main - too messy
    snake = lambda y: y.replace(' ', '_')  # wrapper -> converts string to snake_case

    create_dirs() # prepare environment for file write
    response = fetch_html(url, load_cookie()) # txt file reading - will replace w/ http requests

    if response:
        solutions = parse(response) # use beautifulsoup

        for s in solutions:
            rank = snake(s.find('span').text)
            code = s.find('pre').text
            lang = s.find('h6').text.lower().strip()
            name = snake(s.find('a').text)
            link = s.find('a', href=True)
            kata_id = link['href'][6:]

            if code:
                file_name = cleanup_filename(f'{name}.{lang[:2]}')
                file_path = f'{rank}/{file_name}'
                description =  f"'''\n{get_description(kata_id)}\n'''\n\n"
                contents = f'{description}{code}'

                # debug lines
                #description = 'lolol'
                #contents = f'{description}{code}'

                #if file_path == '6_kyu/Decode_the_Morse_code_.py':
                #    description =  f"'''\n{get_description(kata_id)}\n'''\n\n" # get_description(kata_id) -> works good
                #    contents = f'{description}{code}'
                # end debug lines

                write_file(file_path, contents) # bug - can't create filenames with char '?' -> fixed


if __name__ == '__main__':
    main()