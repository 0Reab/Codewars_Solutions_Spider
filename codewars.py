import json

from file_ops import create_dirs, cleanup_filename, write_file
from get_data import fetch_html, get_description
from bs4 import BeautifulSoup


def load_cookie(file) -> dict:
    try:
        with open(file, 'r') as r:
            return json.loads(r.read()) # dictionary
    except FileNotFoundError:
        print(f'File not found {file}')
    except json.JSONDecodeError as e:
        print(f'Invalid JSON syntax: {e}')


def parse(data):
    # beautiful soup html parsing for challenge solutions
    soup = BeautifulSoup(data, 'html.parser')
    return soup.find_all('div', class_='list-item-solutions')


def main():
    user = 'your_username_here'  # Change this
    file_name = 'cookie.json'
    challenge_api = 'https://www.codewars.com/api/v1/code-challenges/'
    url = f'https://www.codewars.com/users/{user}/completed_solutions'

    # cleanup main - too messy
    snake = lambda y: y.replace(' ', '_')  # wrapper -> converts string to snake_case

    create_dirs() # prepare environment for file write
    response = fetch_html(url, load_cookie(file_name)) # txt file reading - will replace w/ http requests

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
                description =  f"'''\n{get_description(kata_id, challenge_api)}\n'''\n\n"
                # description = 'lolol'

                # debug lines
                contents = f'{description}{code}'
                print(f'writing file -> {file_path}')

                write_file(file_path, contents)


if __name__ == '__main__':

    main()
