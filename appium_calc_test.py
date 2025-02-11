from appium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import AppiumOptions

# Desired capabilities for the Google app
desired_cap = {
    "appium:automationName": "UiAutomator2",
    "appium:platformName": "Android",
    "appium:platformVersion": "15",  
    "appium:deviceName": "1cd698977d77", 
    "appium:app": "C:\APKs\com.miui.calculator.apk", 
    "appium:noReset": True 
}

appium_options = AppiumOptions()
appium_options.load_capabilities(desired_cap)

try:
    # Connect to the Appium server
    driver = webdriver.Remote("http://127.0.0.1:4723", options=appium_options)
    print(f"Connected to Appium server with session ID: {driver.session_id}")

    wait = WebDriverWait(driver, 20)

    # Wait for the search bar to be present and click it
    converter_button = wait.until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Converter"]')))
    converter_button.click()


    print("Test passed: Clicked 'Converter Button' Successfully")

except WebDriverException as e:
    print(f"Error connecting to Appium server: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    if 'driver' in locals():
        driver.quit()