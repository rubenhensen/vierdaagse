from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# import required module
from playsound import playsound

playsound('./iphone_notification.mp3')
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.4daagse.nl/meedoen/ticket-overdragen")
wait = WebDriverWait(driver, 30)
element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']")))
element.click()
element = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Zoek ticket")))
element.click()
driver.switch_to.frame("atleta-embed")
try:
    # Zoek de knop met het attribuut name="English"
    english_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='English']")))
    
    # Als de knop gevonden is, klik erop
    english_button.click()
    
    # Wacht tot het taalmenu zichtbaar is en klik op de link met name="Nederlands"
    wait = WebDriverWait(driver, 10)
    nederlands_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@name='Nederlands']")))
    nederlands_link.click()
    
    print("Taal succesvol gewijzigd naar Nederlands")
    
except NoSuchElementException:
    # Als er geen knop met name="English" is, dan hoeft er niets te gebeuren
    print("De pagina staat niet op Engels of de taalknop heeft een ander formaat")


while True:
    if (len(driver.find_elements(By.XPATH, "//a[normalize-space()='Ticket kopen']")) != 0):
        element = driver.find_element(By.XPATH, "//a[normalize-space()='Ticket kopen']")
        element.click()
    if (len(driver.find_elements(By.XPATH, "//button[normalize-space()='Ticket kopen']")) != 0):
        element = driver.find_element(By.XPATH, "//button[normalize-space()='Ticket kopen']")
        element.click()
        # for playing note.wav file
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
    if (len(driver.find_elements(By.XPATH, "//span[normalize-space()='Ticket kopen']")) != 0):
        element = driver.find_element(By.XPATH, "//span[normalize-space()='Ticket kopen']")
        element.click()
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
        playsound('./iphone_notification.mp3')
    if (len(driver.find_elements(By.XPATH, "//span[text()='Vernieuwen']")) != 0):
        if (len(driver.find_elements(By.XPATH, "//span[text()='Vernieuwen']")) != 0):
            element = driver.find_element(By.XPATH, "//span[text()='Vernieuwen']")
            element.click()