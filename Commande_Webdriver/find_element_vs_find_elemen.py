import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(4)
driver.find_element(By.NAME,'Username').send_keys('Admin')
time.sleep(4)
driver.find_element(By.NAME,'password').send_keys('admin123')
time.sleep(4)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
time.sleep(4)
#find_elements
list_link=driver.find_elements(By.NAME,'a')
print(len(list_link))
time.sleep(2)
print('Le test du premier lien est:',list_link[3].text)
for link in list_link:
    print(link.text)
time.sleep(4)
driver.close
