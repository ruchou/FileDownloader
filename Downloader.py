#!/usr/bin/env python

# $ ./downloader <URL> -c nThreads
import requests
import sys, getopt
import os
import threading
import click
from requests.adapters import HTTPAdapter


def Handler(start, end, url, filename):
    # specify the starting and ending of the file
    headers = {'Range': 'bytes=%d-%d' % (start, end)}
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    try:
        r = s.get(url, headers=headers, stream=True)
    except requests.exceptions.RequestException as e:
        print(e)
        exit(0)

    # open the file and write the content of the file
    with open(filename, "r+b") as fp:
        fp.seek(start)
        var = fp.tell()
        fp.write(r.content)

@click.command(help="It downloads the specified file with associated name")
@click.option('-c',default=4, help="No of Threads")
@click.argument('url',type=click.Path())
@click.pass_context
def download_file(ctx,url,c):
    # parse arguments
    local_filename = url.split('/')[-1]
    if not local_filename :
        click.echo('Unknown file name')
        exit(0)
    if c <= 0:
        click.echo("number of threads must be larger than 0")
        exit(0)

    #Send Http head
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    try:
        r = s.head(url)
        file_size = int(r.headers['content-length'])
    except requests.exceptions.RequestException as e:
        print(e)
        exit(0)
    except:
        click.echo('error')
        exit(0)

    part = int(file_size) / c
    #create files
    with open(local_filename,"wb") as fp:
        fp.write(b"\0" * file_size)

    #download files in parallel
    for i in range(c):
        start = int(part) * i
        end = start + part
        t = threading.Thread(target=Handler,
                             kwargs={
                                         'start': start,
                                         'end': end,
                                         'url': url,
                                         'filename': local_filename
                                    }
                             )
        t.setDaemon(True)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


if __name__ == '__main__':
    download_file(obj={})

