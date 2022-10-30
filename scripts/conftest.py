import pytest
from appium import webdriver
from common import constant
from common.ConfTools import DoConf
from common.LogTools import DoLogs
from common.yaml_tools import YamlTools
from page.page_login import PageLogin


@pytest.fixture(scope="session")
def tool_instance():
    ym = YamlTools()
    conf = DoConf(constant.globe_conf_dir)
    log = DoLogs(__name__)
    yield ym, conf, log


@pytest.fixture(scope="class")
def get_driver(tool_instance):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", tool_instance[0].read_yaml(constant.dev_desired_caps_dir))
    yield driver, tool_instance
    driver.close_app()


@pytest.fixture(scope="class")
def login_driver(tool_instance):
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", tool_instance[0].read_yaml(constant.dev_desired_caps_dir))
    PageLogin(driver).page_login(tool_instance[1].get_value("data", "account"),
                                 tool_instance[1].get_value("data", "pwd"))
    yield driver, tool_instance
    driver.close_app()

