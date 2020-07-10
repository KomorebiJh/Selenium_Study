import time
import unittest
from AutoTest.Test.Web_Test.Csdn_Study.framework.browser_engine import BrowserEngine
from AutoTest.Test.Web_Test.Csdn_Study.pageobjects.baidu_homepage import HomePage
from AutoTest.Test.Web_Test.Csdn_Study.pageobjects.baidu_news_home import NewsHomePage
from AutoTest.Test.Web_Test.Csdn_Study.pageobjects.news_sports_home import SportNewsHomePage


class ViewNBANews(unittest.TestCase):
    def setUp(self):
        browse = BrowserEngine(self)
        self.driver = browse.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_view_nba_views(self):
            # 初始化百度首页，并点击新闻链接
            baiduhome = HomePage(self.driver)
            # baiduhome.click_news()
            self.driver.find_element_by_xpath("//*[@id='u1']/a[@name='tj_trnews']").click()
            # 初始化一个百度新闻主页对象，点击体育
            newshome = NewsHomePage(self.driver)
            # self.driver.refresh()
            # newshome.click_sports()
            self.driver.find_element_by_xpath('//*[@id="channel-all"]/div/ul/li[7]/a').click()

            newshome.get_windows_img()


if __name__ == '__main__':
    unittest.main()
