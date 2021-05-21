from logs.log import Logger
from selenium import webdriver
from time import sleep


class BasePage:
    url = 'http://39.98.138.157/shopxo/index.php'
    log = Logger().get_logger()

    # driver=webdriver.Chrome()
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(2)

    # 访问url
    def open(self):
        self.driver.get(self.url)
        self.log.info('访问url：{}'.format(self.url))

    # 元素定位
    def locator(self, loc):
        self.log.info('正在使用:{}定位,其定位元素为：{}'.format(loc[0], loc[1]))
        return self.driver.find_element(*loc)

    # 输入
    def input_(self, loc, txt):
        self.locator(loc).send_keys(txt)
        self.log.info('正在输入:{}'.format(txt))

    # 点击
    def click(self, loc):
        self.locator(loc).click()

    # 切换至Iframe窗体
    def switch_to_iframe(self, loc):
        self.driver.switch_to.frame(self.locator(*loc))

    # 获取属性
    def get_attr(self, loc, name):
        self.locator(loc).get_attribute(name)

    # 获取文本
    def assert_text(self, loc):
        return self.locator(loc).text


