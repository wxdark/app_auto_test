import allure

import page
from base.base import Base


class PageUpdate(Base):
    # 点击版本更新
    @allure.step(title='点击版本更新')
    def page_click_update(self):
        self.base_click_element(page.about_update)
