import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://technologychannel.github.io/SampleWebsite/')
username = browser.find_element(by=By.NAME,value="username")
username.send_keys("beingbivek" + Keys.RETURN)
time.sleep(1)
password = browser.find_element(by=By.NAME,value="password")
password.send_keys("123456789" + Keys.RETURN)
time.sleep(1)
button = browser.find_element(by=By.TAG_NAME("button"))
button.click()