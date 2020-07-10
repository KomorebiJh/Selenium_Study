# from selenium import webdriver
#
# driver = webdriver.Chrome()

# driver.get("https://cn.bing.com")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("CMCC")
# driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
# driver.quit()

# =======================
# 第1部分： 定位元素
# =======================

# # # #################
# # # id定位
# # # #################
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_id("sb_form_q").send_keys("CMCC")
# driver.find_element_by_id("sb_form_go").click()
# driver.quit()

# # #################
# # name定位
# # #################
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_name("q").send_keys("CMCC")
# driver.find_element_by_name("go").click()
# driver.quit()


# # #################
# # class定位
# # #################
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_class_name("b_searchbox").send_keys("CMCC")
# driver.find_element_by_class_name("b_searchboxSubmit").click()
# driver.quit()

# # #################
# # link定位
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_link_text("学术").click()
# sleep(2)
# driver.quit()

# # #################
# # partial link定位
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_partial_link_text("学").click()
# driver.quit()

# # #################
# # xpath定位--绝对路径
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div/div[2]/div[3]/form/div/input[1]").send_keys("CMCC")
# driver.find_element_by_xpath("/html/body/table/tbody/tr/td/div/div[2]/div[3]/form/div/div[1]/input").click()
# driver.quit()
#
# # #################
# # xpath定位--简化版
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("CMCC")
# driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()
# driver.quit()

# #################
# # xpath定位--简化版
# # 元素属性定位
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_xpath('//input[@id="sb_form_q"]').send_keys("CMCC")
# driver.find_element_by_xpath('//input[@id="sb_form_go"]').click()
# driver.quit()
#
# # #################
# # xpath定位--简化版
# # 元素属性定位
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# driver.find_element_by_xpath('//input[@name="q"]').send_keys("CMCC")
# driver.find_element_by_xpath('//input[@name="go"]').click()
# driver.quit()


# # #################
# # css定位--简化的CSS定位
# # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_css_selector("#sb_form_q").send_keys("CMCC")
# driver.find_element_by_css_selector("#sb_form_go").click()
# driver.quit()
#
# # # #################
# # # css定位--
# # # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_css_selector(".b_searchbox").send_keys("CMCC")
# driver.find_element_by_css_selector(".b_searchboxSubmit").click()
# driver.quit()
#
# # # # #################
# # # # css定位--属性定位
# # # # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
# #
# driver.find_element_by_css_selector("[name='q']").send_keys("CMCC")
# driver.find_element_by_css_selector("[name='go']").click()
# driver.quit()

# # # # #################
# # # # 属性组合定位
# # # # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_xpath('//input[@id="sb_form_q" and @name="q"]').send_keys("CMCC")
# driver.find_element_by_xpath('//input[@id="sb_form_go" and @name="go"]').click()
# driver.quit()


# # # # #################
# # # # find_elemnet组合定位
# # # # #################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element(by="id",value="sb_form_q").send_keys("CMCC")
# driver.find_element(by="id",value="sb_form_go").click()
# driver.quit()


# =======================
# 第2部分： 常规操作
# =======================

# # ################
# # 浏览器控制最大化
# # ################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.maximize_window()
# sleep(2)
# driver.set_window_size(800,600)
# sleep(2)
#
# driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("CMCC")
# driver.find_element_by_xpath('//*[@id="sb_form_go"]').click()
# driver.quit()

# # ################
# # 浏览器控制前进与后退
# # ################
# from selenium import webdriver
# from time import  sleep
#
# # driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_link_text("学术").click()
# print(driver.title)
# sleep(2)
#
# driver.back()
# print(driver.title)
# sleep(2)
# driver.quit()


# # ################
# # 浏览器控制前进与后退
# # ################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Chrome()
#
# driver.get("https://cn.bing.com/")
#
# driver.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys("CMCC")
# sleep(3)
# driver.find_element_by_xpath('//*[@id="sb_form_q"]').clear()


# ################
# # 实际结果与测试结果的对比
# ################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Firefox()
#
# driver.get("https://cn.bing.com/")
# driver.maximize_window()
#
# Expect_title = "Bing 学术"
#
# driver.find_element_by_link_text("学术").click()
# sleep(1)
# # print(driver.title)
# True_title = driver.title
#
# driver.get_screenshot_as_file("CMCC.png")
#
# if True_title == Expect_title:
#     print(True)
# else:
#     print(False)
#
# driver.quit()

# # ################
# # 实际结果与测试结果的对比
# # ################
# from selenium import webdriver
# from time import  sleep
#
# driver = webdriver.Firefox()
#
# driver.get("https://cn.bing.com/")
# driver.maximize_window()
#
# Expect_title = "Bing 学术"
#
# driver.find_element_by_link_text("学术").click()
# sleep(1)
# # print(driver.title)
# True_title = driver.title
#
# driver.get_screenshot_as_file("CMCC.png")
#
# if True_title == Expect_title:
#     print(True)
#
# else:
#     print(False)


# =======================
# # 第3部分： 等待时间
# =======================

# # ################
# # 等待WebDriverWait
# # ################
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# driver = webdriver.Firefox()
#
# driver.get("https://cn.bing.com/")
#
# # element = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"sb_form_q")))
# # element.send_keys("CMCC")
# # driver.quit()
# element = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,"sb_form_q")))
# element.send_keys("CMCC")
# driver.quit()

# ################
# 等待implicitly_wait
# ################
from selenium import webdriver
from time import ctime,sleep
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://cn.bing.com/")

try:
    print(ctime())
    driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("CMCC")
    driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
except NoSuchElementException as e:
    print(e)
finally:
    print(ctime())
    driver.quit()


# # ################
# # 强制等待sleep
# # ################
# from selenium import webdriver
# from time import sleep
# from selenium.common.exceptions import NoSuchElementException
#
# driver = webdriver.Firefox()
# driver.get("https://cn.bing.com/")
#
# sleep(5)
# driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("CMCC")
# driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
# driver.quit()

# # ################
# # # 等待案例
# # # ################
# # from selenium import webdriver
# # from time import ctime,sleep
# # from selenium.common.exceptions import NoSuchElementException
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# #
# # driver = webdriver.Firefox()
# #
# # driver.implicitly_wait(10)
# # driver.get("https://cn.bing.com/")
# #
# # try:
# #     print(ctime())
# #     WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.ID,"sb_form_qdd")))
# #     print(ctime())
# #     driver.find_element_by_xpath("//*[@id='sb_form_qdd']").send_keys("CMCC")
# #     driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
# # except NoSuchElementException as e:
# #     print(e)
# # finally:
# #     print(ctime())
# #     driver.quit()


# =======================
# 第4部分： 其它案例
# =======================

# # ################
# # 定位一组元素
# # ################
# from selenium import webdriver
# from time import ctime,sleep
#
# driver = webdriver.Firefox()
# driver.get("file:///G:/Demo/checkbox.html")

# 方式1：运行方式2要把方式1注释掉
# inputs = driver.find_elements_by_tag_name("input")
# # print(inputs)
#
# for i in inputs:
#     if i.get_attribute("type") == "checkbox":
#         i.click()
#         sleep(1)
# driver.quit()

# # 方式2
# checkboxes = driver.find_elements_by_xpath("//input[@name='fruit']")
# print(len(checkboxes))
#
# for checkbox in checkboxes:
#     checkbox.click()
# driver.quit()


# # # ################
# # # frame的操作
# # # ################
# from selenium import webdriver
# from time import ctime,sleep
#
# driver = webdriver.Firefox()
# driver.get("file:///G:/Demo/iframe.html")
#
# driver.switch_to.frame("iname")
# driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("CMCC")
# driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
#
# # driver.switch_to_default_content()
# # driver.switch_to.parent_frame()
# driver.switch_to.default_content()
# driver.find_element_by_xpath("/html/body/div[1]/a").click()
# driver.quit()


# # # ################
# # # 警告框的操作
# # # ################
# from selenium import webdriver
# from time import ctime,sleep
#
# driver = webdriver.Firefox()
# driver.get("file:///G:/Demo/alert.html")
# driver.find_element_by_xpath("//input[@name='b1']").click()
# sleep(3)
# text = driver.switch_to.alert.text
# print(text)
#
# # driver.switch_to.alert.accept() #接受警告框
# driver.switch_to.alert.dismiss() #解散警告框
# driver.quit()

# # # ################
# # # js的操作
# # # ################
# from selenium import webdriver
# from time import ctime,sleep
#
# driver = webdriver.Firefox()
# driver.get("https://cn.bing.com")
#
# driver.set_window_size(800,600)
# driver.find_element_by_xpath("//*[@id='sb_form_q']").send_keys("CMCC")
# driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
# sleep(3)
# js = "window.scrollTo(100,500)"
# driver.execute_script(js)
# sleep(3)
# driver.quit()

# =======================
# 第5部分： 测试模型
# =======================

# # # ################
# # # 定位一组元素
# # # ################
# from selenium import webdriver
# from time import ctime,sleep
# from Search import search
#
# driver = webdriver.Firefox()
# driver.get("https://cn.bing.com")
#
# driver.maximize_window()
# search(driver)
#
# driver.quit()