from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
min_sli = driver.find_element(By.XPATH,"//span[1]")
max_sli = driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[2]/span[2]")
print(min_sli.location) #{'x': 59, 'y': 250}
print(max_sli.location) #{'x': 412, 'y': 250}
act=ActionChains(driver)
act.drag_and_drop_by_offset(min_sli,+100,0).perform()
act.drag_and_drop_by_offset(max_sli,-100,0).perform()
print(min_sli.location)
print(max_sli.location)