# Codewars_Solutions_Spider

Codewars API at the moment does not have a functionality to fetch solutions to coding challanges solutions.

## Desciption

Headless selenium web browsing to load fetch dynamically loaded content and then parse it via beatiful soup.<br>
Completes missing API feature to fetch your codewars challenge solutions.

## Output

My solutions output for example.<br>
https://github.com/0Reab/Codewars_solutions

Organized files in directories by challenge difficulty (or special `Retired` directory): 
* `/7_kyu/fibbonaci_sequence.py`
* `/8_kyu/sum_array.py`

Each file will have:
* Name same as challenge name with appropriate file extension for the language.
* prepended multi-line comment with the challenge description.
* Your solution code. 

## Features

* Rate limited HTTPS via python `requests` to prevent spam.
* Sanitized and organized file and directory names.

## Usage

1. `pip install -r requrements.txt`<br>
2. Change the `user` variable in `codewars.py` to your username.<br>
3. Put cookie from request header into `raw` variable as string and run `format_cookie.py`<br>
4. Run `codewars.py`
