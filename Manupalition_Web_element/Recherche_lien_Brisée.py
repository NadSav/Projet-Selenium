import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
list_link=driver.find_elements(By.TAG_NAME,"a")
compteur=0
for link in list_link:
    url=link.get_attribute("href")
    try:
        reponse=requests.head(url)
    except:
        None
    if reponse.status_code>=400:
        print(url,"est un lien brise")
        compteur=compteur+1
    else:
        print(url, "est un valide")
print("Le nombre de liste brisee est :",compteur)
time.sleep(4)
driver.close