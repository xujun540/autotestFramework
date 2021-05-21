import requests
from selenium import webdriver

from base.base_page import BasePage
from chrome_options.options import Options
from page_object.login_page import LoginPage

'''
这是pytest中的预置函数定义的配置文件：注意，文件名称一定是conftest。不能是其他的
scope参数定义的4种等级（默认等级是function）：
    session：在本次session级别中只执行一次
    module：在模块级别中只执行一次
    class：在类级别中只执行一次
    function：在函数级别中执行，每有一个函数就执行一次 。。
'''
import pytest


# 预置函数：用于前期的数据准备
@pytest.fixture(scope='class')
def browser():
    driver = webdriver.Chrome(options=Options().conf_option())
    return driver


