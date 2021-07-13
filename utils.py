import selenium.webdriver

import json

from selenium.webdriver.support.wait import WebDriverWait


class DriverUtils:
    __wq_driver = None

    @classmethod
    def get_wq_driver(cls):
        if cls.__wq_driver is None:
            cls.__wq_driver = selenium.webdriver.Chrome()
            cls.__wq_driver.implicitly_wait(10)
            cls.__wq_driver.maximize_window()

        return cls.__wq_driver

    __qw_key = True

    @classmethod
    def wq_key(cls, key):
        cls.__qw_key = key

    @classmethod
    def wq_quit(cls):
        if cls.__wq_driver is not None and cls.__qw_key:
            cls.__wq_driver.quit()


def is_exts(driver, text):
    path_str = "//*[contains(text(),'{}')]".format(text)

    try:
        el = WebDriverWait(driver, 5, 1).until(lambda x: x.find_element_by_xpath(path_str))
    except Exception as e:
        el = False
    return el


def wq_data(filename):
    case_data = []
    with open(file=filename, encoding='utf-8')as f:
        dict_data = json.load(f)
        for i in dict_data.values():
            case_data.append(list(i.values()))

        return case_data

