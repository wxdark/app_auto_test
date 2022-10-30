import allure

import page
from base.base import Base


class PageSetting(Base):
    # 点击关于奥莱
    @allure.step(title='设置中心 点击 关于奥莱')
    def page_click_about(self):
        self.base_find_element_with_scroll(page.setting_about).click()

    # 点击清理缓存
    @allure.step(title='设置中心 点击 清理缓存')
    def page_click_clear_cache(self):
        self.base_find_element_with_scroll(page.setting_clear_cache).click()

    # 点击地址管理
    @allure.step(title='设置中心 点击 地址管理')
    def page_click_address_manage(self):
        self.base_find_element_with_scroll(page.setting_address).click()

    # 点击退出登录
    @allure.step(title='设置中心-设置-退出-确认')
    def page_click_quit(self, page_object):
        page_object.user_center.page_click_setting()
        self.base_find_element_with_scroll(page.setting_quit).click()
        self.base_click_element(page.setting_quit_enter)