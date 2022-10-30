import threading
import time

from appium import webdriver


# 获取driver
def init_driver(port, udid):
    desired_cap = dict()
    desired_cap['platformName'] = 'Android'
    desired_cap['platformVersion'] = '5.1'
    desired_cap['deviceName'] = 'genymotion'
    desired_cap['udid'] = udid
    # 192.168.149.101:5555
    desired_cap['appPackage'] = 'com.android.settings'
    desired_cap['appActivity'] = '.Settings'
    # 'http://127.0.0.1:4725/wd/hub'
    driver = webdriver.Remote('http://127.0.0.1:' + port + '/wd/hub', desired_cap)
    return driver


def execute(port, udid):
    driver = init_driver(port, udid)
    driver.find_element_by_xpath('//*[@text="更多"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@text="移动网络"]').click()


devices = [{'port': '4723', 'udid': '192.168.149.101:5555'}, {'port': '4725', 'udid': '192.168.149.102:5555'}]
for device in devices:
    # execute(device['port'], device['udid'])  # 按顺序运行
    threading.Thread(target=execute, args=(device['port'], device['udid'])).start()  # 同时执行测试脚本
