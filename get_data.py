from time import sleep
from selenium import webdriver


def fetch_html(url, cookies) -> str:
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.codewars.com/') # load base domain

    # load cookies
    for name, value in cookies.items():
        driver.add_cookie({"name": name, "value": value, "domain": ".codewars.com"})

    driver.get(url)


    # scrolling to load all dynamically loaded data
    height_param = 'document.body.scrollHeight'
    last_height = driver.execute_script(f'return {height_param}')

    while True:
        driver.execute_script(f'window.scrollTo(0, {height_param});') # scroll to bottom
        sleep(2)

        new_height = driver.execute_script(f'return {height_param}')
        if new_height == last_height:
            break
        last_height = new_height

    # return and exit
    raw_html = driver.page_source
    driver.quit()

    return raw_html