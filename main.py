from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request 

URL = "https://www.instagram.com/dlwlrma/"

driver = webdriver.Chrome("/Users/kim-eunsu/Desktop/click/chromedriver")
driver.get(URL)

sleep(5)

facebook_login_btn = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button')
sleep(5) 
facebook_login_btn.click()

