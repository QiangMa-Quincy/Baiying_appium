from appium.webdriver.common.mobileby import MobileBy
from admin.newpage0127.pre_page import PrePage


class Main(PrePage):
    def launch_mainpage(self):
        """
        进入主页PO
        :return:
        """
        self.basepage.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/m_main_image1")
        return True