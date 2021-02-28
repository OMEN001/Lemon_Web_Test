# -*- coding: utf-8 -*-
# @Time : BaLiang
# @Author : 86187
import os
import unittest

from datetime import datetime

from Libs.HTMLTestRunnerNew import HTMLTestRunner
from Common.handle_path import testcases_dir
from Common.handle_path import htmlreport_dir


# 创建测试套件
suite = unittest.TestSuite()

# 创建加载测试用例的套件并加载测试用例
loder = unittest.TestLoader()
suite.addTest(loder.discover(testcases_dir))
# 测试报告名称
result_full_path = "Web_Auto" + "_" + \
                   datetime.strftime(datetime.now(),'%Y%m%d%H%M%S') + ".html"
# 测试报告存放路径
result_full_path = os.path.join(htmlreport_dir,result_full_path)

with open(result_full_path,"wb") as one:
    # 创建测试运行程序
    runner = HTMLTestRunner(stream= one,
                            title="前程贷自动化测试报告",
                            description="前程贷UI自动化测试",
                            tester="BaLiang")
    #运行测试用例
    runner.run(suite)

