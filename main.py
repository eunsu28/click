from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib.request 

URL = "https://www.instagram.com/dlwlrma/"

driver = webdriver.Chrome("chromedriver")
driver.get(URL)