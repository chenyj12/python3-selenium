import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)

import unittest
from Base.log import log1
from Base.browser_engine import *
from Base.browser_engine import BrowserEngine


class Start(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        log1.info('-----退出浏览器-----')
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
