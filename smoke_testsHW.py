from selenium import webdriver


driver = webdriver.Chrome(executable_path='Drivers/chromedriver.exe')
driver.get("https://cleveronly.com/brainbucket/index.php?route=account/login")

driver.maximize_window()

logo = driver.find_element_by_xpath("//img[@title='Brainbucket']")

newregistrantbtn = driver.find_element_by_xpath("//a[contains(text(),'Continue')]")
newregistrantbtn.click()

firstname_field = driver.find_element_by_xpath("//fieldset/div[2]")
firstname_field_class = firstname_field.get_attribute("class")
assert "required" in firstname_field_class
firstname_input = driver.find_element_by_id("input-firstname")
firstname_input.clear()
firstname_input.send_keys("Oksana")

# To verify that all required fields have the word "required" in class we use:
# -inspector tool

lastname_field = driver.find_element_by_xpath("//fieldset/div[2]")
lastname_field_class = lastname_field.get_attribute("class")
assert "required" in lastname_field_class
lastname_input = driver.find_element_by_id("input-lastname")
lastname_input.clear()
lastname_input.send_keys("Herelyuk")


email_field = driver.find_element_by_xpath("//fieldset/div[2]")
email_field_class = email_field.get_attribute("class")
assert "required" in email_field_class
email_input = driver.find_element_by_id("input-email")
email_input.clear()
email_input.send_keys("ohhomework@gmail.com")


telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
telephone_field_class = telephone_field.get_attribute("class")
assert "required" in telephone_field_class
telephone_input = driver.find_element_by_id("input-telephone")
telephone_input.clear()
telephone_input.send_keys("773-773-7733")


fax_input = driver.find_element_by_id("input-fax")
fax_input.clear()
fax_input.send_keys("773-773-3377")

company_input = driver.find_element_by_id("input-company")
company_input.clear()
company_input.send_keys("OH Company")

address_1_field = driver.find_element_by_xpath("//fieldset/div[2]")
address_1_field_class = address_1_field.get_attribute("class")
assert "required" in address_1_field_class
address_1_input = driver.find_element_by_id("input-address-1")
address_1_input.clear()
address_1_input.send_keys("1122 N. Bucket St.")


address_2_input = driver.find_element_by_id("input-address-2")
address_2_input.clear()
address_2_input.send_keys()

city_field = driver.find_element_by_xpath("//fieldset/div[2]")
city_field_class = address_1_field.get_attribute("class")
assert "required" in city_field_class
city_input = driver.find_element_by_id("input-city")
city_input.send_keys('Chicago')

zone_id_field = driver.find_element_by_xpath("//fieldset/div[2]")
zone_id_field_class = zone_id_field.get_attribute("class")
assert "required" in zone_id_field_class
zone_id_input = driver.find_element_by_id("input-zone")
zone_id_input.send_keys('Illinois')


postcode_input = driver.find_element_by_id("input-postcode")
postcode_input.clear()
postcode_input.send_keys()

password_field = driver.find_element_by_xpath("//fieldset/div[2]")
password_field_class = password_field.get_attribute("class")
assert "required" in password_field_class
password_input = driver.find_element_by_id("input-password")
password_input.clear()
password_input.send_keys("Brainbucket1122")


confirm_field = driver.find_element_by_xpath("//fieldset/div[2]")
confirm_field_class = confirm_field.get_attribute("class")
assert "required" in confirm_field_class
confirm_input = driver.find_element_by_id("input-confirm")
confirm_input.clear()
confirm_input.send_keys("Brainbucket1122")


      #required field is left without any input.

#telephone_field = driver.find_element_by_xpath("//fieldset/div[2]")
#telephone_field_class = telephone_field.get_attribute("class")
#assert "required" in telephone_field_class
#telephone_input = driver.find_element_by_id("input-telephone")
#telephone_input.clear()
#telephone_input.send_keys()-------no input

#   - also to test if all required fields enters information we could run script like this one:

# submityoupersonaldetailsbtn = driver.find_element_by_xpath("//input[@value='Continue']")
# submityoupersonaldetailsbtn.click()
#    If required field is left without any input it will return framed in red.
#Complited by Oksana H. 07/07/2021