from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from base.base_page import BasePage


class LoginPage(BasePage):
    url = BasePage.url + '?s=/index/user/logininfo.html'
    user = (By.NAME, 'accounts')
    pwd = (By.NAME, 'pwd')
    button = (By.XPATH, '/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button')
    ass = (By.XPATH, '//div[@id="common-prompt"]/p')
    href = (By.XPATH, '//a[text()="忘记密码？"]')

    # 登录#
    def login(self, username, password):
        self.open()
        self.input_(self.user, username)
        self.input_(self.pwd, password)
        self.click(self.button)

    # 获取标签文本#
    def assert_txt(self):
        return self.assert_text(self.ass)

    # 点击忘记密码#
    def forget(self):
        self.open()
        self.click(self.href)


# if __name__ == '__main__':
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     ln = LoginPage(driver)
#     username = '635193961'
#     pwd = '635193961'
#     ln.login(username, pwd)
#     sleep(0.5)
#     text = ln.assrt()
#     print(text)
