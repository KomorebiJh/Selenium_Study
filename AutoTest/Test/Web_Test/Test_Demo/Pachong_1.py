#
#
#
# #coding:UTF-8
# import requests     #用来抓取网页的html源代码
# import csv          #将数据写入到csv文件中
# import random       #random：取随机数
# import time         #time：时间相关操作
# import socket       #socket和http.client 在这里只用于异常处理
# import http.client
# from bs4 import BeautifulSoup     #BeautifulSoup：用来代替正则式取源码中相应标签中的内容
# import ssl
#
#
#
#
# def get_content(url,data=None):
#     header = {
#         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#         'Accept-Encoding':'gzip,deflate',
#         'Accept-Language':'zh-CN,zh;q=0.9',
#         'Connection':'keep-alive',
#         'User-Agent':'Mozilla/5.0(Windows NT 10.0;Win64; x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/76.0.3809.132Safari / 537.36'
#     }
#
#     timeout = random.choice(range(80,180))
#     while True:
#         try:
#             rep = requests.get(url,headers = header,timeout = timeout)
#             rep.encoding = 'utf-8'
#             break
#
#         except socket.timeout as e:
#             print('3:',e)
#             time.sleep(random.choice(range(8,15)))
#
#         except socket.timeout as e:
#             print('4:',e)
#             time.sleep(random.choice(range(20,60)))
#
#         except socket.timeout as e:
#             print('5:',e)
#             time.sleep(random.choice(range(30,80)))
#
#
#         except socket.timeout as e:
#             print('6:',e)
#             time.sleep(random.choice(range(5,15)))
#
#     return rep.text
#
#
# def get_data(html_text):
#     final = []
#     bs = BeautifulSoup(html_text,"html.parser")  # 创建BeautifulSoup对象
#     body = bs.body
#     data = body.find('div',{'id':'7d'})
#     ul = data.find('ul')
#     li = ul.find_all('li')
#
#     for day in li:  # 对每个li标签中的内容进行遍历
#         temp = []
#         date = day.find('h1').string# 找到日期
#         temp.append(date)  # 添加到temp中
#         inf = day.find_all('p')  # 找到li中的所有p标签
#         temp.append(inf[0].string, )  # 第一个p标签中的内容（天气状况）加到temp中
#         if inf[1].find('span') is None:
#             temperature_highest = None  # 天气预报可能没有当天的最高气温（到了傍晚，就是这样），需要加个判断语句,来输出最低气温
#         else:
#             temperature_highest = inf[1].find('span').string  # 找到最高温
#             temperature_highest = temperature_highest.replace('℃', '')  # 到了晚上网站会变，最高温度后面也有个℃
#         temperature_lowest = inf[1].find('i').string  # 找到最低温
#         temperature_lowest = temperature_lowest.replace('℃', '')  # 最低温度后面有个℃，去掉这个符号
#         temp.append(temperature_highest)  # 将最高温添加到temp中
#         temp.append(temperature_lowest)  # 将最低温添加到temp中
#         final.append(temp)  # 将temp加到final中
#
#     return temp
#
#
# def write_data(data, name):
#     file_name = name
#     with open(file_name, 'a', errors='ignore', newline='') as f:
#             f_csv = csv.writer(f)
#             f_csv.writerows(data)
#
# ssl._create_default_https_context = ssl._create_unverified_context
#
# if __name__ == '__main__':
#     url ='http://www.weather.com.cn/weather/101280101.shtml'
#     html = get_content(url)
#     result = get_data(html)
#     write_data(result, 'weather.csv')
