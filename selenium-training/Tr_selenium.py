from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import time
import os
from pathlib import Path

# avatar_path = os.path.join(Path(__file__).resolve().parent, "ayoub.png")

# driver = webdriver.Chrome()

# new_account = {
#     "username": "ayoub-dj",
#     "name": "ayoub",
#     "bio": "Hello I am Ayoub",
#     "email": "ayoub@aol.com",
#     "password1": "ayoub@123pass",
#     "password2": "ayoub@123pass",
# }


# driver.get("http://127.0.0.1:8000/register/")

# def wait_for_readyState():
#     wait = WebDriverWait(driver, 10)
#     wait.until(lambda d: d.execute_script("return document.readyState") == "complete")

# wait_for_readyState()

# email_field = driver.find_element(By.NAME, 'email')
# username_field = driver.find_element(By.ID, 'id_username')
# password1_field = driver.find_element(By.NAME, 'password1')
# password2_field = driver.find_element(By.NAME, 'password2')
# submit_button_signup = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Sign up']")

# email_field.send_keys(new_account["email"])
# username_field.send_keys(new_account["username"])
# password1_field.send_keys(new_account["password1"])
# password2_field.send_keys(new_account["password2"])

# submit_button_signup.send_keys(Keys.RETURN)

# wait_for_readyState()

# # avatar_path
# avatar_filed = driver.find_element(By.ID, "id_avatar")
# name_filed = driver.find_element(By.NAME, "name")
# bio_filed = driver.find_element(By.ID, "id_bio")
# submit_button_profile = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Complete Your Profile']")

# avatar_filed.send_keys(avatar_path)
# name_filed.send_keys(new_account["name"])
# bio_filed.send_keys(new_account["bio"])


# submit_button_profile.click()



# time.sleep(100)
# # driver.close() # to close a page
# driver.quit() # To close the entire browser


# driver = webdriver.Chrome()

# driver.get("http://127.0.0.1:8000/login/")


# By.ID	The first element with the id attribute value matching the location will be returned.
# element = driver.find_element(By.ID,"email-id")

# By.NAME	The first element with the name attribute value matching the location will be returned.
# element = driver.find_element(By.NAME, "password")

# By.XPATH	The first element with the xpath syntax matching the location will be returned.
# element = driver.find_element(By.XPATH, "//input[@type='submit'")

# By.LINK_TEXT	The first element with the link text value matching the location will be returned.
# <a href="http://example.com">Click Here</a> 
# element = driver.find_element(By.LINK_TEXT, "Click Here") # Exact Match:

# By.PARTIAL_LINK_TEXT	The first element with the partial link text value matching the location will be returned.
# <a href="http://example.com">Click Here</a>
# element = driver.find_element(By.LINK_TEXT, "Click") # # Partial Match


# By.TAG_NAME	The first element with the given tag name will be returned.
# element = driver.find_element(By.TAG_NAME, "div")

# By.CLASS_NAME	the first element with the matching class attribute name will be returned.
# element = driver.find_element(By.CLASS_NAME, ".container")


# By.CSS_SELECTOR	The first element with the matching CSS selector will be returned.
# element = driver.find_element(By.CSS_SELECTOR, ".container h2")


# to find multiple elements
# elements = driver.find_elements()

# element.send_keys("some text") # To send text key 
# element.clear() # To clear the content od an element 



# Waits in selenium
# Sets a default wait time for the WebDriver
# driver.implicitly_wait(10)


# Allows you to wait for a specific condition 
# wait = WebDriverWait(driver, 6)

# wait 5 seconds before looking for element
# element = WebDriverWait(driver, 5).until(
#     EC.presence_of_element_located((By.CLASS_NAME, "text"))
# )


# driver = webdriver.Chrome()

# driver.get("https://www.youtube.com/results?search_query=selenium+in+python")

# wait = WebDriverWait(driver, 10)

# elements = driver.find_elements(By.CLASS_NAME, "ytd-item-section-renderer #dismissible")

# target_element = elements[1].find_element(By.ID, 'thumbnail')

# target_element.click()

# url = target_element.get_attribute('href')





# Action Chains in selenium
driver = webdriver.Chrome()

driver.get("https://chatgpt.com/")

wait = WebDriverWait(driver, 10)

search_bar = driver.find_element(By.ID, "prompt-textarea")
send_btn = driver.find_element(By.CSS_SELECTOR, '[data-testid="send-button"]')


search_bar.click()

question = 'How can I see how are you in spanish and only tell me the answer only'

search_bar.send_keys(question)

send_btn.click()

time.sleep(100)