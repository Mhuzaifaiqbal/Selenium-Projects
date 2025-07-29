import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.homepage import Homepage

class TestLogin:
    @classmethod
    def setup_class(cls):
        print("Setting up driver...")
        cls.service = Service(executable_path="chromedriver.exe")  # adjust path
        cls.driver = webdriver.Chrome(service=cls.service)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        cls.login_page = LoginPage(cls.driver)
        cls.homepage = Homepage(cls.driver)

    def test_login(self):
        print("Starting login test...")
        self.login_page.enter_username("Admin")
        self.login_page.enter_password("admin123")
        self.login_page.click_login()

        print("Waiting for user dropdown to appear...")
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.homepage.dropdown_menu)
        )

        print("Clicking dropdown menu...")
        self.homepage.click_dropdown_menu()
        print("Clicking logout...")
        self.homepage.click_logout()

        time.sleep(2)

    @classmethod
    def teardown_class(cls):
        print("Tearing down...")
        cls.driver.quit()
        cls.service.stop()
        print("Teardown complete.")

if __name__ == "__main__":
    TestLogin.setup_class()
    test = TestLogin()
    test.test_login()
    TestLogin.teardown_class()
