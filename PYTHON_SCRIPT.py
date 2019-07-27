# -*- coding: utf-8 -*-
"""
Spyder Editor
code created by jim gitonga

This is a temporary script file.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#webdriver accesing net using chrome
chrome_browser = webdriver.Chrome("C:\webdrivers/chromedriver.exe")

#for opening the facebook login page
chrome_browser.get('https://www.facebook.com/')


#inputing of username_found_using inspect element
username = chrome_browser.find_elements_by_css_selector("input[name=email]")
#eneters the username below
username[0].send_keys('youremail@gmail or any other.com')

#inputing of password
password = chrome_browser.find_elements_by_css_selector("input[name=pass]")
#create a text file to hide your password and let it be read from there
get_password=open("password.txt", "r").readlines()
password[0].send_keys(jim_password)

#for loging in
loginButton = chrome_browser.find_elements_by_css_selector("input[type=submit]")
loginButton[0].click()
#hooray sip coffee as your facebook page opens




