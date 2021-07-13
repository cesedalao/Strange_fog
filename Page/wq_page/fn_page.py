import time

from selenium.webdriver.common.by import By

from Base.wq_base import BasePage, BaseHanble
from utils import DriverUtils


class AmBasePage3(BasePage):
    def __init__(self):
        super().__init__()

        # 点击导出门店
        self.c3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[2]/span')
        # 门店导入确定
        self.c4 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[6]/div/div[3]/span/button[2]/span')
        # 点击导出店铺
        self.c5 = (By.XPATH,
                   '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[3]/span')
        # 点击导出公众号
        self.c6 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[4]/span')
        self.cc3 = (By.XPATH, '//*[@id="exportDialog"]/div/div/div[2]/div/div[1]/div/input')
        # 点击保存导出公众号
        self.s1 = (By.XPATH, '//*[@id="exportDialog"]/div/div/div[3]/span/button[1]/span')
        # 点击后台管理
        self.s2 = (By.XPATH, '//*[@id="topVersionId"]/ul/li[7]/a')
        # 点击线下管理
        self.s3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/div/aside/ul/div/ul/div[1]/li/ul/li/ul/li[2]')
        # 点击导出小程序
        self.s4 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[5]/span')
        # 输入小程序名称
        self.s5 = (By.XPATH, '//*[@id="exportDialog"]/div/div/div[2]/div/div[1]/div/input')
        # 点击保存小程序
        self.cc1 = (By.XPATH, '//*[@id="exportDialog"]/div/div/div[3]/span/button[1]')
        self.ss2 = (By.XPATH, '//*[@id="topVersionId"]/ul/li[7]/a')
        # 点击线下管理
        self.ss3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/div/aside/ul/div/ul/div[1]/li/ul/li/ul/li[2]')

        # 点击公众号欢迎语设置
        self.cc2 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[6]/span')
        # 点击文字
        self.s6 = (By.XPATH,
                   '//*[@id="home-wrap"]/section/section/main/div/div[10]/div/div/div[2]/div/div[2]/div[1]/div/label[1]/span[1]/span')
        # 输入文字
        self.c7 = (
            By.XPATH,
            '//*[@id="home-wrap"]/section/section/main/div/div[10]/div/div/div[2]/div/div[2]/div[2]/div/textarea')
        # 确定
        self.c8 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[10]/div/div/div[3]/span/button[2]/span')
        # 点击banner 设置
        self.c9 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[7]/span')
        # 点击编辑
        self.c10 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/div/div/div[3]/button[1]/span')
        # 更改名称
        self.s7 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/div[1]/div/input')
        # 点击保存
        self.c11 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[2]/span')

    def find_c4(self):
        return self.fd_el(self.c4)

    def find_c3(self):
        return self.fd_el(self.c3)

    def find_c5(self):
        return self.fd_el(self.c5)

    def find_c6(self):
        return self.fd_el(self.c6)

    def find_cc3(self):
        return self.fd_el(self.cc3)

    def find_s1(self):
        return self.fd_el(self.s1)

    def find_s2(self):
        return self.fd_el(self.s2)

    def find_s3(self):
        return self.fd_el(self.s3)

    def find_s4(self):
        return self.fd_el(self.s4)

    def find_s5(self):
        return self.fd_el(self.s5)

    def find_cc1(self):
        return self.fd_el(self.cc1)

    def find_ss2(self):
        return self.fd_el(self.ss2)

    def find_ss3(self):
        return self.fd_el(self.ss3)

    def find_cc2(self):
        return self.fd_el(self.cc2)

    def find_s6(self):
        return self.fd_el(self.s6)

    def find_c7(self):
        return self.fd_el(self.c7)

    def find_c8(self):
        return self.fd_el(self.c8)

    def find_c9(self):
        return self.fd_el(self.c9)

    def find_c10(self):
        return self.fd_el(self.c10)

    def find_s7(self):
        return self.fd_el(self.s7)

    def find_c11(self):
        return self.fd_el(self.c11)


class AmBaseHanble3(BaseHanble):
    def __init__(self):
        self.log_page = AmBasePage3()

    def c3(self):
        self.log_page.find_c3().click()

    def c4(self):
        self.log_page.find_c4().click()

    def c5(self):
        self.log_page.find_c5().click()

    def c6(self):
        self.log_page.find_c6().click()

    def cc3(self, sh):
        self.ip_text(self.log_page.find_cc3(), sh)

    def s1(self):
        self.log_page.find_s1().click()

    def s2(self):
        self.log_page.find_s2().click()

    def s3(self):
        self.log_page.find_s3().click()

    def s4(self):
        self.log_page.find_s4().click()

    def s5(self, s5):
        self.ip_text(self.log_page.find_s5(), s5)

    def cc1(self):
        self.log_page.find_cc1().click()

    def ss2(self):
        self.log_page.find_ss2().click()

    def ss3(self):
        self.log_page.find_ss3().click()

    def cc2(self):
        self.log_page.find_cc2().click()

    def s6(self):
        self.log_page.find_s6().click()

    def c7(self, c7):
        self.ip_text(self.log_page.find_c7(), c7)

    def c8(self):
        self.log_page.find_c8().click()

    def c9(self):
        self.log_page.find_c9().click()

    def c10(self):
        self.log_page.find_c10().click()

    def s7(self, s7):
        self.ip_text(self.log_page.find_s7(), s7)

    def c11(self):
        self.log_page.find_c11().click()


class AmPorxy3:
    def __init__(self):
        self.driver = DriverUtils.get_wq_driver()
        self.logg_page = AmBaseHanble3()

    def test_login(self, sh):
        self.logg_page.c3()
        time.sleep(2)
        self.logg_page.c4()
        time.sleep(2)
        self.logg_page.c5()
        time.sleep(3)
        self.logg_page.c6()

        self.logg_page.cc3(sh)
        time.sleep(1)
        self.logg_page.s1()
        time.sleep(2)
        self.logg_page.s2()
        time.sleep(1)
        self.logg_page.s3()
        time.sleep(1)
        self.logg_page.s4()
        time.sleep(1)

    def test_xcx(self, s5):
        self.logg_page.s5(s5)
        time.sleep(2)
        self.logg_page.cc1()
        time.sleep(2)
        self.logg_page.ss2()
        time.sleep(2)
        self.logg_page.ss3()
        time.sleep(1)
        self.logg_page.cc2()
        time.sleep(1)
        self.logg_page.s6()
        time.sleep(1)

    def test_yysz(self, c7):
        self.logg_page.c7(c7)
        time.sleep(1)
        self.logg_page.c8()
        time.sleep(1)
        self.logg_page.c9()
        self.logg_page.c10()
        time.sleep(1)

    def test_banner(self, s7):
        self.logg_page.s7(s7)
        self.logg_page.c11()
