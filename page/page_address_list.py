import allure

import page
from base.base import Base


class PageAddressList(Base):
    # 点击新增地址
    @allure.step(title='地址列表 点击 新增地址')
    def page_click_add_address(self):
        self.base_find_element_with_scroll(page.address_add_btn).click()

    # 获取新增地址联系人,手机文本信息
    @allure.step(title='地址列表 获取 收件人和电话标题')
    def page_get_receipt_name(self):
        return self.base_get_text(page.address_receipt_name)

    # 判断是否存在默认地址
    @allure.step(title='判断默认标记是否存在')
    def page_if_exist_default(self):
        return self.base_if_exist_feature(page.address_is_default)

    # 判断删除按钮是否存在
    @allure.step(title='判断删除按钮是否存在')
    def page_if_exist_delete_btn(self):
        return self.base_if_exist_feature(page.address_delete_btn)

    # 点击默认地址进入编辑页面
    @allure.step(title='地址列表 点击 默认地址')
    def page_click_default_address(self):
        self.base_click_element(page.address_is_default)

    # 点击编辑按钮
    @allure.step(title='地址列表 点击 编辑按钮')
    def page_click_edit_btn(self):
        self.base_click_element(page.address_edit_btn)

    # 点击删除按钮
    @allure.step(title='地址列表 点击编辑后 点击删除按钮')
    def page_click_delete_btn(self):
        self.base_click_element(page.address_delete_btn)

    # 点击确认按钮
    @allure.step(title='地址列表 点击删除后 点击确认删除按钮')
    def page_click_confirm_btn(self):
        self.base_click_element(page.address_confirm_btn)
