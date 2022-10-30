from appium import webdriver

from common import constant
from common.yaml_tools import YamlTools


def get_driver(no_reset=True):
    desired_cap = dict()
    # 需要连接的手机的平台
    desired_cap['platformName'] = "Android"
    # 需要连接的手机系统版本号
    desired_cap['platformVersion'] = "5.1"
    # 需要连接的手机设备号
    desired_cap['deviceName'] = "192.168.149.101:5555"
    # 需要打开的包名
    desired_cap['appPackage'] = "com.yunmall.lc"
    # 需要打开的界面名
    desired_cap['appActivity'] = "com.yunmall.ymctoc.ui.activity.MainActivity"
    # 如果为True不重置应用,为False就是重置,登录脚本需要重置应用,其他大部分脚本需要登录状态,不重置应用
    desired_cap['noReset'] = no_reset
    # 获取toast
    desired_cap['automationName'] = 'Uiautomator2'
    # 连接appium服务器，获取driver对象
    print(desired_cap)
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
    return driver


if __name__ == '__main__':
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", YamlTools().read_yaml(constant.dev_desired_caps_dir))
