import time

from base.base_driver import get_driver
from page.page import Page


class TestUpdate:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_update(self):
        # 点击设置按钮
        self.page.user_center.page_click_setting(self.page)
        # 点击关于百年奥莱
        self.page.setting.page_click_about()
        # 点击版本更新
        self.page.update.page_click_update()
        # 断言toast值是否为当前已是最新版本
        assert self.page.update.base_is_exist_toast("当前已是最新版本")
