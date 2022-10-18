from datetime import datetime
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from time import sleep
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from db_connect import insert_varibles_into_table_messagesend
from string import Template
from datetime import datetime


browser = webdriver.Firefox(executable_path=r'C:\\xampp\\htdocs\\projetlinkedin\\geckodriver.exe')
url = "http://linkedin.com/"
# path to browser web driver		
browser.get(url)
# Getting the login element
username = browser.find_element(By.ID,"session_key")

# Sending the keys for username	
username.send_keys("idia-curi@nic.sn")

# Getting the password element								
password = browser.find_element(By.ID,"session_password")

# Sending the keys for password
password.send_keys("@Idia.CuRi2022")	

# Getting the tag for submit button					
browser.find_element(By.CLASS_NAME,"sign-in-form__submit-button").click()
sleep(2)

n_pages=42

for n in range(42,n_pages):
    browser.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page="+ str(n))
    sleep(2)
    

    all_buttons = browser.find_elements(By.TAG_NAME, 'button')
    message_buttons = [btn for btn in all_buttons if btn.text == "Message"]
    for i in range(0,len(message_buttons)):
            #click sur le boutton message
            browser.execute_script("arguments[0].click();",message_buttons[i])
            sleep(2)

            #activation de main_div
            main_div = browser.find_element(By.XPATH,"//div[starts-with(@class,'msg-form__msg-content-container')]")
            #main_div.click()
            browser.execute_script("arguments[0].click();",main_div)

            #type de message
            paragraphs = browser.find_element(By.CSS_SELECTOR, ".msg-form__contenteditable")
            all_span = browser.find_elements(By.TAG_NAME,"span")
            all_span= [s for s in all_span if s.get_attribute("aria-hidden") == "true"]
            ind = [*range(17,54,4)]
            all_prenom = []
            all_nom=[]
            for j in ind:
                prenom = all_span[j].text.split(" ")[0]
                nom= all_span[j].text.split(" ")[1]
                all_prenom.append(prenom)
                all_nom.append(nom)
            message="Bonjour "+ all_prenom[i] + ", Dans le cadre du projet IDIA (initiative pour le Développement de l'IA), l'université Cheikh Anta Diop est en train de mener des recherches pour promouvoir l'usage de l'intelligence artificielle et d'anticiper sur les effets désastreux de ses applications non contrôlées. Ces recherches sont inscrites dans une démarche inclusive afin que les résultats puissent avoir le plus grand impact. En tant qu'acteur de l'écosystème numérique, votre avis nous intéresse et vos observations seront sans doute d'un apport précieux pour des résultats plus probants et au profit de la société. \n C'est pourquoi nous vous saurions gré de bien vouloir prendre quelques minutes pour répondre à ce questionnaire et nous faire part de votre avis sur les aspects techniques et éthique pour une IA responsable.Pour toute question supplémentaire veuillez-vous adresser à Dr Modou Gueye, enseignant-chercheur informaticien à l'UCAD (modou2.gueye@ucad.edu.sn) ou à Dr Fatou Ndiaye, enseignante-chercheuse sociologue à l'UCAD (sfndiayeucad@gmail.com).\n Cliquer sur ce lien  https://www.nayaa.fr/idia/projetlinkedin/formulaire.php?id="+all_prenom[i]+"&id2="+all_nom[i]+ " pour remplir le formulaire.\n Merci infiniment."
            paragraphs.send_keys(message)
            sleep(2)
            #envoie de message
            browser.find_element(By.CLASS_NAME,"msg-form__send-button").click()
            insert_varibles_into_table_messagesend(all_prenom[i], all_nom[i], datetime.now())

            sleep(1)

            #fermer div
            close_button= browser.find_element(By.XPATH,'/html/body/div[5]/aside/div[2]/header/div[4]/button[3]/span')
            browser.execute_script("arguments[0].click();",close_button)
            sleep(1)
