from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import pandas as pd
import time
import os

# Read account and password
load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# Read your matirx
matrix = pd.read_csv('Matrix.csv', index_col=0)

driver = webdriver.Chrome()
driver.get('https://portal.titech.ac.jp/')

# Step 1: Click '同意 (マトリクス...)'
driver.find_element(By.XPATH, "//input[contains(@value, 'マトリクス')]").click()

# Step 2: Input account and password
driver.implicitly_wait(10)
driver.find_element(By.NAME, "usr_name").send_keys(username)
driver.find_element(By.NAME, "usr_password").send_keys(password)
driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value, 'OK')]").click()

# Step 3: Matrix validation
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Matrix Authentication')]"))
)

labels = driver.find_elements(By.XPATH, "//th[contains(text(),'[') and contains(text(),']')]")
for label in labels:
    coord = label.text.strip("[]").split(',')
    col, row = coord[0], coord[1]
    code = matrix.loc[int(row), col]
    input_box = label.find_element(By.XPATH, "./following-sibling::td//input[@type='password']")
    input_box.clear()
    input_box.send_keys(code)

driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value, 'OK')]").click()

# Step 4: Login successfully
print("Login complete. You may now use the Portal.")

try:
    while len(driver.window_handles) > 0:
        time.sleep(3)
except:
    pass

print("Browser closed. Program exiting.")
driver.quit()
