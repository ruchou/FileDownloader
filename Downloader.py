#!/usr/bin/env python

# $ ./downloader <URL> -c nThreads
import requests
import sys, getopt
import os
import threading
import click
#
# class Downloader():
#     def __init__(self,url=''):
#         self.url = url
#
#
#     def download_files(self):
#         r = requests.head(self.url)
#
#         # download file name
#         local_filename = self.url.split('/')[-1]
#         if not local_filename:
#             print('Unknowned file name')
#             exit(0)
#
#         # check if it is valid url
#         try:
#             file_size = int(r.headers['content-length'])
#         except:
#             print("Invalid URL")
#             return
#
#         part = int(file_size) / number_of_threads
#         fp = open(file_name, "wb")
#         fp.write('\0' * file_size)
#         fp.close()
#
#         for i in range(number_of_threads):
#             start = part * i
#             end = start + part
#
#             # create a Thread with start and end locations
#             t = threading.Thread(target=Handler,
#                                  kwargs={'start': start, 'end': end, 'url': url_of_file, 'filename': file_name})
#             t.setDaemon(True)
#             t.start()
#
#         main_thread = threading.current_thread()
#         for t in threading.enumerate():
#             if t is main_thread:
#                 continue
#             t.join()
#         print('%s downloaded' % file_name)
#
#         #fetch file from url
#         r = requests.get(self.url,stream= True)
#         if r.status_code != 200:
#             print("status code is not 200, {}".format(r.status_code))
#             exit(0)
#
#         # Retrieve HTTP meta-data
#         print(r.status_code)
#         print(r.headers['content-type'])
#         print(r.encoding)
#
#
#         #write files to local
#         #https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
#         with open(loca_filename, 'wb') as f:
#             for chunk in r.iter_content(chunk_size=1024):
#                 if chunk:  # filter out keep-alive new chunks
#                     f.write(chunk)
#                     f.flush()
#                     os.fsync(f.fileno())

def Handler(start, end, url, filename):
    # specify the starting and ending of the file
    headers = {'Range': 'bytes=%d-%d' % (start, end)}

    # request the specified part and get into variable
    r = requests.get(url, headers=headers, stream=True)

    # open the file and write the content of the html page
    # into file.
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)

@click.command(help="It downloads the specified file with specified name")
@click.option('-count',default=4, help="No of Threads")
@click.argument('url',type=click.Path())
@click.pass_context
def download_file(ctx,url,count):
    r = requests.head(url)
    # download file name
    local_filename = url.split('/')[-1]
    if not local_filename:
        print('Unknowned file name')
        exit(0)

    # check if it is valid url
    try:
        file_size = int(r.headers['content-length'])
    except:
        print("Invalid URL")
        return

    part = int(file_size) / count
    with open(local_filename,"wb") as fp:
        fp.write(b"\0" * file_size)

    for i in range(count):
        start = int(part) * i
        end = start + part
        # create a Thread with start and end locations
        t = threading.Thread(target=Handler,
                             kwargs={'start': start, 'end': end, 'url': url, 'filename': local_filename})
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


if __name__ == '__main__':
    download_file(obj={})

