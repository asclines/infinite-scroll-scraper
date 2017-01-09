import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from utils import urls as URLS
from utils.files import download_media

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
    if not URLS.is_url_valid(args.url):
        raise UserInputException("Invalid URL")

    driver = webdriver.Chrome()
    try:
        driver.get(args.url)
        time.sleep(1)
        page = driver.find_element_by_tag_name("body")
        scroll_page(page, args.pages)
        media_urls = scrape_media(driver)
        media_urls = URLS.filter_urls(media_urls)
        download_media(media_urls, args.folder)

    except WebDriverException as e:
        raise UserInputException("Invalid URL",e)
    finally:
        driver.quit()


def scroll_page(page, count):
    """ Pages down count times on page."""
    while count:
        page.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        count-=1

def scrape_media(driver):
    """ Goes through the element and extracts media links."""
    # page_source = (driver.page_source).encode('utf-8')
    media_urls = []
    media_urls.extend(find_img_elems(driver))
    # body_html = driver.find_element_by_tag_name("body")
    return media_urls

def find_img_elems(driver):
    """ Finds all elements with tag <img> and returns a list of the src."""
    image_elems = driver.find_elements_by_tag_name('img')
    results = []
    for image_elem in image_elems:
        image_url = image_elem.get_attribute("src")
        results.append(image_url)
    return results

def get_args():
    """Return the arguments passed in through CLI, or the defaults."""
    parser = argparse.ArgumentParser(description='Scrapes media from website')
    parser.add_argument('-f','--folder', help='Path to the output folder where media should be saved to. ', type=str, default="./media/")
    parser.add_argument('-p','--pages', help='Number of times to page down in browser.', type=int, default="0")
    parser.add_argument('-u','--url', help='URL to scrape.', type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__": # For future use when a GUI appears.
    scrape(get_args())
    print("done")
