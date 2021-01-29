from admin.newpage0127.login1 import LoginOn

class Test_Login:
    def setup(self):
        self.log = LoginOn()  #LoginON类是继承的BasePage，所以这里不需要再继承

    def test_login(self):
        self.log.login_to_baiying()

