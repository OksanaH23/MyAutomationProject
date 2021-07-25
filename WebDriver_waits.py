from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/account")
driver.maximize_window()

# Oksana Herelyuk 07/24/2021
 # By clicking on the "Continue" or "Login" buttons, use WebDriverWait
# with expected condition element_to_be_clickable instead of driver.find_element_by*


wd_wait = WebDriverWait(driver, 10)

loginbtn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))
continuebtn = wd_wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Continue')]")))
continuebtn.click()

# Added an explicit wait here until the “Register Account” title will be visible.
title = wd_wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='content'] /h1")))
