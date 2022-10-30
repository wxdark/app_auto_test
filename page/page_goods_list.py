import random

import allure

import page
from base.base import Base


class PageGoodsList(Base):
    # 随机点击商品
    @allure.step(title='商品列表 选择 商品')
    def page_click_goods(self):
        goods_list = self.base_find_elements(page.goods_list)
        goods_list_count = len(goods_list)
        goods_list_index = random.randint(0, goods_list_count - 1)
        goods_list[goods_list_index].click()
