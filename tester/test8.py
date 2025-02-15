from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("detach", True)

s = Service()
driver = webdriver.Chrome(service=s)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
driver.find_element(By.ID , "checkBoxOption1").click()
driver.find_element(By.XPATH,"//*[@id='checkBoxOption3']").click()
driver.find_element(By.XPATH , "//*[@id='checkBoxOption2']").click()
time.sleep(3)
# print(check_box)
# print(len(check_box))
# for check_bo in check_box:
#     # if check_box.index(check_bo)+1 < 3 :  or index(check_bo)+1 !=2 :  this is for the limit the checkbox in if condition 
#     check_bo.click()


# (//input[starts-with(@name,'checkBoxOption')])[position()<3]   for the limit the postion 