import os
import time
from urllib.parse import urlsplit, urlunsplit

from selenium import webdriver

from scrape import get_url_to_scrape, scrape_url
from title import get_title
from url import is_partisan


buffer = 1  # in seconds
driver_rel_path = os.path.join("chromedriver_linux64", "chromedriver")


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(repo_path, driver_rel_path)
    driver = webdriver.Chrome(driver_path)
    while True:
        time.sleep(buffer)
        current_url = driver.current_url
        split_url = urlsplit(current_url)
        if is_partisan(split_url.netloc) and len(split_url.path) > 1:
            title = get_title(current_url)
            url_to_scrape = get_url_to_scrape(title)
            centrist_url = scrape_url(url_to_scrape)
            if centrist_url != current_url:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[1])
                driver.get(centrist_url)
