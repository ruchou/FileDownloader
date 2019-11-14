#!/usr/bin/env python

# $ ./downloader <URL> -c nThreads
import requests
import sys, getopt
import os
from multiprocessing.pool import ThreadPool

class Downloader():
    def __init__(self,url=''):
        self.url = url


    def download_files(self):
        #fetch file from url
        r = requests.get(self.url,stream= True)
        if r.status_code != 200:
            print("status code is not 200, {}".format(r.status_code))
            exit(0)

        # Retrieve HTTP meta-data
        print(r.status_code)
        print(r.headers['content-type'])
        print(r.encoding)

        #download file name
        file_name = self.url.split('/')[-1]
        if not file_name:
            print("no such file")
            exit(0)
        #write files to local
        #https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
                    os.fsync(f.fileno())


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) else ''
    downloader = Downloader(url=url)
    downloader.download_files()

