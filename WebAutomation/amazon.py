import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('https://amazon.com')
amazonsearch = browser.find_element(by=By.NAME,value="field-keywords")
amazonsearch.send_keys("the lean startup" + Keys.RETURN)
time.sleep(4)
link = browser.find_element(by=By.CLASS_NAME,value="a-link-normal s-no-outline")
link.click()