import time
from selenium import webdriver

class Driver(object):

    def start(self, driver_name="Chrome"):

        if driver_name == "Firefor":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
            #打开网页
            self.driver.get("https://mail.163.com/")
            #放大窗口
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

    def login(self,Account,Password):

        Account = Account
        Password = Password
        #账号登录
        self.driver.find_element_by_id("lbNormal").click()
        #进入表单
        i_frame = self.driver.find_elements_by_tag_name("iframe")[0]
        self.driver.implicitly_wait(10)
        #切换表单
        self.driver.switch_to.frame(i_frame)
        self.driver.implicitly_wait(10)
        #输入账号、密码
        self.driver.find_element_by_xpath('//input[@name="email"]').send_keys(Account)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//input[@name="password"]').send_keys(Password)
        time.sleep(1)
        #登录
        self.driver.find_element_by_xpath('//a[@id="dologin"]').click()
        self.driver.implicitly_wait(20)

    def write(self,email,title,text):

        email = email
        title = title
        text = text

        #写信
        self.driver.find_element_by_xpath("//*[@class='js-component-component ra0 mD0']").click()
        self.driver.implicitly_wait(10)
        #收件人
        self.driver.find_element_by_xpath("//*[@class='nui-editableAddr-ipt']").send_keys(email)
        time.sleep(2)
        #主题
        self.driver.find_element_by_xpath("//div[@aria-label='邮件主题输入框，请输入邮件主题']/input").send_keys(title)
        time.sleep(1)
        #切换表单
        frame1 = self.driver.find_element_by_class_name("APP-editor-iframe")
        self.driver.switch_to.frame(frame1)
        #正文
        self.driver.find_element_by_class_name("nui-scroll").send_keys(text)
        time.sleep(3)
        #返回上一层frame
        self.driver.switch_to.default_content()
        self.driver.implicitly_wait(10)

        print(self.driver.current_window_handle)
        print(self.driver.title)
        #预览
        self.driver.find_element_by_xpath("//*[@id='_dvModuleContainer_compose.ComposeModule_0']/header/div/div[2]/div/span").click()
        time.sleep(2)

        handles = self.driver.window_handles
        print(handles)

        self.driver.switch_to.window(handles[1])

        time.sleep(2)
        self.driver.find_element_by_xpath("/html/body/div/div[1]/div[2]/div/span").click()

        self.driver.switch_to.window(handles[0])
        time.sleep(1)
        #发送
        self.driver.find_element_by_xpath("//*[@id='_dvModuleContainer_compose.ComposeModule_0']/div/section/footer/div/span").click()
        time.sleep(3)

        self.driver.find_element_by_xpath("/html/body/header/div/ul/li[14]/a").click()
        time.sleep(3)
        self.driver.close()


if __name__ == "__main__":
    test = Driver()
    test.start()
    test.login("zjh_jinhua","hzj520@@")
    test.write("zhangjinhua@cvte.com","这是一封自动化测试邮件","邮件正文内容是自动填写的内容")


