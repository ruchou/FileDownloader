#!/usr/bin/env python
import requests
#     $ ./downloader <URL> -c nThreads
import sys, getopt

class Downloader():
    def __init__(self,url=''):
        self.url = url

    def download_files(self):
        r = requests.get(self.url)
        file_name = self.url.split('/')[-1]
        if not file_name:
            print("no such file")
            exit(0)

        with open(file_name, 'wb') as f:
            f.write(r.content)
            # Retrieve HTTP meta-data
            print(r.status_code)
            print(r.headers['content-type'])
            print(r.encoding)

if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) else ''
    downloader = Downloader(url=url)
    downloader.download_files()

