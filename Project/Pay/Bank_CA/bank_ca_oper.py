import time
from Project.Pay.Bank_CA.bank_ca_page import CompanyAuth, BOCFile, CAMessage
from Project.common_els import Common


class CompanyAuthOper(CompanyAuth, BOCFile, CAMessage, Common):

    def company_auth_submit(self, ca_file, name, ctype, no, type_file1, type_file2):
        self.select_company_auth_file(ca_file)
        self.input_name(name)
        self.input_no(ctype, no)
        self.select_type_file(type_file1, type_file2)
        self.submit_company_auth()

    def bank_file_submit(self,type_file):
        self.boc_file(type_file)
        self.submit_boc_file()

    def ca_message_submit(self,currency,no):
        self.select_currency(currency)
        self.select_bank()
        self.input_bank_no(no)
        self.submit_ca_message()



