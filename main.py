from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

#Define driver,options and service
chrome_options=Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")
service = Service('/Users/harshithharsha/PycharmProjects/pythonProject/Web-Automation/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(options=chrome_options,service=service)


#Loading the wb page
driver.get('https://demoqa.com/login')

#Locate username,password and login button
username_field=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'userName')))
password_field=WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.ID,'password')))
login_button=driver.find_element(By.ID,'login')


#Fill in username and password and click the button
username_field.send_keys('HarshithReddy-Audipudi')
password_field.send_keys('Qwerty@123')
driver.execute_script("arguments[0].click();",login_button)

input("Press enter to close the browser")
driver.quit()

