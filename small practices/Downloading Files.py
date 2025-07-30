from selenium import webdriver 
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[17]/a"))
)
driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[17]/a").click()
time.sleep(2)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[4]"))
)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[4]").click()
time.sleep(2)   

driver.quit()