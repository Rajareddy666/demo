from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
wsg=driver.find_element(By.XPATH,"//div[@id='box3']")
des=driver.find_element(By.XPATH,"//div[@id='box103']")
act=ActionChains(driver)
act.drag_and_drop(wsg,des).perform()