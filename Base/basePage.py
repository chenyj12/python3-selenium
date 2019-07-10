import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)

import getcwd
from Base.log import log1
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class BasePase():
    """测试基类"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, selector):
        # 定位元素
        by = selector[0]
        value = selector[1]
        element = None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    log1.error('没有找到元素，定位方式:%s,使用的是：%'%(by,value))
                return element
            except NoSuchElementException:
                log1.error("报错信息：")
        else:
            log1.info('没有找到元素')

    @staticmethod  # 设置静态方法注解
    def isdisplayed(element):
        value = element.isdisplayed()
        return value

    def is_element_exsist(self, selector):
        '''
           结合WebDriverWait和expected_conditions判断元素是否存在,
           每间隔1秒判断一次，20s超时，存在返回True,不存返回False
        '''
        try:
            WebDriverWait(self.driver, 20, 1).until(EC.presence_of_element_located(selector))
            return True
        except Exception as msg:
            log1.info("元素找不到：%s" % (selector, msg))
            return False

    @staticmethod
    def sleep(secondes):
        time.sleep(secondes)
        log1.info("等待了%d秒", secondes)

    def click(self, selector):
        """点击元素"""
        element = self.find_element(selector)
        try:
            element.click()
            log1.info('点击元素成功')
        except BaseException:
            isdisplay = self.isdisplayed(element)
            if isdisplay is True:
                self.sleep(3)
                element.click()
                log1.info('点击元素成功')
            else:
                log1.error('点击元素报错', exc_info=1)
                self.get_img()

    def inputs(self, selector, value):
        """往输入框输入内容"""
        element = self.find_element(selector)
        element.clear()
        try:
            element.send_keys(value)
            log1.info('输入的内容：%s' % value)
        except BaseException:
            log1.error('内容输入报错', exc_info=1)
            self.get_img()

    def get_img(self):
        """截图方法"""
        img_path = os.path.join(getcwd.get_cwd(), 'Screenshots/')
        # 判断如果文件夹不存在，则创建一个
        if not os.path.join(img_path):
            os.makedirs(img_path)
        # 获取当前时间
        local_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 日期文件夹路径
        date_file_path = os.path.join(img_path, local_date)
        # 判断日期文件夹是否存在，新建该文件夹
        if not os.path.exists(date_file_path):
            os.makedirs(date_file_path)
        # 截图存放路径
        local_time = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        jt_name = local_time + '.png'
        jt_path = os.path.join(date_file_path, jt_name)
        try:
            self.driver.get_screenshot_as_file(jt_path)
            log1.info('截图保存成功')
        except BaseException:
            log1.error('截图失败', exc_info=1)

    def get_title(self):
        """获取标题"""
        title = self.driver.title
        log1.info("当前页面的title为%s" % title)
        return title

    def get_text(self, selector):
        """获取text"""
        element = self.find_element(selector)
        text = element.text
        log1.info("获取的text：%s" % text)
        return text

    def forward(self):
        self.driver.forward()
        log1.info('前进一步')

    def back(self):
        self.driver.back()
        log1.info('后退一步')

    def switch_ifarme(self, selector):
        """切换ifarme"""
        element = self.find_element(selector)
        try:
            self.driver.switch_to.frame(element)
            log1.info('切换frame成功')
        except BaseException:
            log1.error('切换frame报错', exc_info=1)

    def get_handle(self):
        """获得当前handle"""
        handle = self.driver.current_window_handle
        return handle

    def chage_handle(self, handle):
        """切换窗口"""
        handles = self.driver.window_handles
        for i in handles:
            if i != handle:
                self.driver.switch_to_window(i)
