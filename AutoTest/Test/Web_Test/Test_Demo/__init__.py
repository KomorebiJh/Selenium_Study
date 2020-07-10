from AutoTest.Test.Web_Test.Csdn_Study.framework.browser_engine import BrowserEngine


class TestBrowserEngine(object):

    def open_browser(self):
        browserengine = BrowserEngine(self)
        driver = browserengine.openBorwser()


tbe = TestBrowserEngine()
tbe.open_browser()
