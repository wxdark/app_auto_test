import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self, driver):
        self.driver = driver

    # 查找元素
    def base_find_element(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元素特征
        :param timeout: 查找元素超时时间
        :param poll: 查找元素频率
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 查找多个元素
    def base_find_elements(self, loc, timeout=10, poll=0.5):
        """
        :param loc: 元素特征
        :param timeout: 查找元素超时时间
        :param poll: 查找元素频率
        :return:
        """
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(*loc))

    # 点击元素
    def base_click_element(self, loc):
        self.base_find_element(loc).click()

    # 获取元素文本信息
    def base_get_text(self, loc):
        return self.base_find_element(loc).text

    # 输入
    def base_input(self, loc, value):
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(value)

    # 点击手机返回按钮
    def base_press_back(self):
        self.driver.press_keycode(4)

    # 点击手机enter键
    def base_press_enter(self):
        self.driver.press_keycode(66)

    # 判断toast是否存在
    def base_is_exist_toast(self, message):
        message_path = By.XPATH, "//*[contains(@text,'" + message + "')]"
        try:
            self.base_find_element(message_path, timeout=3, poll=0.1)
            return True
        except TimeoutException:
            return False

    # 如果存在toast,获取toast值并返回
    def base_get_toast(self, message):
        if self.base_is_exist_toast(message):
            message_path = By.XPATH, "//*[contains(@text,'" + message + "')]"
            return self.base_find_element(message_path).text
        else:
            raise Exception("toast未出现,请检查参数是否正确或toast有没有出现在屏幕上")

    # 判断元素特征是否存在
    def base_if_exist_feature(self, feature):
        try:
            self.base_find_element(feature)
            return True
        except TimeoutException:
            return False

    # 滑动一次方法封装
    def base_scroll_page_one_time(self, direction="up"):
        """
        滑动一次
        :param direction:
         up ： 从上往下滑
         down： 从下往上滑
         left：从左往右滑
         right：从右往左滑
        :return:
        """
        # 考虑屏幕的分辨率问题,滑动参数不应该写死
        # 获取屏幕宽度
        width = self.driver.get_window_size()['width']
        # 获取屏幕高度
        height = self.driver.get_window_size()['height']
        # 滑动坐标
        center_x = width / 2
        center_y = height / 2
        # 横向滑动坐标(横向滑动幅度大小调整left_x,right_x即可)
        left_x = width / 8 * 1
        left_y = center_y
        right_x = width / 8 * 7
        right_y = center_y
        # 纵向滑动坐标
        top_x = center_x
        top_y = height / 4 * 1
        bottom_x = center_y
        bottom_y = height / 4 * 3
        # 从上往下滑
        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y, 3000)
        # 从下往上滑
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y, 3000)
        # 从左往右滑
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        # 从右往左滑
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y, 3000)
        else:
            raise Exception("请检查参数是否正确, up/down/left/right")

    # 滑动查找元素
    def base_find_element_with_scroll(self, feature, direction="up"):
        """
        滑动查找元素
        :param feature:元素特征
        :param direction: 滑动方向
        :return:
        """
        # 循环查找元素
        page_source = ""
        while True:
            try:
                return self.base_find_element(feature)
            except Exception:
                self.base_scroll_page_one_time(direction)
                # 判断是否到底部
                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

    # 判断字符串是否存在page_source中
    def base_is_keyword_in_page_source(self, keyword, timeout=10, poll=0.1):
        """
        :param keyword: 关键字符串
        :param timeout: 超时时间，默认10s
        :param poll: 查找频率，默认0.1s
        :return: 如果字符串存在page_source中返回True，不存在返回False
        """
        # 定义结束时间
        end_time = time.time() + timeout
        while True:
            # 如果结束时间大于当前时间,就认为超时了
            if end_time < time.time():
                print("超时了")
                return False
            # 判断keyword是否存在page_source中
            if keyword in self.driver.page_source:
                return True
            time.sleep(poll)
