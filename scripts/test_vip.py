import time

import pytest
from appium.webdriver.mobilecommand import MobileCommand

from base.base_analyze import data_analyze
from base.base_driver import get_driver
from page.page import Page


class TestVip:
    def setup(self):
        self.driver = get_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", data_analyze("vip.yaml", "test_vip"))
    def test_vip(self, args):
        """
        提示No Chromedriver found that can automate Chrome '39.0.0'
        即webview与chromewebdriver版本不一致
        :return:
        """
        try:
            # 判断是否登录，如果没有登录则登录
            self.page.home.page_if_login_in(self.page)
            # 点击加入超级VIP
            self.page.user_center.page_click_join_vip()
            # 切换至webview环境
            # self.driver.switch_to.context('WEBVIEW_com.yunmall.lc')
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'WEBVIEW_com.yunmall.lc'})
            # 输入邀请码
            self.page.vip.page_input_invitation_code(args['invitation_code'])
            # 点击立即成为会员
            self.page.vip.page_click_become_vip()
            #  断言“邀请码输入不正确”是否在page_source中
            assert self.page.vip.base_is_keyword_in_page_source(args['expect']), "%s 不在page_source中" % args['expect']
            # 切回原生环境
            # self.driver.switch_to.context('NATIVE_APP')
            self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {'name': 'NATIVE_APP'})
        except Exception as e:
            print(e)
