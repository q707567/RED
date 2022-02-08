import time
from Project.Pay.CreatCompany.creat_company_page import CreatCompany
from Project.common_els import Common


class CreatCompanyOper(CreatCompany, Common):

    def creat_company_submit(self, name, address):
        self.input_name(name)
        self.select_province()
        self.input_address(address)
        self.submit()
