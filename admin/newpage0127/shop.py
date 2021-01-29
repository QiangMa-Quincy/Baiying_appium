from appium.webdriver.common.mobileby import MobileBy
from admin.newpage0127.pre_page import PrePage


class ShopMall(PrePage):
    def launch_shopmall(self):
        """
        进入商城PO
        :return:
        """
        self.basepage.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/m_main_click2")
        return True