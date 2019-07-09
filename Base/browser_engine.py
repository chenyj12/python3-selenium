import os.path
from configparser import ConfigParser
from selenium import webdriver
from Base.log import log1


class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 当前文件相对路径获取方法
    chrome_driver_path = dir + '/Tools/chromedriver.exe'
    ie_driver_path = dir + '/Tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    # 从config.ini文件中读取浏览器类型，返回driver
    def open_browser(self, driver):
        config = ConfigParser()
        # 获取config配置文件地址
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        log1.info("选择的浏览器类型为：%s" % browser)
        if browser == "Firefox":
            driver = webdriver.Firefox()
            log1.info("Starting firefox browser.")
        elif browser == "Chrome":
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')  # 去除浏览器的警告
            # option.add_argument('headless')        #加载浏览器静默模式
            driver = webdriver.Chrome(chrome_options=option)
            # driver = webdriver.Chrome(self.chrome_driver_path)
            log1.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie(self.ie_driver_path)
            log1.info("Starting IE browser.")
        # driver.get(url)
        # log1.info("打开 url: %s" % url)
        driver.maximize_window()
        log1.info("Maximize the current window.")
        driver.implicitly_wait(10)
        log1.info("Set implicitly wait 10 seconds.")
        return driver

    def quit_browser(self):
        self.driver.quit()
        log1.info("退出当前浏览器")
