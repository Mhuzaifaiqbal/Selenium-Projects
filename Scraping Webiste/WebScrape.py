# -----------------PLEASE NOTE THAT I DONOT PROMOTE THE USE OF SCRAPING FOR MALICIOUS PURPOSES-----------------------------------
# This code is for educational purposes only. Please ensure you comply with the terms of service of the website you are scraping.
#MAKE SURE TO READ README. FILE 
import time 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service=Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("")#Amazon.in URL can be placed here since HTML structure for Amazon.in is used in this code (https://www.amazon.in/)
print("Setting up the driver and navigating to Amazon")
driver.maximize_window()

#Sometimes this page might appear and sometimes it may not, so we handle it with a try-except block
try:
    continue_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[3]/div/div/form/div/div/span/span/button"))
    )
    continue_button.click()
    print("Clicked 'Continue' button.")
except:
    print("'Continue' button not found. Skipping...")

WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input"))
)
search=driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
search.send_keys("")#You can enter any search term here
search.submit()



list=[]
for i in range(1,5):
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']"))
    )
    items = driver.find_elements(By.XPATH,"//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal']")
    for item in items:
        list.append(item.text)
        print( "appended to list\n")
    WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//a[contains(@class, 's-pagination-next')]"))
    )
    driver.find_element(By.XPATH,"//a[contains(@class, 's-pagination-next')]").click()
    print("Moving on to the next page\n")
    time.sleep(2)

    
print("Scraping completed. Found", len(list), "items.")
driver.quit()