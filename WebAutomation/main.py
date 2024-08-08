from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Edge()
browser.get('https://google.com')
box = browser.find_element(by=By.NAME,value="q")
box.send_keys("Rich Dad Poor Dad" + Keys.RETURN)