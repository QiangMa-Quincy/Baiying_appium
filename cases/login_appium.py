from admin.newpage0127.base_page import BasePage
from admin.newpage0127.mine import Mine
from admin.page.app import APP


class TestLogin:
    def setup(self):
        basepage= BasePage()
        self.mine =Mine(basepage)

    def test_login(self):
        result = self.mine.goto_login().Login_to_baiying()
