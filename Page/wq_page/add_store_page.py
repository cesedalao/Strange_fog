import time

from selenium.webdriver.common.by import By

from Base.wq_base import BasePage, BaseHanble
from utils import DriverUtils


class AmBasePage2(BasePage):
    def __init__(self):
        super().__init__()

        # 点击线下门店
        self.c3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/div/aside/ul/div/ul/div[1]/li/ul/li/ul/li[2]')
        # 点击添加门店
        self.c4 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[1]/span')
        # 点击店铺类型
        self.c5 = (By.XPATH,
                   '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[1]/div/div/div[2]/span/span/i')
        # 点击专卖店
        self.c6 = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span')
        self.cc3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[1]')
        # 输入编码
        self.s1 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[2]/div/div[1]/input')
        # 输入店铺名称
        self.s2 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[3]/div/div[1]/input')
        # 输入详细地址
        self.s3 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[7]/div/div[1]/input')
        # 输入负责人
        self.s4 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[8]/div/div/input')
        # 输入电话
        self.s5 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[9]/div/div[1]/input')
        # 点击营业时间
        self.cc1 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[10]/div/div/input[1]')
        # 确认时间
        self.cc2 = (By.XPATH, '//*[@class="el-time-panel__footer"]/button[2]')
        # 输入经纬度
        self.s6 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[12]/div/div[2]/input')
        # 检索
        self.c7 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[2]/form/div[12]/div/button/span')
        # 确定
        self.c8 = (By.XPATH, '//*[@id="home-wrap"]/section/section/main/div/div[3]/button[2]')

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

    def find_cc2(self):
        return self.fd_el(self.cc2)

    def find_s6(self):
        return self.fd_el(self.s6)

    def find_c7(self):
        return self.fd_el(self.c7)

    def find_c8(self):
        return self.fd_el(self.c8)


class AmBaseHanble2(BaseHanble):
    def __init__(self):
        self.log_page = AmBasePage2()

    def c3(self):
        self.log_page.find_c3().click()

    def c4(self):
        self.log_page.find_c4().click()

    def c5(self):
        self.log_page.find_c5().click()

    def c6(self):
        self.log_page.find_c6().click()

    def cc3(self):
        self.log_page.find_cc3().click()

    def s1(self, s1):
        self.ip_text(self.log_page.find_s1(), s1)

    def s2(self, s2):
        self.ip_text(self.log_page.find_s2(), s2)

    def s3(self, s3):
        self.ip_text(self.log_page.find_s3(), s3)

    def s4(self, s4):
        self.ip_text(self.log_page.find_s4(), s4)

    def s5(self, s5):
        self.ip_text(self.log_page.find_s5(), s5)

    def cc1(self):
        self.log_page.find_cc1().click()

    def cc2(self):
        self.log_page.find_cc2().click()

    def s6(self, s6):
        self.ip_text(self.log_page.find_s6(), s6)

    def c7(self):
        self.log_page.find_c7().click()

    def c8(self):
        self.log_page.find_c8().click()


class AmPorxy2:
    def __init__(self):
        self.driver = DriverUtils.get_wq_driver()
        self.logg_page = AmBaseHanble2()

    def test_login(self, s1, s2, s3, s4, s5, s6):
        self.logg_page.c3()
        time.sleep(2)
        self.logg_page.c4()
        time.sleep(1)
        self.logg_page.c5()
        time.sleep(1)
        self.logg_page.c6()
        self.logg_page.cc3()
        time.sleep(1)
        self.logg_page.s1(s1)
        self.logg_page.s2(s2)
        time.sleep(1)
        self.logg_page.s3(s3)
        self.logg_page.s4(s4)
        time.sleep(1)
        self.logg_page.s5(s5)
        time.sleep(2)
        self.logg_page.cc1()
        time.sleep(2)
        self.logg_page.cc2()
        time.sleep(1)
        self.logg_page.s6(s6)
        time.sleep(1)
        self.logg_page.c7()
        time.sleep(1)
        self.logg_page.c8()
        time.sleep(3)
