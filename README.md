
To install:

    pip install -r requirements.txt 

To run program:
    
     ./downloader <URL> -c nThreads
 
Example:

    ./Downloader.py http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh
    ./Downloader.py http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh -c 5


Architecture:

    First, HTTP Head request to check the file size
    Second, divide the file size by the number of threads to download file
    Finally, download the files in parallel and merge into the one file
    