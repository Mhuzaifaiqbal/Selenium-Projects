import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service   
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service=Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/")
time.sleep(2)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/ul/li[39]/a"))
)
driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[39]/a").click()
time.sleep(2)   

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/a[2]"))
)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/a[2]").click()
time.sleep(2)

list=["?mode=random","?pixel_shift=100","?mode=random&pixel_shift=100"]
for url in list:
    base_url=driver.current_url
    add_term=url
    full_url=base_url+add_term
    driver.get(full_url)
    time.sleep(2)

time.sleep(2)
driver.quit()
