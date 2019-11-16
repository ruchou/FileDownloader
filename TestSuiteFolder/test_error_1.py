import unittest
from Downloader import *
from click.testing import CliRunner

class MyTestCase(unittest.TestCase):
    #invalid url
    def test_1(self):
        url = 'http://oak.cs.ucla.edu/classes/cs246/projects/fdsjlfjsdlkfjs.sh'
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url,'-c','5'])
        self.assertEqual(0, result.exit_code)
        self.assertIn("error",result.output)

    #  invalid thread
    def test_2(self):
        url = 'http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh'
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url, '-c', '-1'])
        self.assertEqual(0, result.exit_code)
        self.assertIn("number of threads must be larger than 0", result.output)

if __name__ == '__main__':
    unittest.main()
