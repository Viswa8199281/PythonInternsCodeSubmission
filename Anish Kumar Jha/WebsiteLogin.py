from selenium import webdriver
import time

#create a connection with your web browswer
browser = webdriver.Chrome("C:/Users/anish/Documents/Hackveda/chromedriver_win32/chromedriver.exe")
browser.maximize_window()
browser.get("https://www.hackveda.in/one2one")
time.sleep(2)

username = browser.find_element_by_id("email")
username
time.sleep(2)

username.send_keys("anishjha989@gmail.com")
time.sleep(2)

password = browser.find_element_by_id("password")
password.send_keys("")
time.sleep(2)

button = browser.find_element_by_id("login_btn")
button.click()
time.sleep(2)

