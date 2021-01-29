from admin.newpage0127.base_page import BasePage
from admin.newpage0127.mainpage import Main


class Test_Main:
    def setup(self):
        basepage= BasePage()
        self.mainpage = Main(basepage)

    def test_launch_mainpage(self):
        self.mainpage.launch_mainpage()