import unittest
from Base.start import Start
from Pages.loginpage import LoginPage


class Test01(Start):
    """测试登录"""
    def test(self):
        '''测试登录用例，账号：xx 密码xx'''

        title = self.driver.title
        print(title)

    def test_login01(self):
        '''测试登录用例，账号：xx 密码xx'''

        lo = LoginPage(self.driver)
        lo.login_action('admin', 'a23')
        self.assertFalse(lo.check_loginStatus(), msg='成功')


if __name__ == '__main__':
    unittest.main()

