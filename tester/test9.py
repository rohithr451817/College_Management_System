from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service()
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
drop = driver.find_element(By.ID , "dropdown-class-example")# here we can use the xpath also by seeing the chrome browser 
select = Select(drop)
select.select_by_index(2)
# driver.implicitly_wait(3.5) we can use this also .. but it will not wait for other func , it will do its work 
# this is selenium wait condiition , 
time.sleep(2)
select.select_by_visible_text("Option2")
time.sleep(1)
select.select_by_value("option3")

