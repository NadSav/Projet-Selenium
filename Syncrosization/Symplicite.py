
import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www,google.ca")
#time.sleep(4)
#driver.find_element(By.XPATH,'//input[@name="q"]').send_keys("selenium")
driver.find_element(By.NAME,"q").send_keys("selenium")
searchgoogle=MyWait.until(EC.presence_of_element_located((By.NAME,"q")))


time.sleep(4)
driver.close