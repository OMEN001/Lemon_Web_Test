# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
from selenium.webdriver.common.by import By


class LoginPageLocs:
    #用户名输入框
    username_input = (By.XPATH,'//input[@name="phone"]')
    #密码输入框
    passwd_input = (By.XPATH,'//input[@name="password"]')
    #登录按钮
    login_button = (By.XPATH,'//button[text()="登录"]')
    #输入不存在的用户名提示信息
    not_existed_user_msg = (By.XPATH,'//div[@class="layui-layer-content"]')
    #不输入用户名和密码的提示信息
    not_input_user_passwd_msg = (By.XPATH,'//div[@class="form-error-info"]')



