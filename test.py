#importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#browsing the respective url
browser.get("https://app.cloudqa.io/home/AutomationPracticeForm")

browser.maximize_window()

#filling first name
first_name = browser.find_element(By.ID, "fname")

first_name.send_keys("Muhammed")

#filling last anme
last_name = browser.find_element(By.ID, "lname")

last_name.send_keys("Sinan C K")

#selecting male checkbox
checkbox = browser.find_element(By.ID, "male")  

checkbox.click()

#filling date of birth
date_of_birth = browser.find_element(By.ID, "dob")

date_of_birth.send_keys("2000-08-08")


#making browser window open for 10 seconds   
time.sleep(10)

#quiting the window 
browser.quit()