from Base.basePage import BasePase
from Base.log import log1
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePase):
    UserNameOrPhone = ['name', 'userNameOrPhone']
    Password = ['name', 'password']
    Sign_button = ['tag', 'button']  # 登录按钮
    logout = ['class', 'fa fa-ls fa-sign-out']  # 退出按钮
    quding = ['class', 'el-button el-button--default el-button--small el-button--primary ']
    Act_name=['xpath','//*[@id="app"]/div/section/aside/div/div[1]/div[1]/p']

    def input_phone(self, value):
        self.inputs(self.UserNameOrPhone, value)

    def input_password(self, value):
        self.inputs(self.Password, value)

    def login_click(self):
        self.click(self.Sign_button)

    def login(self, name, pwd):
        log1.info('-----执行登录操作-----')
        self.driver.get('http://quark.backend.hktqa.cn')
        self.input_phone(name)
        self.input_password(pwd)
        self.login_click()

    def login_out(self):
        log1.info('-----执行退出账号操作-----')
        self.click(self.logout)
        self.click(self.quding)

    def check_login(self):
        log1.info('-----检查登录信息-----')
        try:
            element = self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[1]/div[1]/p').text
            log1.info('登录成功，账号为%s' % element)
        except NoSuchElementException:
            log1.error('登录失败')
            return False
        else:
            return True
