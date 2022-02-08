# coding=utf-8
from selenium.webdriver.common.keys import Keys
from Common.webkeys import WebKeys
from Common.common import upload_file


class BankCA(WebKeys):

    def bank_url(self):
        self.driver.get('https://www.cargonpay.com/back/#/setting/certification/list')

    def company_auth_button(self):
        self.elements_location('xpath', '//div[@class="bank-list-btn"]/a[text()="企业授权"]')[0].click()

    def boc_file_button(self):
        self.element_location('xpath', '//div[@class="bank-list-btn"]/a[text()="上传保函"]').click()

    def boc_ca_button(self):
        self.elements_location('xpath', '//div[@class="bank-list-btn"]/a[text()="添加认证"]')[0].click()

    def spd_ca_button(self):
        self.element_location('xpath', '//div[@class="bank-list-btn  "]/a[text()="添加认证"]').click()

    def cmb_ca_button(self):
        self.elements_location('xpath', '//div[@class="bank-list-btn"]/a[text()="添加认证"]')[1].click()

    def cncb_ca_button(self):
        self.elements_location('xpath', '//div[@class="bank-list-btn"]/a[text()="添加认证"]')[2].click()


class CompanyAuth(WebKeys):

    def select_company_auth_file(self, path):
        self.driver.find_element_by_xpath('//label[contains(text(),"企业授权书")]/..//a[@class="add-file-btn"]').click()
        upload_file(path)

    def input_name(self, value):
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人姓名")]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人姓名")]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人姓名")]').send_keys(value)

    def input_no(self, ctype, value):
        self.element_location('xpath', '//span[@class="ivu-select-selected-value"]').click()
        self.element_location('xapth', f'//li[contains(@class,"ivu-select-item") and text()={ctype}]').click()
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人证件号")]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人证件号")]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[contains(@placeholder,"请输入法人证件号")]').send_keys(value)

    def select_type_file(self, path1, path2):
        self.element_location('xpath',
                              '//input[contains(@placeholder,"证件（人像面）")]/../a[contains(text(),"添加文件")]').click()
        upload_file(path1)
        self.element_location('xpath',
                              '//input[contains(@placeholder,"证件（国徽面）")]/../a[contains(text(),"添加文件")]').click()
        upload_file(path2)

    def submit_company_auth(self):
        button = self.element_location('xpath', '//button[@class="ml110 f4 ivu-btn ivu-btn-primary"]')
        flag = button.get_property('disabled')
        if flag is False:
            button.click()
        else:
            print("不可点击")


class BOCFile(WebKeys):

    def boc_file(self, path):
        self.element_location(('xpath', '//i[@class="ivu-icon ivu-icon-ios-cloud-upload-outline"]')).click()
        upload_file(path)

    def submit_boc_file(self):
        self.element_location('xpath', '//button[@class="ivu-btn ivu-btn-primary"]/span[text()="提交"]')


class CAMessage(WebKeys):

    def select_currency(self, currency):
        self.element_location('xpath', '//span[@class="ivu-select-placeholder"]').click()
        self.element_location('xpath', f'//li[contains(@class,"ivu-select-item") and text()={currency}]').click()

    def select_bank(self):
        self.element_location('xpath', '//span[@placeholder="请选择开户行"]').click()
        self.elements_location('xpath', '//input[@placeholder="请选择开户行"]/../../following-sibling::div//li[contains(@class, "ivu-select-item")]')[0].click()

    def input_bank_no(self, value):
        self.element_location('xpath', '//input[contains(@placeholder,"请输入银行账号")]').send_keys(Keys.CONTROL, 'a')
        self.element_location('xpath', '//input[contains(@placeholder,"请输入银行账号")]').send_keys(Keys.BACK_SPACE)
        self.element_location('xpath', '//input[contains(@placeholder,"请输入银行账号")]').send_keys(value)

    def submit_ca_message(self):
        self.element_location('xpath', '//button[@class="f4 ivu-btn ivu-btn-primary"]/span[text()="下一步"]')


