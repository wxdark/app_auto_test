import allure

import page
from base.base import Base


class PageVip(Base):
    # 输入邀请码
    @allure.step(title='输入邀请码')
    def page_input_invitation_code(self, text):
        self.base_input(page.vip_invitation_code, text)

    # 点击成为会员按钮
    @allure.step(title='点击 成为会员')
    def page_click_become_vip(self):
        self.base_click_element(page.vip_become)
