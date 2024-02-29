import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Product.models import Element
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.keys import Keys
import requests
import json
import random

class PageObject:
    driver = None

    def sleep(self, second):
        if str(second).isdigit():
            time.sleep(int(second))
        else:
            time.sleep(0.5)

    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        
    def open_url(self, url):
        self.driver.get(url)

    def max_size(self):
        self.driver.maximize_window()

    def click(self, locator):
        if locator is None:
            return
        else:
            try:
                PageObject.find_element(self.driver, locator).click()
            except:
                raise

    # 有时需要加() 有时不需要 原因暂时不清楚 此为不加
    def click_no(self, locator):
        if locator is None:
            return
        else:
            try:
                PageObject.find_element(self.driver, locator).click
            except:
                raise

    def click_point(self, x, y, left_click=True):
        if left_click:
            ActionChains(self.driver).move_by_offset(x, y - 103).click.perform()
        else:
            ActionChains(self.driver).move_by_offset(x, y - 103).context_click.perform()

    def send_keys(self, locator, value):
        if locator is None:
            return
        if value is None:
            self.clear(locator)
        else:
            PageObject.find_element(self.driver, locator).send_keys(value)

    def clear(self, locator):
        if locator is None:
            return

    def alert_accept(self):
        '''
        对弹窗实行确认操作
        :return:
        '''
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        '''
        对弹窗实行取消操作
        :return:
        '''
        self.driver.switch_to.alert.dismiss()

    def alert_text(self):
        text = self.driver.switch_to.alert.text
        print(text)

    def switch_to_window(self, title=None):
        '''
        :param title: 遍历的方式获得一个当前所有的窗口列表，通过传递默认参数title来进行当前窗口的切换，直到匹配到与title相同的窗口。
        :return: title
        '''
        handle = self.driver.current_window_handle
        if title:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)
                    if self.driver.title == title:
                        break
            else:
                raise ValueError("未找到标题为：" + title + " 的页面")
        else:
            for handle_ in self.driver.window_handles:
                if handle != handle_:
                    self.driver.switch_to.window(handle)

    def switch_to_frame(self, locator=None):
        if locator:
            self.driver.switch_to.frame(PageObject.find_element(self.driver, locator))
        else:
            self.driver.switch_to.default_content()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()
        self.sleep(1)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def select_by_text(self, element, value, visible=False):
        '''
        select_by_index()  :通过索引定位
        select_by_value()  :通过value值定位
        select_by_visible_text() :通过文本值定位
        deselect_all()          ：取消所有选项
        deselect_by_index()     ：取消对应index选项
        deselect_by_value()      ：取消对应value选项
        deselect_by_visible_text() ：取消对应文本选项
        first_selected_option()  ：返回第一个选项
        all_selected_options()   ：返回所有的选项
        :return:
        '''
        if element is None:
            return
        element = PageObject.find_element(self.driver, element)
        if not visible:
            Select(element).select_by_text(value)
        else:
            Select(element).select_by_visible_text(value)  # 需要所需选项的全文 直接通过选项的文本内容来定位

    @staticmethod
    def find_element(driver, locator, more=False, timeout=20):
        message = locator
        if isinstance(locator, dict):
            locator = (locator.get("by", None), locator.get("locator", None))
            message = locator
        elif isinstance(locator, list) and len(locator) > 2:
            locator = (locator[0], locator[1])
            message = locator
        elif isinstance(locator, Element):
            message = locator.name
            locator = (locator.by, locator.locator)
        elif isinstance(locator, str):
            locator = tuple(locator.split(".", 1))
            message = locator
        else:
            raise TypeError("element参数类型错误: type:" + str(type(locator)))
        try:
            try:
                if more:
                    return WebDriverWait(driver, timeout).until(ec.visibility_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))
            except:
                if more:
                    return WebDriverWait(driver, timeout).until(ec.presence_of_all_elements_located(locator))
                else:
                    return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))
        except Exception:
            raise RuntimeError("找不到元素:" + str(message))

    def move_to_element(self, locator):
        ActionChains(self.driver).move_to_element(self.find_element(self.driver, locator)).perform()

    # def autologin(self, locator1, locator2):
    #     telephone = '181'+''.join(str(random.choice(range(10))) for _ in range(8))
    #     payload = {"telephone": telephone}
    #     r = requests.post('https://your_website/your_api/code', data = payload)
    #     dic = r.json()
    #     code = dic['data']['code']
    #     self.sleep(3)
    #     self.send_keys(locator1, telephone)
    #     self.send_keys(locator2, code)

    def move_jindutiao(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView();", PageObject.find_element(self.driver, locator))


    def xuanting(self, locator):
        '''
        鼠标悬停
        '''
        el = PageObject.find_element(self.driver, locator)
        ActionChains(self.driver).move_to_element(el).perform()

    def clear_cookies(self):
        """
        清除cookie
        """
        self.driver.delete_all_cookies()


    def take_screen_shot(self, file_name):
        """
        page 页面截图操作
        file_name:path还没写
        """
        self.driver.save_screenshot(file_name)


    def enter(self, locator):
        if locator is None:
            return
        else:
            PageObject.find_element(self.driver, locator).send_keys(Keys.ENTER)










    

