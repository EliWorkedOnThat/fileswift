from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import random
import time

# Path to your ChromeDriver
chrome_driver_path = 'C:\\Users\\User\\OneDrive\\Desktop\\chromedriver-win64\\chromedriver.exe'

# Set up the Chrome options
chrome_options = Options()
# Path to your specific Chrome profile (Profile 1)
chrome_profile_path = 'C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data'

# Add your Chrome profile to options
chrome_options.add_argument(f"user-data-dir={chrome_profile_path}")
chrome_options.add_argument(f"profile-directory=Profile 1")  # Specify the profile directory

# Set up the Chrome service
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the Gmail signup page
driver.get('https://accounts.google.com/signup')

# Create a Faker instance
fake = Faker()

# Generate a random first and last name
first_name = fake.first_name()
last_name = fake.last_name()

# Fill the first name and last name fields using Selenium
time.sleep(1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys(first_name)
time.sleep(1)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "lastName"))).send_keys(last_name)

# Locate and click the "Next" button
time.sleep(0.5)
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/..")))
time.sleep(1.2)
next_button.click()

# Wait for the input fields to load
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="month"]')))

# Locate the month input box and randomly choose a month
month_input = driver.find_element(By.XPATH, '//*[@id="month"]')
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
random_month = random.choice(months)
time.sleep(1)
month_input.send_keys(random_month)

# Locate the day input box and enter a randomly chosen day
day_input = driver.find_element(By.XPATH, '//*[@id="day"]')
random_day = random.randint(1, 28)
time.sleep(1)
day_input.send_keys(str(random_day))

# Locate the year input box and enter a random year
year_input = driver.find_element(By.XPATH, '//*[@id="year"]')
random_year = random.randint(1980, 2003)
time.sleep(1)
year_input.send_keys(str(random_year))

# Locate the gender input field and randomly select a gender
gender_input = driver.find_element(By.XPATH, '//*[@id="gender"]')
list_of_genders = ["Male", "Female"]
random_gender = random.choice(list_of_genders)
time.sleep(1)
gender_input.send_keys(random_gender)

# Locate and click the "Next" button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/..")))
time.sleep(1)
next_button.click()

# Click on "Create your own Gmail address"
create_own_gmail_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div[1]/div[1]/div/span/div[1]/div/div[3]/div/div[3]/div')))
time.sleep(1)
create_own_gmail_button.click()

# Locate and click the "Next" button
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/..")))
next_button.click()
time.sleep(2)

# Wait for the Gmail address input box to load
gmail_input_box_xpath = '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input'
gmail_input_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, gmail_input_box_xpath)))

# Clear the input box before entering the new Gmail address
gmail_input_box.clear()

# Generate the Gmail address with four random digits
random_digits = random.randint(1000, 9999)  # Four random digits
gmail_address = f"{first_name}{last_name}{random_digits}"
time.sleep(1)
gmail_input_box.send_keys(gmail_address)

# Locate and click the "Next" button again
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/..")))
time.sleep(1)
next_button.click()

# Generate Random Password
password = f"Letmein.123"

# Wait for the password fields to appear
password_input_xpath = '//*[@id="passwd"]/div[1]/div/div[1]/input'
confirm_password_input_xpath = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/input'

password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, password_input_xpath)))
confirm_password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, confirm_password_input_xpath)))

# Enter the password into both fields
password_input.send_keys(password)
time.sleep(1)
confirm_password_input.send_keys(password)

# Locate and click the "Next" button again
next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Next']/..")))
time.sleep(1)
next_button.click()

# Print the generated credentials
print("The browser will remain open until you manually close it. Press Enter in the console to exit the script...")
print(f"Gmail Address: {gmail_address}")
print(f"Password: {password}")

# The script will pause here until you press Enter
input("Press Enter to exit the script (browser will still remain open).")
