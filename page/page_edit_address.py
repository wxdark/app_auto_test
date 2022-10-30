import random
import time

import allure

import page
from base.base import Base


class PageEditAddress(Base):
    # 输入收件人
    @allure.step(title='编辑地址 输入收件人')
    def page_input_receipt_name(self, name):
        self.base_input(page.edit_add_receipt_name, name)

    # 输入手机号
    @allure.step(title='编辑地址 输入手机号')
    def page_input_phone(self, phone):
        self.base_input(page.edit_add_phone, phone)

    # 输入详细地址
    @allure.step(title='编辑地址 输入详细地址')
    def page_input_detail_address(self, addr):
        self.base_input(page.edit_add_detail_addr_info, addr)

    # 输入邮编
    @allure.step(title='编辑地址 输入邮编')
    def page_input_post_code(self, code):
        self.base_input(page.edit_add_post_code, code)

    # 点击设为默认地址
    @allure.step(title='编辑地址 点击 设置为默认地址')
    def page_click_default(self):
        self.base_click_element(page.edit_add_address_default)

    # 点击选择所在地区
    @allure.step(title='编辑地址 点击 所在地区')
    def page_click_area(self):
        self.base_click_element(page.edit_add_address_province)

    # 随机选择省市区
    @allure.step(title='选择区域')
    def page_choose_area(self):
        self.page_click_area()
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            # 获取当前页面所有地区
            areas = self.base_find_elements(page.edit_add_area_title)
            # 获取地区个数
            area_count = len(areas)
            # 获取元素下标
            area_index = random.randint(0, area_count - 1)
            # 随机点击选择地区
            areas[area_index].click()
            time.sleep(1)

    # 点击保存按钮
    @allure.step(title='编辑地址 点击 保存按钮')
    def page_click_save_btn(self):
        self.base_click_element(page.edit_add_save_btn)

    # 新增地址组合业务方法封装
    def page_add_address(self, name, phone, addr, code):
        self.page_input_receipt_name(name)
        self.page_input_phone(phone)
        self.page_input_detail_address(addr)
        self.page_input_post_code(code)
        self.page_click_default()
        self.page_choose_area()
        self.page_click_save_btn()

    # 编辑地址业务组合方法封装
    def page_edit_address(self):
        self.page_input_receipt_name("李三属")
        self.page_input_phone("18933213325")
        self.page_input_detail_address("铭记大家123啊")
        self.page_choose_area()
        self.page_input_post_code("856321")
        self.page_click_save_btn()
