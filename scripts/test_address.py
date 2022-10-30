import time

import pytest

from base.base_analyze import data_analyze
from base.base_driver import get_driver
from page.page import Page


class TestAddress:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    # 新增地址测试脚本
    @pytest.mark.parametrize("args", data_analyze("address.yaml", "test_add_address"))
    def test_add_address(self, args):
        name = args['name']
        phone = args['phone']
        addr = args['address']
        code = args['post_code']
        toast = args['toast']
        # 点击设置按钮
        self.page.user_center.page_click_setting(self.page)
        # 点击地址管理
        self.page.setting.page_click_address_manage()
        # 点击新增地址按钮
        self.page.address_list.page_click_add_address()
        # 输入新增地址信息
        self.page.edit_address.page_add_address(name, phone, addr, code)
        if toast is None:
            assert self.page.address_list.page_get_receipt_name() == "%s  %s" % (name, phone)
        else:
            assert self.page.address_list.base_is_exist_toast(toast)

    # 编辑地址测试脚本
    def test_edit_address(self):
        # 点击设置按钮
        self.page.user_center.page_click_setting(self.page)
        # 点击地址管理
        self.page.setting.page_click_address_manage()
        # 判断是否存在地址,如果不存在就新增
        if not self.page.address_list.page_if_exist_default():
            # 点击新增地址按钮
            self.page.address_list.page_click_add_address()
            # 输入新增地址信息
            self.page.edit_address.page_add_address("李大叔", "18865633314", "深南大道1112号", "755231")
        self.page.address_list.page_click_default_address()
        # 重新输入地址信息进行修改并保存
        self.page.edit_address.page_edit_address()
        # 断言是否保存成功
        assert self.page.address_list.base_is_exist_toast("保存成功")

    def test_delete_address(self):
        # 点击设置按钮
        self.page.user_center.page_click_setting(self.page)
        # 点击地址管理
        self.page.setting.page_click_address_manage()
        # 断言是否有地址可删
        assert self.page.address_list.page_if_exist_default(), "默认标记不存在，没有地址可删"
        for i in range(10):
            self.page.address_list.page_click_edit_btn()
            # 判断删除按钮是否存在
            if not self.page.address_list.page_if_exist_delete_btn():
                # 不存在break
                break
            # 存在就继续删除
            self.page.address_list.page_click_delete_btn()
            self.page.address_list.page_click_confirm_btn()
        # 断言是否删除成功(查找默认标记,如果没有则断言通过)
        assert not self.page.address_list.page_if_exist_default(), "收货地址没有删除完毕"


