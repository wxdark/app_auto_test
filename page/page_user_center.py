import time

import allure

import page
from base.base import Base


class PageUserCenter(Base):
    # 获取用户昵称
    @allure.step(title='个人中心 获取 用户昵称')
    def page_get_nickname_text(self):
        return self.base_get_text(page.user_center_nickname)

    # 点击设置按钮
    @allure.step(title='个人中心  点击  设置')
    def page_click_setting(self, page_object):
        # 判断当前是否登录
        page_object.home.page_if_login_in(page_object)
        self.base_click_element(page.user_setting)

    # 点击加入超级VIP
    @allure.step(title='个人中心 点击 加入超级VIP')
    def page_click_join_vip(self):
        self.base_find_element_with_scroll(page.user_join_vip).click()
        time.sleep(2)

    # 新封装退出登录
    def page_click_logout(self):
        self.base_click_element(page.user_setting)
        self.base_find_element_with_scroll(page.setting_quit).click()
        self.base_click_element(page.setting_quit_enter)

