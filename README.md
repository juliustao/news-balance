# News Balance

## Environment
This code is tested with Python 3.6.9 on Ubuntu 18.04 in the Chromium browser.

* Any recent version of Python 3 should work.
* Although not tested on Windows or Mac, there is no OS-specific code. I
expect Mac to work out-of-the-box, but Windows will need some adjustments.
* Google Chrome should work. To use another browser, download its webdriver
in the setup below and change `run.py` so `driver` uses the correct browser.

## Getting Started
0. Check if you have Python 3 by running `python3 --version`.
If not found, install Python 3 from [here](https://www.python.org/downloads/).

1. I highly recommend that you create a Python 3 virtual environment:
    ```
    python3 -m venv PATH_TO_VENV
    ```
    Activate the environment:
    ```
    source PATH_TO_VENV/bin/activate
    ```
    To activate in Windows:
    ```
    PATH_TO_VENV\Scripts\activate.bat
    ```

2. Install pip dependencies:
    ```
    pip install -r requirements.txt
    ```

3. Install the Selenium webdriver:

    See [here](https://selenium-python.readthedocs.io/installation.html#drivers)
    for links to webdrivers for Selenium-compatible browsers. Place the unzipped
    folder under this repository, and remember to specify the driver path later.

    Windows users may need the details underneath the section from the above link.

4. Sanity-check the backend:

    Copy the URL of some news article from Fox or Vox and run
    ```
    python3 test.py --url THAT_URL
    ```

5. Open the Selenium browser:

    Before running `python3 run.py`, check that the default arguments are
    satisfactory. If not, specify them accordingly.

    A Selenium browser should appear. If you begin reading any partisan news
    article, you'll be interrupted by a new tab with similar content but
    contrasting viewpoint.

    The original intent is to show centrist articles, but I added an option
    to show articles from opposing viewpoints. Be warned though, as the
    newly shown articles are partisan and will spawn opposing articles
    themselves! That might just be intended to encourage centrism though :wink:


## Details
The core of this repository is its backend, which checks a given article's
political bias and recommends an article of similar content from a more
central viewpoint. We scrape the news site
[AllSides](https://www.allsides.com/unbiased-balanced-news) by querying
the given article's title in its search engine and filtering for articles
that are centrist and most relevant.

The frontend is what I had the most trouble with. Ideally, we could detect
when a new webpage is loaded and send its URL to the backend, which is
surprisingly difficult to do from native Python. Selenium works fine, but
I'd love to see a native-browser solution!
