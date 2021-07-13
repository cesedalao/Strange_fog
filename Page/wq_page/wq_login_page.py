import time

from selenium.webdriver.common.by import By

from Base.wq_base import BasePage, BaseHanble


class AmBasePage(BasePage):
    def __init__(self):
        super().__init__()
        # 输入手机号码
        self.s1 = (By.XPATH, '//*[@id="phoneNumber"]')
        # 获取验证码
        self.c1 = (By.XPATH, '//*[@id="getCode"]')
        # 点击登录
        self.c2 = (By.XPATH, '//*[@id="loginButton"]')

    def find_s1(self):
        return self.fd_el(self.s1)

    def find_c1(self):
        return self.fd_el(self.c1)

    def find_c2(self):
        return self.fd_el(self.c2)


class AmBaseHanble(BaseHanble):
    def __init__(self):
        self.log_page = AmBasePage()

    def s1(self, s):
        self.ip_text(self.log_page.find_s1(), s)

    def c1(self):
        self.log_page.find_c1().click()

    def c2(self):
        self.log_page.find_c2().click()


class AmPorxy:
    def __init__(self):
        self.logg_page = AmBaseHanble()

    def test_login(self, s):
        self.logg_page.s1(s)

        self.logg_page.c1()
        time.sleep(30)

        self.logg_page.c2()
        time.sleep(3)
