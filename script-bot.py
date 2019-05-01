from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

username = 'username or email'
password = 'pass'

browser = webdriver.Chrome()
browser.get(('url'))

# fill in username and hit the next button
username = browser.find_element_by_id('id_input_username')
username.send_keys(username)

username = browser.find_element_by_id('id_input_password')
username.send_keys(password)

nextButton = browser.find_element_by_id('id_button_submit')
nextButton.click()


# For Google forms login
#password = WebDriverWait(browser, 10).until(
#EC.presence_of_element_located((By.NAME, "password")))
#password.send_keys(passwordStr)
#signInButton = browser.find_element_by_id('passwordNext')
#signInButton.click()