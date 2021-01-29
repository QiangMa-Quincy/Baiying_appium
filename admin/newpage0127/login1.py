from appium.webdriver.common.mobileby import MobileBy
from admin.newpage0127.base_page import BasePage


class LoginOn(BasePage):
    """
    登陆实施
    """
    basepage =BasePage

    def login_to_baiying(self):
        self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/m_main_image5") #进入"我的"页面
        """
        收入账号、密码
        登陆
        :return:
        """
        try:
            self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/tv_no_login")
        except:
            #如果没有找到登陆元素
            #点击设置-退出登陆
            self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/ll_setting")
            self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/tv_login_out")
            self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/m_btn2")
            self.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/m_main_image5") #点击"我的"
            self.login_to_baiying()
            #print(123)
            return True#加了returen不报错了

        el2 = self.find(MobileBy.ID, "com.lenovo.SmartOffice:id/et_login_or_psw_edit")
        el2.send_keys("18613368127")
        self.find_and_click(MobileBy.ID, "com.lenovo.SmartOffice:id/bt_login_next_or_login")
        el4 = self.find(MobileBy.ID,"com.lenovo.SmartOffice:id/et_password")
        el4.send_keys("plg123456")
        self.find_and_click(MobileBy.ID,"com.lenovo.SmartOffice:id/b_login")

        return True