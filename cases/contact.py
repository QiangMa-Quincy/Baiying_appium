from admin.newpage0127.base_page import BasePage
from admin.newpage0127.contacts import Contacts

class TestContact:
    def setup(self):
        basepage = BasePage()
        self.contacts = Contacts(basepage)

    def test_contact(self):
        self.contacts.launch_contacts()
        print("进入通讯录")
