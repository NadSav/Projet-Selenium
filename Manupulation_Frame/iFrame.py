import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame('packageListFrame')   #by name
driver.find_element(By.LINK_TEXT,"//a[text()='org.openqa.selenium']").click()
driver.switch_to.default_content()
driver.switch_to.frame('packageFrame')
driver.find_element(By.TAG_NAME,"//span[contains(text(),'WebDriver')][1]").click()
driver.switch_to.default_content()
time.sleep(4)


driver.close