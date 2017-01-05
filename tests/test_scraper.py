import unittest
from .context import scraper

class TestArguments(unittest.TestCase):
    """ Tests handling of arguments passed in from user."""
    def setUp(self):
        """ Creates valid args for simplicity. Each test can modify the one they are testing."""
        self.args = scraper.Args
        self.args.url = "http://www.google.com"

    def test_invalid_url(self):
        """ Makes sure that the correct exception is raised when an invalid URL is pased in."""
        self.args.url = "notavalidurl"
        with self.assertRaises(scraper.UserInputException):
            scraper.scrape_site(self.args)
