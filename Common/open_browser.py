from Common.read_config import ReadConfig
from Common.common import path_file
from playwright.sync_api import sync_playwright
from playwright.async_api import async_playwright


class RunBrowser(object):
    def __init__(self):
        self.browser = ''
        self.page = ''

    def sync_run(self, browser_window, browser_type):
        if browser_type == 'chrome':
            # self.browser = browser_window.chromium.launch(headless=False)
            self.browser = browser_window.chromium.launch()
        if browser_type == 'firefox':
            self.browser = browser_window.firefox.launch()
        self.page = self.browser.new_page()

    async def async_run(self, browser_window, browser_type):
        if browser_type == 'chrome':
            self.browser = await browser_window.chromium.launch()
        if browser_type == 'firefox':
            self.browser = await browser_window.firefox.launch()
        self.page = await self. browser.new_page()





