import logging

from utils import DriverUtils

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_wq_driver()

    def fd_el(self, location):
        logging.info('开始定位{}的元素'.format(location))
        try:
            el = WebDriverWait(self.driver, 5, 1).until(lambda x: x.find_element(*location))
            return el
        except Exception as e:
            logging.error('无法定位{}得元素'.format(location))


class BaseHanble:

    def ip_text(self, el, text):
        el.clear()
        el.send_keys(text)
