from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from base.base_page import BasePage


class ProductPage(BasePage):
    url = BasePage.url + '?s=/index/goods/index/id/2.html'

    suite = (By.XPATH, '//li[@data-value="套餐一"]')
    color = (By.XPATH, '//li[@data-value="金色"]')
    memory = (By.XPATH, '//li[@data-value="32G"]')
    cart = (By.XPATH, '//*[@title="加入购物车"]')

    def addcart(self):
        self.open()
        self.click(self.suite)
        sleep(1)
        self.click(self.color)
        sleep(1)
        self.click(self.memory)
        sleep(1)
        self.click(self.cart)
