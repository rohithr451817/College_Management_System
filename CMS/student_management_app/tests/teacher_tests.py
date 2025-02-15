from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import unittest
import time

class TestCases(unittest.TestCase):
    # def setUp(self):
    #     driver = webdriver.Chrome()
    #     driver.maximize_window()

    # def test_l_showtitle(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.maximize_window()         
    #     self.driver.get('http://localhost:8000/')
    #     title = self.driver.title
    #        # Print the title
    #     print(f'Title of the page is: {title}')
    #     time.sleep(2)
 

    def test_m_stafflogin(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get('http://localhost:8000/')

        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'Email')) )
        email_input.send_keys('Vinayak@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('staff1556666')

        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()

        try:
          WebDriverWait(self.driver, 10).until(
          EC.presence_of_element_located((By.ID, 'subject')))
          print("Login successful")
        except TimeoutException:
          print("Login unsuccessful")
        
        time.sleep(2)
        # self.driver.get('http://127.0.0.1:8000/staff_home/')


    
    def test_n_leave(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get('http://localhost:8000/')
       
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')) )
        email_input.send_keys('Vinayak@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('staff')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()

       
        # Wait for the Leave Date input field to be clickable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[5]/a/p"))).click()

        # Enter the date
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[1]/div[1]/input").send_keys("25-07-2024")

        # Wait for the Leave Reason text area to be clickable
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[1]/div[2]/textarea"))).click()

        # Enter the reason
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[1]/div[2]/textarea").send_keys("Give me holiday")

        # Click on the Apply for Leave button
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[2]/button").click()
         
        time.sleep(2)
       
    def test_o_feedback(self):
        self.driver = webdriver.Chrome() 
        self.driver.maximize_window()
        self.driver.get('http://localhost:8000/')
       
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')) )
        email_input.send_keys('Vinayak@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('staff')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[6]/a"))).click()

        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[1]/div/textarea").send_keys("No proper facilities , undiscipline students, error board, no chalk")
        
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/section/div/div[1]/div/div/form/div[2]/button").click()
         
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()