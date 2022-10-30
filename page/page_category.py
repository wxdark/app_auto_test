import random

import allure

import page
from base.base import Base


class PageCategory(Base):
    # 随机点击商品分类列表
    @allure.step(title='商品分类列表 选择 商品分类')
    def page_click_category_list(self):
        category_list = self.base_find_elements(page.category_goods_list)
        category_list_count = len(category_list)
        category_list_index = random.randint(0, category_list_count - 1)
        category_list[category_list_index].click()
