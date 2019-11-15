import unittest
from Downloader import *
from click.testing import CliRunner

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_1(self):
        url = 'http://oak.cs.ucla.edu/classes/cs246/projects/p3_test.sh'
        runner = CliRunner()
        result = runner.invoke(
            download_file, [url,'-c','5'])
        self.assertEqual(0, result.exit_code)
        # self.assertIn('Find: 3 sample', result.output)


        # download_file(obj={})

if __name__ == '__main__':
    unittest.main()
