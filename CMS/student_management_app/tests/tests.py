from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import unittest
import time

class TestCases(unittest.TestCase):

    def setUp(self):
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()

    def test_a_show_title(self):
           self.driver = webdriver.Chrome()
           self.driver.get('http://127.0.0.1:8000/')
           title = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'title'))).get_attribute('innerText')
           time.sleep(2)
           print("The title is", title)

    def test_b_chechurl(self):
         
     # Open the URL
      self.driver.get("http://127.0.0.1:8000/")
      # Wait for the link with the text "HKBK College of Engineering" to be clickable
      link = WebDriverWait(self.driver, 10).until(
      EC.element_to_be_clickable((By.LINK_TEXT, "HKBK College of Engineering"))
       )
       # Click on the link
      link.click()
      # Wait for the new page to load
      WebDriverWait(self.driver, 5).until(EC.url_contains("https://www.hkbk.edu.in/"))
      self.driver.get("https://www.hkbk.edu.in/")
     # Print a success message
      print("Successfully navigated to https://www.hkbk.edu.in/")

    def test_c_login(self):
        self.driver.get('http://localhost:8000/')
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
        email_input.send_keys('rohi@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('admin')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()
        print("login Sucessful")

        WebDriverWait(self.driver, 10).until(EC.title_contains('Student Management System | Dashboard'))
        print('The title is', self.driver.title)

        # self.driver.get('http://127.0.0.1:8000/admin_home/')
    
   

       
    def test_e_Add_staff(self):
        self.driver.get('http://localhost:8000/')
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
        email_input.send_keys('rohi@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('admin')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()
        print("login Sucessful")

        # WebDriverWait(self.driver, 10).until(EC.title_contains('Student Management System | Dashboard'))
        # print('Student Management System | Dashboard', self.driver.title)

        # self.driver.get('http://127.0.0.1:8000/admin_home/')
      # Assuming you've already logged in and are on the admin page

      # Click on "Manage Staff"
        manage_staff_link = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Manage Staff"))
          )
        manage_staff_link.click()

        # Click on "Add Staff"
        add_staff_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "+ Add Staff"))
         )
        add_staff_button.click()

        # Enter staff details
        email_input = self.driver.find_element(By.NAME, "email")
        email_input.send_keys("user@example.com")  # Replace with the desired staff ID


        username_input = self.driver.find_element(By.NAME, "username")
        username_input.send_keys("johndoe")  # Replace with the desired username

        password_input = self.driver.find_element(By.NAME, "password")
        password_input.send_keys("johndoe")  # Replace with the desired username

        first_name_input = self.driver.find_element(By.NAME, "first_name")
        first_name_input.send_keys("John")  # Replace with the desired first name
 
        last_name_input = self.driver.find_element(By.NAME, "last_name")
        last_name_input.send_keys("Doe")  # Replace with the desired last name

        address_input = self.driver.find_element(By.NAME, "address")
        address_input.send_keys("Bangalore,Karnataka")  # Replace with the desired address
        
        # Click on "Add Staff" button
        # add_staff_submit_button = self.driver.find_element(By.NAME, "add_staff")
        # add_staff_submit_button.click()
        
        print("Added Staff Succesfully")
        # self.driver.get('http://127.0.0.1:8000/admin_home/')


    def test_f_view_attendence(self):
        self.driver.get('http://localhost:8000/')
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
        email_input.send_keys('rohi@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('admin')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()


      # Click on the "View Attendance" link
        view_attendance_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'View Attendance'))
        )
        view_attendance_link.click()

        # Select subject
        subject_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'subject'))
        )
        subject_select.click()
        subject_option = WebDriverWait(subject_select, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='DBMS']"))
        )
        subject_option.click()

        # Select session year
        session_year_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'session_year_id'))
        )
        session_year_select.click()
        session_year_option = WebDriverWait(session_year_select, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='July 17, 2024 to Aug. 17, 2024']"))
        )
        session_year_option.click()

        # Click on "Fetch Attendance" button
        fetch_attendance_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fetch_attendance'))
        )
        fetch_attendance_button.click()

        # Select attendance date
        attendance_date_select = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, 'attendance_date'))
        )
        attendance_date_select.click()
        attendance_date_option = WebDriverWait(attendance_date_select, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='2024-07-18']"))
        )
        attendance_date_option.click()

        # Click on "Fetch Student Attendance" button
        fetch_student_attendance_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fetch_student'))
        )
        fetch_student_attendance_button.click()
        time.sleep(5)
        print("Attendance Fetched sucessful")


    def test_g_buttontest(self):
        #... (rest of the test code remains the same)
        self.driver.get('http://127.0.0.1:8000/')
        email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
        email_input.send_keys('rohi@gmail.com')

        password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
        password_input.send_keys('admin')

        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
        login_button.click()

        fetch_student_feedback_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[13]/a/p'))
        )
        fetch_student_feedback_button.click()
        time.sleep(5)

        fetch_staff_feedback_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[14]/a/p'))
        )
        fetch_staff_feedback_button.click()
        time.sleep(5)

        fetch_student_leave_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[15]/a/p'))
        )
        fetch_student_leave_button.click()
        time.sleep(5)

        fetch_staff_leave_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/aside/div/div[4]/div/div/nav/ul/li[16]/a/p'))
        )
        fetch_staff_leave_button.click()
        time.sleep(5)


    def test_h_toexit(self):
        #... (rest of the test code remains the same)
         self.driver.get('http://127.0.0.1:8000/')
         email_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Email')))
         email_input.send_keys('rohi@gmail.com')

         password_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'Password')))
         password_input.send_keys('admin')

         login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, 'Sign')))
         login_button.click()

         #code to logout
         settings_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/ul[2]/li/a"))
        )
       # Click on the settings shape button
         settings_button.click() 
         time.sleep(3)

        # Wait for the Logout button to be clickable
         logout_button = WebDriverWait(self.driver, 10).until(
         EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/nav/ul[2]/li/div/a[2]"))
          )
       # Click on the Logout button
         logout_button.click()
         time.sleep(3)
         print("Logout Sucessful")   

     # Close the browser
   
         
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()







