import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

valid_media_exts = set(['jpg'])

class Args(object):
    """Simple class for holding args when not from CLI"""
    pass

class UserInputException(Exception):
    """Raised when an exception is thrown due to user input."""

def scrape(args):
    """
    Entry method to all the real work.
    Epects args to be either filled from CLI argument parsing or from GUI.
    """
    browser = webdriver.Chrome()
    try:
        browser.get(args.url)
        time.sleep(1)
        page = browser.find_element_by_tag_name("body")
        scroll_page(page, args.pages)
    except WebDriverException as e:
        raise UserInputException("Invalid URL",e)
    finally:
        browser.quit()

def scroll_page(page, count):
    """ Pages down count times on page."""
    while count:
        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        count-=1


def get_args():
    """Return the arguments passed in through CLI, or the defaults."""
    parser = argparse.ArgumentParser(description='Scrapes media from website')
    parser.add_argument('-f','--folder', help='Path to the output folder where media should be saved to. ', type=str, default="./media/")
    parser.add_argument('-p','--pages', help='Number of times to page down in browser.', type=int, default="10")
    parser.add_argument('-u','--url', help='URL to scrape.', type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__": # For future use when a GUI appears.
    scrape(get_args())
