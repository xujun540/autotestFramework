import pytest
from conf.yaml_driver import load_yaml
from page_object.login_page import LoginPage
from page_object.product_page import ProductPage


class TestCases:

    @pytest.mark.parametrize('data', load_yaml('../data/user.yaml'))
    def test_login(self, data, browser):
        lg = LoginPage(browser)
        lg.login(data['user'], data['pwd'])
        text = lg.assert_text()
        assert text == data['text']

    def test_add_cart(self, browser):
        pg = ProductPage(browser)
        pg.addcart()


if __name__ == '__main__':
    pytest.main(['case_demo.py', '-s'])
