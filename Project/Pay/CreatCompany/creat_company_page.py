# coding=utf-8
from selenium.webdriver.common.keys import Keys
from Common.webkeys import WebKeys


class CreatCompany(WebKeys):

    def creat_url(self):
        self.driver.get('https://www.cargonpay.com/back/#/company/create')

    def input_name(self, value):
        self.element_location('xpath', '//input[contains(@placeholder,"请输入企业名称")]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[contains(@placeholder,"请输入企业名称")]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[contains(@placeholder,"请输入企业名称")]').send_keys(value)

    def select_province(self):
        self.element_location('xpath', '//input[contains(@placeholder,"请选择省/市/区")]').click()
        self.elements_location('xpath', '//div[@class="ivu-tabs-content"]//a[contains(text(),"北京市")]')[-1].click()
        self.elements_location('xpath', '//div[@class="ivu-tabs-content"]//a[contains(text(),"北京市")]')[-1].click()
        self.elements_location('xpath', '//div[@class="ivu-tabs-content"]//a[contains(text(),"东城区")]')[-1].click()


    def input_address(self,value):
        self.element_location('xpath', '//input[contains(@placeholder,"请输入详细办公地址")]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[contains(@placeholder,"请输入详细办公地址")]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[contains(@placeholder,"请输入详细办公地址")]').send_keys(value)

    def submit(self):
        self.element_location('xpath', '//button[@class="long ivu-btn ivu-btn-primary ivu-btn-long"]').click()


class SelectCompany(WebKeys):

    def select_url(self):
        self.driver.get('https://www.cargonpay.com/back/#/company/select')

    def select_company(self, value):
        self.element_location('xpath', f'//a[@class="company-list-item cur"]/p[text()={value}]').click()



