from appium.webdriver.common.mobileby import MobileBy
from admin.newpage0127.pre_page import PrePage


class Mine(PrePage):
    def launch_minepage(self):
        """
        进入我的PO
        :return:
        """
        self.basepage.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/m_main_image5")
        return True

