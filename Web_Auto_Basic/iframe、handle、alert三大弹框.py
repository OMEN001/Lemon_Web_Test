# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 窗口切换
# driver = webdriver.Chrome("D:\Tools\Chrome浏览器\Google\Chrome\Application\chromedriver.exe")
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# driver.find_element_by_id("kw").send_keys("柠檬班官网")
# driver.find_element_by_id("su").click()
# time.sleep(2)
# loc = (By.XPATH,'//div[@id="1"]//a[text()="腾讯课堂"]')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
# driver.find_element(*loc).click()
#
# # 获取窗口的所有句柄
# wins = driver.window_handles
# time.sleep(2)
# print(wins)
#
# # 获取当前窗口句柄
# cur = driver.current_window_handle
# print("当前窗口的句柄为：",cur)
# time.sleep(2)
#
# # 切换窗口句柄
# driver.switch_to.window(wins[0])
#
# time.sleep(2)
# # 关闭当前会话
# loc1 = (By.XPATH,'//*[@id="3"]/h3/a')
# WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc1))
# driver.find_element(*loc1).click()
# time.sleep(2)
# driver.quit()

# alert窗口切换
# 1、某一个行为，触发了alert弹框

# 2、切换到alert窗口 al = driver.switch_to.alert

# 3、al.al.accept() 关闭   al.text() 获取文本信息 al.send_keys("") 输入内容  al.dismiss() 取消


# iframe窗口切换
# 1、确认自己要操作的元素，是否在iframe当中？
#    F12，定位元素后，看上方的完整的元素路径当中，是否有iframe，是否有2个以上的html

# 2、找到iframe - 标签对。容器，里面放的是html.
#   iframe是个元素，主html来讲，仍然是可以通过元素定位找到的。
#   3种方式：
#   1）name属性：  login_frame_qq
#   2）index下标：  2
#   3）webElement对象：driver.find_element_by_name("login_frame_qq")

# 3、切换进iframe,在新的html页面当中操作。
# 4、若要退出iframe,driver.switch_to.default_content()

driver = webdriver.Chrome("D:\Tools\Chrome浏览器\Google\Chrome\Application\chromedriver.exe")
driver.get("http://www.baidu.com")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("腾讯课堂")
driver.find_element_by_id("su").click()
time.sleep(2)
loc = (By.XPATH,'//a[text()="_职业培训、考试提升在线教育平台"]')
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc))
driver.find_element(*loc).click()
time.sleep(2)

wins = driver.window_handles
print(wins)
driver.switch_to.window(wins[1])

loc1 = (By.XPATH,'//a[contains(@class,"mod-entry-login js-login-op")]')
driver.find_element(*loc1).click()
WebDriverWait(driver,20).until(EC.visibility_of_element_located(loc1))

time.sleep(2)

qq_login = (By.XPATH,'//div[@class="content-btns"]/a[text()="QQ登录"]')
driver.find_element(*qq_login).click()

driver.switch_to.frame("login_frame_qq")

loc2 = (By.XPATH,'//a[text()="帐号密码登录"]')
driver.find_element(*loc2).click()

username = (By.XPATH,'//input[@id="u"]')
password = (By.XPATH,'//input[@id="p"]')
login_button = (By.XPATH,'//input[@id="login_button"]')

WebDriverWait(driver,20).until(EC.visibility_of_element_located(login_button))

driver.find_element(*username).send_keys("2586089125")
driver.find_element(*password).send_keys("ybfk312628ltj")
driver.find_element(*login_button).click()

time.sleep(2)

driver.quit()


