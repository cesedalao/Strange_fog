import logging

import time
import allure
import pytest

from Page.wq_page.account_page import AmPorxy1

from Page.wq_page.add_store_page import AmPorxy2
from Page.wq_page.fn_page import AmPorxy3

from Page.wq_page.wq_login_page import AmPorxy

from utils import DriverUtils, is_exts, wq_data

import logging


class TestWq:
    @classmethod
    def setup_class(cls):
        cls.driver = DriverUtils.get_wq_driver()
        cls.driver.get('https://h.jkcrm.cn/login.do')

    # 登录
    @allure.severity(allure.severity_level.BLOCKER)
    def test_wq01(self):
        AmPorxy().test_login(19131222371)

        logging.info('开始断言登录是否成功')
        try:
            assert is_exts(self.driver, '后台管理')
        except Exception as e:
            print('抱歉登录失败了')
        else:
            print('恭喜你登录集客CRM后台管理成功了')

    # 进入云千载测试账号

    @allure.severity(allure.severity_level.BLOCKER)
    def test_wq02(self):
        AmPorxy1().test_login('云千载测试账号')

        logging.info('开始断言进入云千载测试账号是否成功')
        try:
            assert is_exts(self.driver, '线下门店')
        except Exception as e:
            print('抱歉登录云千载后台管理失败了')
        else:
            print('恭喜你进入云千载测试账号成功')

    # 添加线下门店

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("bm_name", "dp_name", "dz_name", "fzr_name", "ph", "jzd_name"),
                             wq_data('E:/my_python/Strange fog/data/score.json'))
    @pytest.mark.repeat(2)
    def test_wq03(self, bm_name, dp_name, dz_name, fzr_name, ph, jzd_name):
        # 添加时间格式防止重复
        bm = bm_name.format(time.strftime('%H%M%S'))
        dp = dp_name.format(time.strftime('%H%M%S'))

        AmPorxy2().test_login(bm, dp, dz_name, fzr_name, ph, jzd_name)
        logging.info('开始断言添加线下门店是否成功')
        # 添加截图
        allure.attach(self.driver.get_screenshot_as_png(), "添加下线门店结果", allure.attachment_type.PNG)

        try:
            assert is_exts(self.driver, '13522344046')
        except Exception as e:
            print('抱歉添加线下门店失败了')
        else:
            print('恭喜你添加线下门店成功')

    @allure.severity(allure.severity_level.CRITICAL)
    def test_wq04(self):
        AmPorxy3().test_login('测试116')
        logging.info('开始断言导出公众号是否成功')

        allure.attach(self.driver.get_screenshot_as_png(), '导出公众号结果', allure.attachment_type.PNG)

        try:
            assert is_exts(self.driver, '完成')
        except Exception as e:
            print('抱歉导出公众失败了失败了')
        else:
            print('恭喜你导出公众号成功')

        AmPorxy3().test_xcx('测试117')
        logging.info('开始断言导出小程序是否成功')
        allure.attach(self.driver.get_screenshot_as_png(), '导出小程序结果', allure.attachment_type.PNG)

        try:
            assert is_exts(self.driver, '完成')
        except Exception as e:
            print('抱歉导出小程序失败了')
        else:
            print('恭喜你导出小程序成功')

        AmPorxy3().test_yysz(456)

        AmPorxy3().test_banner(4567)
        logging.info('开始断言banner名称是否成功')
        allure.attach(self.driver.get_screenshot_as_png(), '修改banner名称结果', allure.attachment_type.PNG)
        try:
            assert is_exts(self.driver, '789')
        except Exception as e:
            print('抱歉修改banner名称失败了')
        else:
            print('恭喜你修改banner名称成功')

    @classmethod
    def teardown_class(cls):
        DriverUtils.wq_quit()


if __name__ == "__main__":
    pytest.main()
