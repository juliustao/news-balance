import argparse
import os
import time
from urllib.parse import urlsplit, urlunsplit

import selenium
from selenium import webdriver

from scraper import get_url_to_scrape, scrape_url
from sites import get_view
from title import get_title


def run(driver, opposing, latest):
    try:
        current_url = driver.current_url
    except selenium.common.exceptions.NoSuchWindowException:
        driver.switch_to.window(driver.window_handles[-1])
        current_url = driver.current_url
    split_url = urlsplit(current_url)
    # check if the site is partisan and if we're not on the home page
    view = get_view(split_url.netloc)
    if view and len(split_url.path) > 1:
        print("Partisanship detected. Finding new article...")
        if opposing:
            if view == "left":
                view = "right"
            elif view == "right":
                view = "left"
        else:
            view = "centrist"
        title = get_title(current_url)
        url_to_scrape = get_url_to_scrape(title, view=view, latest=latest)
        centrist_url = scrape_url(url_to_scrape)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(centrist_url)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--driver_path", type=str, default="chromedriver_linux64/chromedriver",
        help="Relative path of browser driver from repository directory.",
    )
    parser.add_argument(
        "--buffer", type=float, default=1.,
        help="Time in seconds added between loops.",
    )
    parser.add_argument(
        "--opposing", action="store_true",
        help="Show articles from opposing rather than centrist views.",
    )
    parser.add_argument(
        "--latest", action="store_true",
        help="Show the most recent rather than most relevant article.",
    )
    args = parser.parse_args()

    if args.buffer < 1.:
        raise Exception("Buffer should be at least 1 second.")

    repo_path = os.path.dirname(os.path.abspath(__file__))
    driver = webdriver.Chrome(os.path.join(repo_path, args.driver_path))
    while True:
        time.sleep(args.buffer)
        run(driver, args.opposing, args.latest)
