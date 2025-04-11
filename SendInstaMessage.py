from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def SendMessage(username, password, recipient_username, message):
    # Set up Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Open Instagram
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        
        # Login
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = driver.find_element(By.NAME, "password")
        
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete
        
        # Dismiss save login info prompt if it appears
        try:
            not_now_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now_btn.click()
            time.sleep(2)
        except:
            pass
        
        # Dismiss notifications prompt if it appears
        try:
            not_now_btn = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]"))
            )
            not_now_btn.click()
            time.sleep(2)
        except:
            pass
        
        # Go to recipient's profile
        driver.get(f"https://www.instagram.com/{recipient_username}/")
        time.sleep(3)
        
        # Click message button
        message_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Message')]"))
        )
        message_button.click()
        time.sleep(3)
        
        # Type and send message
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@role='textbox']"))
        )
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
        time.sleep(2)
        
        print(f"Message sent to {recipient_username} successfully!")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()







SendMessage(Username, Password, Recipient, Message)