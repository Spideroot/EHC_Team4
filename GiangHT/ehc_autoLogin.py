from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import getpass

usernameStr = input('Email/Username: ')
passwordStr = getpass.getpass('PassWord: ')

browser = webdriver.Chrome()
browser.get(('https://github.com/login'))

# fill in username and hit the next button

username = browser.find_element_by_id('login_field')
username.send_keys(usernameStr)

password =  browser.find_element_by_id('password')
password.send_keys(passwordStr)

signInButton = browser.find_element_by_name('commit')
signInButton.click()
