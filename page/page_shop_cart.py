import allure

import page
from base.base import Base


class PageShopCart(Base):
    # 点击全选按钮
    @allure.step(title='购物车 点击 全选')
    def page_click_selection_button(self):
        self.base_click_element(page.shop_cart_selection_button)

    # 点击编辑按钮
    @allure.step(title='购物车 点击 编辑')
    def page_click_edit_btn(self):
        self.base_click_element(page.shop_cart_edit_btn)

    # 点击完成按钮
    @allure.step(title='购物车 点击 完成')
    def page_click_complete_btn(self):
        self.base_click_element(page.shop_cart_complete_btn)

    # 点击加号
    @allure.step(title='购物车 点击 加号')
    def page_click_add_count(self):
        self.base_click_element(page.shop_cart_add_count)

    # 处理金额
    @allure.step(title='处理金额（返回数字格式）')
    def page_deal_with_price(self, price):
        return float(price[2:])

    # 获取商品单价
    @allure.step(title='购物车 获取商品单价')
    def page_get_price(self):
        price = self.base_get_text(page.shop_cart_price)
        return self.page_deal_with_price(price)

    # 获取商品总价
    @allure.step(title='购物车 记录总价')
    def page_get_total_price(self):
        total_price = self.base_get_text(page.shop_cart_total_price)
        return self.page_deal_with_price(total_price)

    # 点击删除按钮
    @allure.step(title='购物车 点击 删除')
    def page_click_delete_btn(self):
        self.base_click_element(page.shop_cart_delete_btn)

    # 点击删除确认按钮
    @allure.step(title='购物车 点击 删除后的确认按钮')
    def page_click_affirm(self):
        self.base_click_element(page.shop_cart_affirm)

    # 判断购物车是否为空
    @allure.step(title='判断购物车是否有商品')
    def page_is_shop_cart_empty(self):
        return self.base_if_exist_feature(page.shop_cart_is_empty)
