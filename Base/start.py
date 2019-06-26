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
    #
    # def test(self):
    #     title = self.driver.title
    #     print(title)

if __name__ == '__main__':
    unittest.main()