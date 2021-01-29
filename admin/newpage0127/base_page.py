# 操作方法的封装
from appium import webdriver


class BasePage:
    def __init__(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "emulator-5554"
        caps["appPackage"] = "com.lenovo.SmartOffice"
        caps["appActivity"] = ".axianniu.MainActivity"
        # noReset 保留缓存， 比如登录状态
        caps["noReset"] = "True"
        # 不停止应用，直接运行测试用例
        # caps["dontStopAppOnReset"] = "true"
        caps['skipDeviceInitialization'] = 'true'
        caps['skipServerInstallation'] = 'true'
        # caps["settings[waitForIdleTimeout]"] = 0
        # 关键  localhost:4723  本机ip:server端口
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
        self.driver.implicitly_wait(15)  # 隐式等待

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def send(self, by, locator, content):
        self.find(by, locator).send_keys(content)

    def screenshot(self, picture_path):
        self.driver.save_screenshot(picture_path)
