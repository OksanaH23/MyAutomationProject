from selenium import webdriver


driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')


driver.get("https://cleveronly.com/brainbucket/index.php?route=account/account")

driver.maximize_window()
#Complited by Oksana H. 07/07/2021
#Locates an email field and enters e-mail on the Login Page

email_input_field = driver.find_element_by_xpath("//input[@name='email']")
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("ohhomework@gmail.com")

#Locates the password field and enters the password on the Login Page

password_input_field = driver.find_element_by_xpath("//input[@name='password']")
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Brainbucket1122")

#Clicks the “Login” button

logincustomerbtn = driver.find_element_by_xpath("//input[@value='Login']")
logincustomerbtn.click()





