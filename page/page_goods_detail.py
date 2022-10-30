import time

import allure
from selenium.webdriver.common.by import By

import page
from base.base import Base


class PageGoodsDetail(Base):
    # 点击加入购物车
    @allure.step(title='商品详情页 点击 加入购物车')
    def page_click_add_shop_cart(self):
        self.base_click_element(page.goods_detail_add_shopcart)

    # 点击确认按钮
    @allure.step(title='商品详情页 点击 确认')
    def page_click_ensure(self):
        self.base_click_element(page.goods_detail_confirm_btn)

    # 获取toast提示信息
    @allure.step(title='商品详情页 获取 第一个规格的描述信息')
    def page_get_hint_info(self, text):
        return text.split(" ")[1]

    # 选择规格
    @allure.step(title='商品详情页 选择商品规格')
    def page_choose_spec(self):
        while True:
            # 点击确认按钮
            self.page_click_ensure()
            # 判断是否存在 "请选择" 字样的toast信息,如果有则代表没有选择规格
            if not self.base_is_exist_toast("请选择"):
                break
            spec = self.page_get_hint_info(self.base_get_toast("请选择"))
            spec_parent_element = By.XPATH, "//*[@text = '%s']/../*[2]/*[1]" % spec
            self.base_click_element(spec_parent_element)
            time.sleep(5)
