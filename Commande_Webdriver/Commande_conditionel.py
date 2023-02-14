import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://omayo.blogspot.com/")
time.sleep(4)
Check_list=driver.find_element(By.ID,'checkbox2').is_selected()
print(Check_list)
time.sleep(4)
Check_button=driver.find_element(By.ID,'but1').is_enabled()
print(Check_button)
time.sleep(4)
Check_displayed=driver.find_element(By.ID,'hbutton').is_displayed()
print(Check_displayed)
time.sleep(4)

driver.close