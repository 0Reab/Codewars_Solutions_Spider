import json

raw = 'cookie from https request header' # change me
cookie = {}

for line in raw.split(';'):
    line_list = line.split('=', 1)

    key= ''.join(line_list[0]).strip()
    value = ''.join(line_list[1:]).strip()

    cookie[key] = value

with open('cookie.json', 'w') as file:
    json.dump(cookie, file, indent=4)