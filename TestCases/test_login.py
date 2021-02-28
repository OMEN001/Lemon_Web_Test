# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import unittest
import time
import ddt

from selenium import webdriver

from TestDatas import Common_Datas as CD
from TestDatas import login_datas as LD
from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from Common.handle_log import do_log


@ddt.ddt
class TestLogin(unittest.TestCase):

    # 前置条件（每条用例运行前执行）
    def setUp(self) -> None:
        # 打开谷歌浏览器
        self.driver = webdriver.Chrome("D:\Tools\Chrome浏览器\Google\Chrome\Application\chromedriver.exe")
        #访问项目登录地址
        self.driver.get("http://8.129.91.152:8765/Index/login.html")
        #窗口最大化
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)

    # 后置条件（每条用例运行结束后执行）
    def tearDown(self) -> None:
        # 关闭当前会话窗口
        self.driver.quit()

    def test_success_login(self):
        do_log.info("登录功能-正常场景用例-输入正确的用户名和密码登录")
        self.lp.login(CD.username,CD.password)
        # 登录后页面发生跳转建议这里等待一下
        time.sleep(1)
        # url发生改变
        self.assertEqual("http://8.129.91.152:8765/Index/index",self.driver.current_url)
        # 我的用户是否存在
        self.assertTrue(HomePage(self.driver).user_is_exited())

    # 输入未注册的用户进行登录
    def test_not_exited_user_login(self):
        do_log.info("登录功能-异常场景用例-输入未注册用户名和密码登录")
        self.lp.login(LD.no_exit_datas["username"],LD.no_exit_datas["passwd"])
        self.assertEqual(self.lp.get_not_user_or_error_passwd(),LD.no_exit_datas["check"])
    #输入错误的密码登录
    def test_error_passwd_login(self):
        do_log.info("登录功能-异常场景用例-输入用户名和错误的密码登录")
        self.lp.login(LD.passwd_error["username"],LD.passwd_error["passwd"])
        self.assertEqual(self.lp.get_not_user_or_error_passwd(),LD.passwd_error["check"])
    @ddt.data(*LD.wrong_datas)
    def test_not_input_user_or_passwd_login(self,data):
        do_log.info("登录功能-异常场景用例-不输入用户名或者密码以及错误的用户名登录")
        self.lp.login(data["username"],data["passwd"])
        self.assertEqual(self.lp.error_user_msg(),data["check"])

if __name__ == '__main__':
    unittest.main()