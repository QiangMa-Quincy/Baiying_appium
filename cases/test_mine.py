from admin.newpage0127.base_page import BasePage
from admin.newpage0127.mine import Mine

class Test_Mine:
    def setup(self):
        basepage= BasePage()
        self.minepage= Mine(basepage)

    def test_launch_mine_page(self):
        self.minepage.launch_minepage()


