import argparse
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

class UserInputException(Exception):
    """Raised when an exception is thrown due to user input."""

def scrape_site(args):
    """
    Entry method to all the real work.
    Epects args to be either filled from CLI argument parsing or from GUI.
    """
    browser = webdriver.Chrome()
    try:
        browser.get(str(args.url))
    except WebDriverException as e:
        raise UserInputException("Invalid URL",e)
    finally:
        browser.quit()



def get_args():
    """Return the arguments passed in through CLI, or the defaults."""
    parser = argparse.ArgumentParser(description='Scrapes media from website')
    parser.add_argument('-f','--folder', help='Path to the output folder where media should be saved to. ', nargs=1, type=str, default="./media/")
    parser.add_argument('-p','--pages', help='Number of times to page down in browser.', type=int, default="10")
    parser.add_argument('-u','--url', help='URL to scrape.', type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__": # For future use when a GUI appears.
    scrape_site(get_args())
