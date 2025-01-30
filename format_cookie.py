raw = 'cookie from request header' # change me - enter cookie as string
cookie = {}

for line in raw.split(';'):
    line_list = line.split('=', 1)

    key= ''.join(line_list[0]).strip()
    value = ''.join(line_list[1:]).strip()

    cookie[key] = value

print(cookie) # write to cookie.json