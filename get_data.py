import requests

from time import sleep
from selenium import webdriver


def fetch_html(url, cookies) -> str | None:
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    driver.get('https://www.codewars.com/') # load base domain

    # load cookies
    for name, value in cookies.items():
        driver.add_cookie({"name": name, "value": value, "domain": ".codewars.com"})

    driver.get(url)

    # check for error
    if 'Page not found' in driver.page_source or driver.current_url != url:
        driver.quit()
        return None


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


def get_description(kata_id, api) -> str | None:
    # fetch text description of coding challenges via API url and kata id num
    sleep(0.5) # anti dos measures
    resp = requests.get(api+kata_id)

    if resp.status_code != 200: return None

    return resp.json().get('description')
