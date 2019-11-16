import unittest
from Downloader import *
from click.testing import CliRunner

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    #sample file test
    def test_1(self):
        url = 'http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh'
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url,'-c','5'])
        self.assertEqual(0, result.exit_code)

    #mp3 file test
    def test_2(self):
        url = "http://www.hochmuth.com/mp3/Haydn_Cello_Concerto_D-1.mp3"
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url, '-c', '5'])
        self.assertEqual(0, result.exit_code)

if __name__ == '__main__':
    unittest.main()
