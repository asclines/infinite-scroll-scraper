import argparse


def get_args():
    """Return the arguments passed in through CLI, or the defaults."""
    parser = argparse.ArgumentParser(description='Scrapes media from website')
    parser.add_argument('-f','--folder', help='Path to the output folder where media should be saved to. ', nargs=1, type=str, default="./media/")
    parser.add_argument('-p','--pages', help='Number of times to page down in browser.', nargs=1, type=int, default="10")
    parser.add_argument('-u','--url', help='URL to scrape.', nargs=1, type=str, required=True)
    return parser.parse_args()


if __name__ == "__main__": # For future use when a GUI appears.
    args = get_args()
