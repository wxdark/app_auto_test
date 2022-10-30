import allure

import page
from base.base import Base


class PageRegister(Base):
    # 点击已有账号去登陆
    @allure.step(title='注册页 点击 去登陆')
    def page_click_go_login(self):
        self.base_click_element(page.register_go_login)
