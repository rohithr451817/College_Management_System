from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from  selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option("detach", True)

# if __name__ =='__main__':
s = Service()
driver = webdriver.Chrome(service=s, options=options)
driver.get('https://rahulshettyacademy.com/AutomationPractice/') # here location of the testing website 
driver.maximize_window()
blink = driver.find_element(By.CLASS_NAME,"blinkingText")
print(blink.text)
print(blink.get_attribute("href"))# here we can go to the new website and also do this .. in the same method 

# handi=ling the dropdown 
#in this , take search bar unique id , later on send_keys in code 
# then to select the first option in that , u can go and pause and get the unique link
#use the pause and use // to jump directly from grandparent link 
# after tat same process get_attribute ("href") by using xpath , use time.sleep(2) for live wesite

## for the login pop up , we can use the //button[text()='x]  this is just a method 

