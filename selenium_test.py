from selenium import webdriver
import time
import mysql.connector
from selenium.webdriver.common.by import By


#driver = webdriver.Safari()  # Ensure Safaridriver/Chrome Driver installed
driver = webdriver.Chrome()
time.sleep(5)
driver.get('http://localhost:5000/login')

# Interact with the login form
username = driver.find_element(By.NAME, 'username')
password = driver.find_element(By.NAME, 'password')

username.send_keys('test_user')
password.send_keys('user')
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
driver.quit()

# Verify user data in the database
# Update the connection as per your own details
db = mysql.connector.connect(user='root', password='*****', host='localhost', database='testing')
cursor = db.cursor()
cursor.execute("SELECT * FROM users WHERE username = 'test_user'")
user_data = cursor.fetchone()
print(user_data)

assert user_data[1] == 'test_user'  # Verify the username in the database matches
db.close()
#driver.quit()

print("Test passed: User data is correct.")

