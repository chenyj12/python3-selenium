
from Base.basePage import BasePase
from Base.log import log1
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePase):
    userNameOrPhone = ['name', 'userNameOrPhone']
    password = ['name', 'password']
    button = ['tag', 'button']
    loginCount = ['xpath', '//*[@id="side-menu"]/li[1]/div[1]/a/span/span[2]']
    logout = ['xpath', '//*[@id="side-menu"]/li[1]/div[1]/ul/li[4]/a']
    quding = ['xpath', '/html/body/div[3]/div[3]/a[1]/span/span']

    def input_phone(self, value):
        self.inputs(self.userNameOrPhone, value)

    def input_password(self, value):
        self.inputs(self.password, value)

    def login_click(self):
        self.click(self.button)

    def login_action(self, phone1, passward1):
        log1.info('-----执行登录操作-----')
        self.driver.get('http://.cn')
        self.input_phone(phone1)
        self.input_password(passward1)
        self.login_click()


    def login_out(self):
        log1.info('-----执行退出账号操作-----')
        self.click(self.loginCount)
        self.click(self.logout)
        self.click(self.quding)

    def check_loginStatus(self):
        log1.info('-----检查登录信息-----')
        try:
            element=self.driver.find_element_by_xpath('//*[@id="app"]/div/section/aside/div/div[1]/div[1]/p').text
            log1.info('已登录，账号为%s'%element)
        except NoSuchElementException:
            log1.error('登录失败')
            return False
        else:
            # self.login_out()
            return True