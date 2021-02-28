# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from PageLoctors.home_page_locs import HomePageLocs as loc
from Common.basepage import BasePage

class HomePage(BasePage):

    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    #用户名是否存在
    def user_is_exited(self):
        try:
            # WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(loc.my_user_name))
            self.wait_ele_visiable(loc.my_user_name,"首页_判断用户是否存在")
        except:
            return False
        else:
            return True
