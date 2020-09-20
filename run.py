import argparse
import os
import time
from urllib.parse import urlsplit, urlunsplit

import selenium
from selenium import webdriver

from scrape import get_url_to_scrape, scrape_url
from title import get_title
from url import get_view


opposing_view = {
    "left": "right",
    "right": "left",
}
buffer = 1  # in seconds
driver_path = "chromedriver_linux64/chromedriver"
show_opposing_view = False
latest = False


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.abspath(__file__))
    driver = webdriver.Chrome(os.path.join(repo_path, driver_path))
    while True:
        time.sleep(buffer)
        try:
            current_url = driver.current_url
        except selenium.common.exceptions.NoSuchWindowException:
            driver.switch_to.window(driver.window_handles[-1])
            current_url = driver.current_url
        except selenium.common.exceptions.WebDriverException:
            print("Web browser closed: program terminating.")
            break
        split_url = urlsplit(current_url)
        # check if the site is partisan and if we're not on the home page
        view = get_view(split_url.netloc)
        if view and len(split_url.path) > 1:
            if show_opposing_view:
                view = opposing_view[view]
            else:
                view = "centrist"
            title = get_title(current_url)
            url_to_scrape = get_url_to_scrape(title, view=view, latest=latest)
            centrist_url = scrape_url(url_to_scrape)
            if centrist_url != current_url:
                driver.execute_script("window.open('');")
                driver.switch_to.window(driver.window_handles[-1])
                driver.get(centrist_url)
