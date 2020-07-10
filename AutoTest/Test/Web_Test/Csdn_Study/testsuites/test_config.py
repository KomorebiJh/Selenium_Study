# coding=utf-8
# import configparser
# import os
#
#
# class TestReadConfigFile(object):
#
#     def get_value(self):
#         root_dir = os.path.dirname(os.path.abspath('..'))
#         # 注意多层级目录下文件的路径获取
#         # 获取项目根目录的相对路径
#         print(root_dir)
#
#         config = configparser.ConfigParser()
#         file_path = os.path.dirname(os.path.abspath('..'))+'/config/config.ini'
#         config.read(file_path)
#
#         browser = config.get("browserType", "browserName")
#         url = config.get("testServer", "URL")
#
#         return (browser, url)  # 返回的是一个元组
#
#
# trcf = TestReadConfigFile()
# print(trcf.get_value())
#获取系统时间以及格式化时间
# import time
# class GetTime(object):
#
#     def get_system_time(self):
#         print(time.time())  # time.time()获取的是从1970年到现在的间隔，单位是秒
#         print(time.localtime())
#         new_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # 格式化时间，按照 2017-04-15 13:46:32的格式打印出来
#         print(new_time)
#
# gettime = GetTime()
# gettime.get_system_time()

import time
from selenium import webdriver
class getSubstring(object):
    def test_serach_result(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(10)

        driver.get("https://www.baidu.com/")
        driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
        driver.find_element_by_xpath('//*[@id="su"]').click()

        serach_result = driver.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[2]/span').text
        print(serach_result)
        new_string = serach_result.split('约')[1]
        print(new_string)
        last_string = new_string.split('个')[0]
        print(last_string)


getstring = getSubstring()
getstring.test_serach_result()