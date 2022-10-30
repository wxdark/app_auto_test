import allure

import page
from base.base import Base


class PageLogin(Base):
    # 输入账号
    @allure.step(title='登录页 输入账号')
    def page_input_account(self, account):
        allure.attach("输入：", account)
        self.base_input(page.login_input_account, account)

    # 输入密码
    @allure.step(title='登录页 输入密码')
    def page_input_pwd(self, pwd):
        self.base_input(page.login_input_pwd, pwd)

    # 点击登录
    @allure.step(title='登录页 点击 登录按钮')
    def page_click_login_btn(self):
        self.base_click_element(page.login_btn)

    # 登录页组合方法
    def page_login(self, account, pwd):
        self.page_input_account(account)
        self.page_input_pwd(pwd)
        self.page_click_login_btn()
