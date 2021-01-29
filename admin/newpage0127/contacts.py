from appium.webdriver.common.mobileby import MobileBy
from admin.newpage0127.pre_page import PrePage


class Contacts(PrePage):
    def launch_contacts(self):
        """
        进入通讯录PO
        :return:
        """
        self.basepage.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/m_main_image_im")
        return True