import unittest
from .context import urls


class TestUtilsUrls(unittest.TestCase):
    """ Tests methods in utils.urls"""

    def test_invalid_url(self):
        """ Makes sure that utils.url.is_url_valid returns correct values."""
        valid_urls = ['http://www.validsite.com', \
        'https://www.valid.site.com',\
        'http://validsite.org',\
        'https://validsite.net']

        invalid_urls = ['not.valid.site.com'\
        'reallnotavalidsiteatall']

        for valid_url in valid_urls:
            self.assertTrue(urls.is_url_valid(valid_url))

        for invalid_url in invalid_urls:
            self.assertFalse(urls.is_url_valid(invalid_url))
