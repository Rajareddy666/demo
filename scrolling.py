from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)
serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj,options=options)
driver.get("https://www.worldometers.info/geography/flags-of-the-world/")
#starting to middle
#driver.execute_script("window.scrollBy(0,3000)","")
#value=driver.execute_script("return.pageYOffset;")
#print(value)

#stop by match_value
#flag=driver.find_element(By.XPATH,"//img[@src='/img/flags/small/tn_in-flag.gif']")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#value=driver.execute_script("return window.pageYOffset;")
#print(value)

#top-bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(value)