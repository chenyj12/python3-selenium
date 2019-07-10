""" 
@author: chenyj
@file: testLogin.py 
@time: 2019/7/9 15:21 
"""
import os,sys
curPath = os.path.abspath(os.path.dirname(__file__))
Path = os.path.split(curPath)[0]
sys.path.append(Path)

import unittest
from Base.start import Start
from Pages.loginpage import LoginPage
from Base.log import log1


class TestLogin(Start):
    """测试登录功能"""

    def test_login1(self):
        '''用户名为空'''
        case_name = '用户名为空'
        lo = LoginPage(self.driver)
        lo.login('', '12323')
        try:
            self.assertFalse(lo.check_login())
            log1.info("测试用例执行成功：%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name + '\n')
            raise

    def test_login2(self):
        '''密码为空'''
        case_name = '密码为空'
        lo = LoginPage(self.driver)
        lo.login('gadmin', '')
        try:
            self.assertFalse(lo.check_login())
            log1.info("测试用例执行成功：%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name + '\n')
            raise

    def test_login3(self):
        '''密码错误'''
        case_name = '密码错误'
        lo = LoginPage(self.driver)
        lo.login('gadmin', '123456')
        try:
            self.assertFalse(lo.check_login())
            log1.info("测试用例执行成功：%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name + '\n')
            raise

    def test_login4(self):
        '''用户名和密码正确'''
        case_name = '用户名和密码正确'
        lo = LoginPage(self.driver)
        lo.login('gadmin', 'admin123')
        try:
            self.assertTrue(lo.check_login())
            log1.info("测试用例执行成功：%s" % case_name + '\n')
        except AssertionError:
            log1.error("测试用例执行失败：%s" % case_name + '\n')
            raise


if __name__ == '__main__':
    unittest.main
