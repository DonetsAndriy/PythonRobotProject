import sys

__author__ = 'adonets'
from SeleniumWrapper import SeleniumWrapper as wrapper

from homepage import HomePage
from signinpage import SignInPage
sys.path.append('C:\Python27\Lib\site-packages\page_objects')
class PageObjects(HomePage, SignInPage):
    def open_browser_to_english_home_page(self):
        se = wrapper().connect("127.0.0.1", "4444", "*firefox", "http://www.workopolis.com")
        se.start()
        se.window_maximize()
        h = HomePage()
        h.open_english_home_page()

    def close_browser_after_run(self):
        se = wrapper().connection
        se.stop()
