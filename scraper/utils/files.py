import os
import errno
from urllib.request import urlopen

def download_media(urls, output_path):
    """ Downloads all media from the urls and stores in output_path"""
    folderpath = output_path.rstrip('//')
    mkdir_p(folderpath)
    for url in urls:
        filename = url.rsplit('/', 1)[-1]
        filepath = "{}/{}".format(folderpath, filename)
        if(os.path.isfile(filepath)):
            print("{} already exists...skipping.".format(filename))
        else:
            print("Downloading {} \n\t from {}".format(filename,url))
            download(url, filepath)



def mkdir_p(path):
    """ Python implementation of the bash cmd 'mkdir -p'"""
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def download(url, path):
    """ Downloads media from URL"""
    data = urlopen(url).read()
    output = open(path,'wb')
    output.write(data)
    output.close()
