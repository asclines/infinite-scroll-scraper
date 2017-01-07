import unittest
from .context import urls


class TestUtilsUrls(unittest.TestCase):
    """ Tests methods in utils.urls"""

    def test_invalid_url(self):
        """ Tests utils.urls#is_url_valid(url)"""
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

    def test_filter_urls(self):
        """ Tests utils.urls#filter_urls(urls)"""
        test_urls = ['http://media.com/funny.jpg', \
        'http://media.com/funny.JPG', \
        'http://media.com/funny.png', \
        'http://media.com/funny.PNG', \
        'http://media.com/funny.GIF',  \
        'http://media.com/funny.gif', \
        'http://media.com/funny.nope'
         ]

        expected_result = ['http://media.com/funny.jpg', \
        'http://media.com/funny.jpg', \
        'http://media.com/funny.png', \
        'http://media.com/funny.png', \
        'http://media.com/funny.gif', \
        'http://media.com/funny.gif']

        actual_result = urls.filter_urls(test_urls)

        self.assertEquals(expected_result, actual_result)
