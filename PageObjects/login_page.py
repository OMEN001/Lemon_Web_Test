# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLoctors.login_page_locs import LoginPageLocs as loc
from selenium.webdriver.remote.webdriver import WebDriver
from Common.basepage import BasePage

class LoginPage(BasePage):

    """
    通过外部传参的方式引入webdriver(引入测试用例页面的webdriver),这样才能保证在同一个浏览器中操作
    """
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    # 等待元素可见
    def login(self,username,password):
        # WebDriverWait(self.driver,timeout=20,poll_frequency=0.5).until(EC.visibility_of_element_located(loc.login_button))
        # self.driver.find_element(*loc.username_input).send_keys(username)
        # self.driver.find_element(*loc.passwd_input).send_keys(password)
        # self.driver.find_element(*loc.login_button).click()
        self.input_text(loc.username_input,username,"登录页面_用户名输入")
        self.input_text(loc.passwd_input,password,"登录页面_密码输入")
        self.click_element(loc.login_button,"登录页面_点击登录按钮")

    # 获取输入不存在的用户名或错误密码的表单提示信息
    def get_not_user_or_error_passwd(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.not_existed_user_msg))
        # return self.driver.find_element(*loc.not_existed_user_msg).text
        self.wait_ele_visiable(loc.not_existed_user_msg,"登录页面_获取不存在或者输入错误密码的表单提示信息")
        return self.get_element_text(loc.not_existed_user_msg,"登录页面_获取不存在或者输入错误密码的表单提示信息")

    # 不输入用户名或密码的提示信息
    def error_user_msg(self):
        # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.not_input_user_passwd_msg))
        # return self.driver.find_element(*loc.not_input_user_passwd_msg).text
        self.wait_ele_visiable(loc.not_input_user_passwd_msg,"登录页面_不输入用户名或密码的提示信息")
        return  self.get_element_text(loc.not_input_user_passwd_msg,"登录页面_不输入用户名或密码的提示信息")