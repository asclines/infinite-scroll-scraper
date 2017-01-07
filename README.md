# Infinite Website Scrolling Scraper
_Media scraper for sites with infinite scrolling._  
This script will load a website in a browser and download media from it.

# Latest Version
Alpha - This is still under active development.

# Features
- Download images & videos from a website
- Auto scrolls to get more content
- Simple, lightweight & portable

# Motivation
This script is the result of my learning web scraping with Python.  
I hope this can help serve as an educational tool to showcase various software
development skillsets.

# Installation
This script was built with **Python 2.7**.  
It has not been test for **Python 3** yet.

## System
This script has currently only been testing on **Windows 10**.

## Dependencies
The Python libraries this script needs are:
- [Selenium](http://selenium-python.readthedocs.io/)

[ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/):
This script uses ChromeDriver to load a Chrome browser in order to load the website.

# Usage
```
usage: scraper.py [-h] [-f FOLDER] [-p PAGES] -u URL

Scrapes media from website

optional arguments:
  -h, --help            show this help message and exit
  -f FOLDER, --folder FOLDER
                        Path to the output folder where media should be saved
                        to.
  -p PAGES, --pages PAGES
                        Number of times to page down in browser.
  -u URL, --url URL     URL to scrape.
  ```

## Example
Let's say I wanted to get the recent iFunny features and save them in a folder
called "features" in my "C:/" drive. I could do that by running this command:
```
python scraper.py -u https://www.ifunny.co -f C:\features -p 10
```

# Contributing
Please fork this repository and contribute back using pull requests and feature branches.
More info can be found on the [CONTRIBUTING.md](.github/CONTRIBUTING.md) page,



## Running Tests
You can run all tests by running this command in the root folder.
```python
python -m unittest discover
```

<!-- TODO:# Acknowledgements -->

# Roadmap
* Make minimal viable product
* Simplify installation with `pip`
* Provide auto image cropping & editing
* A GUI


# Known Issues
None yet :)
