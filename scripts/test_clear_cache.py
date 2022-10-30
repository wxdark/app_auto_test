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

    def test_clear_cache(self):
        # 点击设置按钮
        self.page.user_center.page_click_setting(self.page)
        # 点击清理缓存
        self.page.setting.page_click_clear_cache()
        # 断言
        assert self.page.setting.base_is_exist_toast("清理成功")
