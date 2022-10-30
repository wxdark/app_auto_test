import pytest
import page
from common import constant
from common.yaml_tools import YamlTools
from page.page_home import PageHome
from page.page_login import PageLogin
from page.page_register import PageRegister
from page.page_setting import PageSetting
from page.page_user_center import PageUserCenter
from page.page import Page


@pytest.mark.test
@pytest.mark.usefixtures("get_driver")
class TestLogin:

    @pytest.mark.parametrize('args', YamlTools().read_yaml(constant.dev_login_dir))
    def test_login(self, get_driver, args):
        get_driver[1][2].log.info("点击我的首页")
        PageHome(get_driver[0]).page_click_user_center()
        get_driver[1][2].log.info("点击去登陆")
        PageRegister(get_driver[0]).page_click_go_login()
        PageLogin(get_driver[0]).page_login(args['account'], args['password'])
        # 判断toast是否有值，如果为空则登录成功
        if args['toast'] is None:
            assert PageUserCenter(get_driver[0]).page_get_nickname_text() == args['account']
            PageUserCenter(get_driver[0]).page_click_logout()
            get_driver[1][2].log.info("登陆成功")
        # 登录失败进行断言
        else:
            assert PageLogin(get_driver[0]).base_is_exist_toast(args['toast'])
            PageLogin(get_driver[0]).base_press_back()
            get_driver[1][2].log.info("登陆失败")
