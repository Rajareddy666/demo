from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=options)

#right click
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
right=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)
act.context_click(right).perform()
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
driver.switch_to.alert.accept()