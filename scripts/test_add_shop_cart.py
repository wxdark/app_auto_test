import time

from base.base_driver import get_driver
from page.page import Page


class TestAddShopCart:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 添加购物车
    def test_add_shop_cart(self):
        # 判断是否登录
        self.page.home.page_if_login_in(self.page)
        # 点击分类按钮
        self.page.home.page_click_category_btn()
        # 随机点击商品分类
        self.page.category.page_click_category_list()
        # 随机点击商品
        self.page.goods_list.page_click_goods()
        # 点击加入购物车
        self.page.goods_detail.page_click_add_shop_cart()
        # 选择商品规格
        self.page.goods_detail.page_choose_spec()
        # 断言是否加入购物车
        assert self.page.goods_detail.base_is_exist_toast("成功加入购物车")

    # 判断价格是否相等
    def test_shop_cart_price(self):
        # 判断是否登录
        self.page.home.page_if_login_in(self.page)
        # 点击首页购物车按钮
        self.page.home.page_click_shop_cart()
        # 点击全选按钮
        self.page.shop_cart.page_click_selection_button()
        # 记录商品总价
        total_price = self.page.shop_cart.page_get_total_price()
        # 点击编辑按钮
        self.page.shop_cart.page_click_edit_btn()
        # 点击加号
        self.page.shop_cart.page_click_add_count()
        # 点击完成按钮
        self.page.shop_cart.page_click_complete_btn()
        # 断言当前价格是否等于 记录总价 + 商品单价
        assert self.page.shop_cart.page_get_total_price() == total_price + self.page.shop_cart.page_get_price()

    # 删除购物车
    def test_delete_shop_cart(self):
        # 判断是否登录
        self.page.home.page_if_login_in(self.page)
        # 点击首页购物车按钮
        self.page.home.page_click_shop_cart()
        if self.page.shop_cart.page_is_shop_cart_empty():
            # 点击分类按钮
            self.page.home.page_click_category_btn()
            # 随机点击商品分类
            self.page.category.page_click_category_list()
            # 随机点击商品
            self.page.goods_list.page_click_goods()
            # 点击加入购物车
            self.page.goods_detail.page_click_add_shop_cart()
            # 选择商品规格
            self.page.goods_detail.page_choose_spec()
            # 点击返回按钮1
            self.page.goods_detail.base_press_back()
            time.sleep(2)
            # 点击返回按钮2
            self.page.goods_list.base_press_back()
            # 点击首页购物车按钮
            self.page.home.page_click_shop_cart()
        # 点击全选按钮
        self.page.shop_cart.page_click_selection_button()
        # 点击编辑按钮
        self.page.shop_cart.page_click_edit_btn()
        # 点击删除按钮
        self.page.shop_cart.page_click_delete_btn()
        # 点击确认
        self.page.shop_cart.page_click_affirm()
        # 断言是否删除成功
        assert self.page.shop_cart.base_is_exist_toast("删除成功")
        assert self.page.shop_cart.page_is_shop_cart_empty()

