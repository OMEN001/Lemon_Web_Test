# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import datetime
import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.handle_log import do_log
from Common.handle_path import screenshot_dir


class BasePage:

    def __init__(self,driver:WebDriver):
        self.driver = driver

    #等待元素可见
    def wait_ele_visiable(self,locator,img_doc,timeout=30,poll_fre = 0.5):
        do_log.info("{},等待{}元素可见".format(img_doc,locator))
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            # 异常信息写入日志
            do_log.exception("元素可见失败")  # exception就是error级别，只不过输出的异常信息更为详细
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise
        else:
            end_time = datetime.datetime.now()
            do_log.info("元素等待结束，开始时间为：{}，结束时间为：{}，等待时长为：{}".format(start_time,end_time,(start_time-end_time)))

    # 等待元素存在
    def wait_page_contains_element(self,locator,img_doc,timeout=30,poll_fre = 0.5):
        do_log.info("{},等待{}元素存在".format(img_doc,locator))
        try:
            start_time = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            do_log.exception("等待元素存在失败")
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise
        else:
            end_time = datetime.datetime.now()
            do_log.info("元素等待结束，开始时间为：{}，结束时间为：{}，等待时长为{}".format(start_time,end_time,(start_time-end_time)))

    # 查找单个元素
    def get_element(self,img_doc,locator):
        do_log.info("{},查找元素{}".format(img_doc,locator))
        try:
            ele = self.driver.find_element(*locator)
        except:
            do_log.exception("查找元素失败!!!")
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise
        else:
            return  ele

    # 输入文本信息
    def input_text(self,locator,value,img_doc,timeout=30,poll_fre=0.5):
        #等待元素可见
        self.wait_ele_visiable(locator,img_doc,timeout,poll_fre)
        # 查找元素
        ele = self.get_element(img_doc,locator)
        do_log.info("{},在{}中输入信息{}".format(img_doc,locator,value))
        try:
            ele.send_keys(value)
        except:
            do_log.exception("文本信息输入失败")
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise

    # 点击元素
    def click_element(self,locator,img_doc,timeout=30,poll_fre=0.5):
        #等待元素可见
        self.wait_ele_visiable(locator,img_doc,timeout,poll_fre)
        #查找元素
        ele = self.get_element(img_doc,locator)
        do_log.info("{},点击元素{}".format(img_doc,locator))
        try:
            ele.click()
        except:
            do_log.exception("元素点击失败")
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise

    # 获取元素的文本信息
    def get_element_text(self,locator,img_doc,timeout=30,poll_fre=0.5):
        # 等待元素存在；
        self.wait_page_contains_element(locator,img_doc,timeout,poll_fre)
        # 查找元素
        ele = self.get_element(img_doc,locator)
        do_log.info("{},获取{}元素的文本内容.".format(img_doc, locator))
        try:
            text = ele.text
        except:
            do_log.exception("获取元素文本内容失败")
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.sava_page_screenshot(img_doc)
            raise
        else:
            do_log.info("获取的文本值为:{}".format(text))
            return text

    def get_element_attribute(self,locator,attr,img_doc):
        #等待元素存在
        self.wait_page_contains_element(img_doc,locator)
        #查找元素
        ele = self.get_element(img_doc,locator)
        do_log.info("{},获取{}元素的属性{}.".format(img_doc, locator, attr))
        try:
            value = ele.get_attribute(attr)
        except:
            # 异常信息写入日志
            do_log.exception("获取元素属性失败：")  # 级别：Error   tracebak的信息完整的写入日志。
            # 截图 - 命名。 页面名称_行为名称_当前的时间.png
            self.save_page_screenshot(img_doc)
            raise
        else:
            do_log.info("获取的属性值为: {}".format(value))
            return value

    #检查元素存在且可见
    def check_element_visible(self,locator,img_doc,timeout=10,poll_fre=0.5):
        """
         # 检测元素是否在页面存在且可见。
         如果退出元素存在，则返回True。否则返回False
        :return: 布尔值
        """
        do_log.info("{},检测元素{}存在且可见于页面。".format(img_doc,locator))
        try:
            WebDriverWait(self.driver,timeout,poll_fre).until(EC.visibility_of_element_located(locator))
        except:
            do_log.exception("{}秒内元素在当前页面不可见。".format(timeout))
            self.save_page_screenshot(img_doc)
            return False
        else:
            do_log.info("{}秒内元素可见。".format(timeout))
            return True

    def sava_page_screenshot(self,img_doc):
        now = time.strftime("%Y%m%d%H%M%S")
        screenshot_path = screenshot_dir + "{}_{}.png".format(img_doc,now)

        try:
            self.driver.save_screenshot(screenshot_path)
        except:
            do_log.exception("当前页面截图失败")
        else:
            do_log.info("页面截图成功并保存在{}".format(screenshot_path))

    # iframe切换
    def switch_to_iframe(self, iframe_pref, img_doc, timeout=30):
        """
        :param iframe_pref:
        :param img_doc:
        :param timeout:
        :return:
        """
        """
        等待iframe可用，并切换进去。
        :param iframe_pref: iframe的标识。支持下标、定位元组、WebElement对象、name属性
        :return: 无
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.frame_to_be_available_and_switch_to_it(iframe_pref))
        except:
            # 日志
            do_log.exception("切换到 {} 的iframe元素：{} 失败！".format(img_doc, iframe_pref))
            # 截图
            self.save_web_screenshot(img_doc)
            raise
        else:
            time.sleep(0.5)
            do_log.info("切换到 {} 的iframe元素：{} 成功！可以对新的html页面操作了！".format(img_doc, iframe_pref))

# if __name__ == '__main__':
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     driver = webdriver.Chrome("D:\Tools\Chrome浏览器\Google\Chrome\Application\chromedriver.exe")
#     driver.get("http://www.baidu.com")
#     driver.maximize_window()
#     ele = (By.XPATH,'//input[@id="kwss"]')
#     BasePage(driver).wait_ele_visiable("百度搜索页面",ele)