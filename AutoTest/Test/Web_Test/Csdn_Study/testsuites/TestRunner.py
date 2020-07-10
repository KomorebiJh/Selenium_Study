import HTMLTestRunner
import os
import unittest
import time



# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLtemplate.html"
fp = open(HtmlFile, "wb")

suite = unittest.TestLoader().discover("AutoTest.Test.Web_Test.Csdn_Study.testsuites")   #遇到的坑，不能把文件夹内的ini文件删掉，否则会报错

if __name__ == '__main__':
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告", description=u"用例测试情况")
    runner.run(suite)
    fp.close()