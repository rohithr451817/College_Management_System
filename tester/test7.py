from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

s = Service()
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
# driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("rohi1")
driver.find_element(By.XPATH, "//input[@id='name']").clear()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("rohi2")

# input_feilds=driver.find_element(By.XPATH, "//input[@id='name']")
# input_feilds.send_keys("rohi")
# input_feilds.clear()
# input_feilds.send_keys("rohi22")

alter=driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']")
alter_text = alter.text
print(alter_text)

