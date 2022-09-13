from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

print("HI...")
userid=input("enter your irctc username:")
pswrd=input("enter your irctc password:")
from_input = input("Enter your origin: ")
to_input = input("Enter your destination: ")

date_input = input("enter the desired date in DD/MM/YYYY formate: ") 
class_list = [
    "Anubhuti Class (EA)",
    "AC First Class (1A)",
    "Vistadome AC (EV)",
    "Exec. Chair Car (EC)",
    "AC 2 Tier (2A)",
    "First Class (FC)",
    "AC 3 Tier (3A)",
    "AC 3 Economy (3E)",
    "Vistadome Chair Car (VC)",
    "AC Chair car (CC)",
    "Sleeper (SL)",
    "Vistadome Non AC (VS)",
    "Second Sitting (2S)"
]

ci = int(input("enter you class_choice:"))
class_input = class_list[ci]

quota_list = [
    "GENERAL",
    "LADIES",
    "LOWER BERTH/SR.CITIZEN",
    "PERSON WITH DISABILITY",
    "TATKAL",
    "PREMIUM TATKAL"
]
ql = int(input("enter you quota_choice:"))
quota_input = quota_list[ql]

print("You will be redirected to site for searching trains....")
driver =  webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.irctc.co.in/nget/train-search')
time.sleep(2)
driver.maximize_window()

alert_element = driver.find_element(By.XPATH, '/html/body/app-root/app-home/div[1]/app-header/p-dialog[2]/div/div/div[2]/div/form/div[2]/button')
alert_element = alert_element.click()
time.sleep(2)

driver.find_element(By.XPATH,'/html/body/app-root/app-home/div[1]/app-header/div[2]/div[2]/div[1]/a[1]').click()
time.sleep(2)

driver.find_element(By.XPATH, '//input[@formcontrolname="userid"]').send_keys(userid)
driver.find_element(By.XPATH, '//input[@formcontrolname="password"]').send_keys(pswrd)
time.sleep(50) #extra time for entering captcha manually
driver.find_element(By.XPATH, '//*[@id="login_header_disable"]/div/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/form/span/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="origin"]/span/input').send_keys(from_input)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="destination"]/span/input').send_keys(to_input)
time.sleep(2)
date = driver.find_element(By.XPATH, '//*[@id="jDate"]/span/input')
date.send_keys(Keys.CONTROL + "a")
date.send_keys(Keys.DELETE)
date.send_keys(date_input)
date.send_keys(Keys.ENTER)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[2]/span').click()
driver.find_element(By.XPATH, '//li/span[contains(text(),"'+class_input+'")]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div/div[2]/span').click()
driver.find_element(By.XPATH, '//li/span[contains(text(),"'+quota_input+'")]').click()
time.sleep(20)
if driver.find_element(By.XPATH, '//span[contains(text(), "Confirmation")]'):
    driver.find_element(By.XPATH,'//button/span[contains(text(), "OK")]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[2]/div[1]/app-jp-input/div/form/div[5]/div/button').click() #search button
time.sleep(10)
driver.find_element(By.XPATH, '//label[contains(text(),"Flexible With Date")]').click()
driver.find_element(By.XPATH, '//label[contains(text(),"Train with Available Berth")]').click()
time.sleep(6)
driver.find_element(By.XPATH, '//*[@id="divMain"]/div/app-main-page/div/div/div[1]/div[1]/div[1]/app-jp-input/div/form/div[5]/div/button').click()
driver.close()