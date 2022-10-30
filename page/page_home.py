import allure

import page
from base.base import Base


class PageHome(Base):
    # 关闭app更新弹窗
    @allure.step(title='首页 点击 关闭更新弹窗')
    def page_click_close_update(self):
        self.base_click_element(page.home_close_update)

    # 点击首页我的按钮
    @allure.step(title='首页 点击  我')
    def page_click_user_center(self):
        self.base_click_element(page.home_click_user)

    # 点击分类按钮
    @allure.step(title='首页 点击 分类')
    def page_click_category_btn(self):
        self.base_click_element(page.home_category)

    # 点击购物车
    @allure.step(title='首页 点击 购物车')
    def page_click_shop_cart(self):
        self.base_click_element(page.home_shop_cart)

    # 判断当时登录状态
    @allure.step(title='首页 登录 (如果没有登录的话)')
    def page_if_login_in(self, page):
        """
        :param page: 为页面对象入口
        :return:
        """
        self.page_click_user_center()
        # 获取当前界面名是否与登陆后界面名一致如果为已登录状态就什么都不做
        if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        # 如果为未登录则进行登录操作
        page.register.page_click_go_login()
        page.login.page_long_in("itheima_test", "itheima")
