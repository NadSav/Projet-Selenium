import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://testautomationpractice.blogspot.com')
time.sleep(4)
#recuperation de lignes et colonne d'une table
lignes_table=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
print(len(lignes_table))
colonnes_table=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
print(len(colonnes_table))
#recuper des valeurs
valeur_cell=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[3]/td[1]")
print(valeur_cell.text)
#recuper toutes le donne du table
nb_lignes=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
nb_colonne=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
time.sleep(3)
valeur_head=driver.find_elements(By.XPATH,"//table[@name='BookTable']//th")
'''for h in range(1,len(valeur_head)+1):
    data_head = driver.find_element(By.XPATH, "//table[@name='BookTable']//th[" + str(h) + "]").text
    print(data_head)'''
for r in range(2,nb_lignes+1):    #Valuers de tout la table
    for c in range(1,nb_colonne):
        val_cell=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
        print(val_cell,end="       ")
    print()
time.sleep(4)
for r in range(2,nb_lignes+1):     #Valuer auter Amin seulement
    val_auteur=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if val_auteur=='Amit':
        prix= driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[4]").text
        nom_liv= driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(r) + "]/td[1]").text
        print(val_auteur,"*******",prix,"*******",nom_liv)
driver.close()

