from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class Homepage():
    def __init__(self, driver):
        self.driver = driver
        self.dropdown_menu = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
        self.logout_button = (By.XPATH, "//a[@href='/web/index.php/auth/logout']")  

    def click_dropdown_menu(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.dropdown_menu)
        )
        home_field=self.driver.find_element(*self.dropdown_menu)
        home_field.click()
        time.sleep(1)

    def click_logout(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.logout_button)
        )
        self.driver.find_element(*self.logout_button).click()
        