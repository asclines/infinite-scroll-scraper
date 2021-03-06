import os
from urllib.parse import urlparse

valid_media_exts = set(['.jpg', '.gif', '.png'])

def is_url_valid(url):
    """ Returns true if url is a valid URL"""
    return urlparse(url).scheme

def filter_urls(urls):
    """ Cleans URLs and filters them to the ones with correct file extenstions."""
    clean_urls = []
    for url in urls:
        clean_url = url.strip().lower()
        ext = os.path.splitext(clean_url )[1]
        if ext in valid_media_exts:
            clean_urls.append(clean_url)
    return clean_urls
