import unittest
from Downloader import *
from click.testing import CliRunner

class MyTestCase(unittest.TestCase):

    #sample file test
    def test_1(self):
        url = 'http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh'
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url,'-c','1'])
        self.assertEqual(0, result.exit_code)

    #mp3 file test
    def test_2(self):
        url = "http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3"
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url, '-c', '2'])
        self.assertEqual(0, result.exit_code)

    # larger mp3 file test
    def test_3(self):
        url = "http://www.hochmuth.com/mp3/Beethoven_12_Variation.mp3"
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url, '-c', '5'])
        self.assertEqual(0, result.exit_code)
    # larger mp3 file test
    def test_4(self):
        url = "http://ipv4.download.thinkbroadband.com/200MB.zip"
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url, '-c', '20'])
        self.assertEqual(0, result.exit_code)
if __name__ == '__main__':
    unittest.main()
