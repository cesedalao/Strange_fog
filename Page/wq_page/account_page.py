import time

from selenium.webdriver.common.by import By

from Base.wq_base import BasePage, BaseHanble
from utils import DriverUtils


class AmBasePage1(BasePage):
    def __init__(self):
        super().__init__()
        # 点击店铺管理
        self.c1 = (By.XPATH, '//*[@id="sideNavigationAccordion"]/li[1]/a/span[2]')
        # 点击店铺管理YQZ
        self.c2 = (By.XPATH, '//*[@id="sideNavigationAccordion"]/li[3]/a/span[2]')
        # 点击用户列表
        self.c3 = (By.XPATH, '//*[@id="navigationSubMenuGroup3"]/li[1]/a/span[2]')
        # 模糊查询
        self.s1 = (By.XPATH, '//*[@id="keyWords"]')
        # 点击查询
        self.c4 = (By.XPATH, '//*[@id="searchButton"]')
        # 点击更多
        self.c5 = (By.XPATH,
                   '//*[@class="table table-striped table-hover table-condensed emay-base-table"]/tbody/tr[2]/td[13]/div/button[2]')
        # 点击正式账号
        self.c6 = (By.XPATH, '//*[@id="tableRender"]/table/tbody/tr[2]/td[13]/div/ul/li[1]/a')
        # 进入管理
        self.c7 = (By.XPATH, "//*[contains(text(),'进入管理')]")
        # 进入后台管理
        self.c8 = (By.XPATH, '//*[@class="navbar-header bootstrap-top14-nav14"]/ul/li[7]')

    def find_c1(self):
        return self.fd_el(self.c1)

    def find_c2(self):
        return self.fd_el(self.c2)

    def find_c3(self):
        return self.fd_el(self.c3)

    def find_s1(self):
        return self.fd_el(self.s1)

    def find_c4(self):
        return self.fd_el(self.c4)

    def find_c5(self):
        return self.fd_el(self.c5)

    def find_c6(self):
        return self.fd_el(self.c6)

    def find_c7(self):
        return self.fd_el(self.c7)

    def find_c8(self):
        return self.fd_el(self.c8)


class AmBaseHanble1(BaseHanble):
    def __init__(self):
        self.log_page = AmBasePage1()

    def c1(self):
        self.log_page.find_c1().click()

    def c2(self):
        self.log_page.find_c2().click()

    def c3(self):
        self.log_page.find_c3().click()

    def s1(self, s):
        self.ip_text(self.log_page.find_s1(), s)

    def c4(self):
        self.log_page.find_c4().click()

    def c5(self):
        self.log_page.find_c5().click()

    def c6(self):
        self.log_page.find_c6().click()

    def c7(self):
        self.log_page.find_c7().click()

    def c8(self):
        self.log_page.find_c8().click()


class AmPorxy1:
    def __init__(self):
        self.driver = DriverUtils.get_wq_driver()
        self.logg_page = AmBaseHanble1()

    def test_login(self, s):
        self.logg_page.c1()
        time.sleep(0.5)

        self.logg_page.c2()

        self.logg_page.c3()

        self.logg_page.s1(s)
        time.sleep(1)

        self.logg_page.c4()

        self.logg_page.c5()
        time.sleep(1)

        self.logg_page.c6()
        time.sleep(1)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.logg_page.c7()
        time.sleep(1)

        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.logg_page.c8()
        time.sleep(1)
