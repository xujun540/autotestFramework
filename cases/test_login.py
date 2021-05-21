import pytest
from conf.yaml_driver import load_yaml
from page_object.login_page import LoginPage
from page_object.product_page import ProductPage


class TestLogin:

    @pytest.mark.parametrize('data', load_yaml('../data/user.yaml'))
    def test_login(self, data, browser):
        lg = LoginPage(browser)
        lg.login(data['user'], data['pwd'])
        print('这是一个登录的')

    def test_add_cart(self, browser):
        pg = ProductPage(browser)
        pg.addcart()


if __name__ == '__main__':
    pytest.main(['test_login.py', '-s'])
