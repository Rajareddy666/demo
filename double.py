from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("https://testautomationpractice.blogspot.com/")
field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("Hello! Raja")
button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act=ActionChains(driver)
act.double_click(button).perform()