# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
"""
actionChains -
点击   click
双击   double_click
悬浮   move_to_element
右键   context_click
拖拽   drag_and_drop
暂停   pause

click_and_hold  和  release

0) 实例化actionChains类
1) 要操作的动作放在 链表当中。  动作的函数 - 放到列表当中。(找到元素，调用鼠标行为)
2) 调用perform() 去执行动作。
"""
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome("D:\Tools\Chrome浏览器\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.maximize_window()

loc = (By.XPATH,'//span[@id="s-usersetting-top"]')

# 0) 实例化actionChains类
ac = ActionChains(driver)

# 1) 要操作的动作放在 链表当中。
# 查找元素
ele = driver.find_element(*loc)
# 鼠标悬浮到元素上，暂停0.5秒，点击元素
ac.move_to_element(ele).pause(0.5).click(ele)

# 2) 调用perform() 去执行动作。
ac.perform()

loc1 = (By.XPATH,'//a[text()="搜索设置"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc1))
driver.find_element(*loc1).click()


select_ele = driver.find_element(*loc)
s = Select(select_ele)

# 2）使用它提供的选择方法，选择下拉列表的值
"""
1) 下标。  s.select_by_index()
2) 文本。  s.select_by_visible_text()
3) value属性  s.select_by_value()
"""
s.select_by_index(6)

s.select_by_visible_text("Adobe Acrobat PDF (.pdf)")

s.select_by_value("ppt")

driver.quit()






