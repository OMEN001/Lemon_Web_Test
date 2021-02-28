# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import os

#项目目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir =  os.path.join(base_dir,"TestCases")

htmlreport_dir =  os.path.join(base_dir,"OutPuts/reports")

logs_dir =  os.path.join(base_dir,"OutPuts/logs")

screenshot_dir = os.path.join(base_dir,"OutPuts/screenshots/")

libs = os.path.join(base_dir,"Libs")

