from admin.newpage0127.base_page import BasePage
from admin.newpage0127.shop import ShopMall


class Test_Shop:
    def setup(self):
        basepage =BasePage()
        self.shop = ShopMall(basepage)

    def test_launch_shopmall(self):
        self.shop.launch_shopmall()