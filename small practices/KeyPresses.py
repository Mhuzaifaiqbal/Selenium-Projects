import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


service=Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[31]/a"))
)
driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[31]/a").click()
time.sleep(2)
 
WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/form/input"))

)

list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for letter in list:
    path=driver.find_element(By.XPATH, "/html/body/div[2]/div/div/form/input")
    path.clear()
    path.send_keys(letter)
    path.submit()
    time.sleep(0.5)
time.sleep(2)

driver.quit()
    