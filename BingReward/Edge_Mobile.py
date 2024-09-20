import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# List of topics to search
topics = [
    "Artificial Intelligence and Machine Learning",
    "Space Exploration and Astronomy",
    "History of Ancient Civilizations",
    "Climate Change and Environmental Science",
    "Quantum Physics and Mechanics",
    "Travel and World Cultures"
]

# Set up Chrome options to simulate a mobile device and ignore SSL errors
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": ("Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36")
}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.binary_location = 'D:/Extra/Software_Local/Chrome/chrome-win32/chrome.exe'  # Path to Chrome binary

# Path to the ChromeDriver
chrome_service = Service('D:/Extra/Software_Local/Chrome/chromedriver-win32/chromedriver.exe')

# Initialize the WebDriver
driver = webdriver.Chrome(service=chrome_service, options=options)

try:
    print("Starting the script...")

    # Log in to Microsoft Live
    print("Navigating to Microsoft Live login page...")
    driver.get("https://login.live.com/")
    
    print("Waiting for email input field...")
    email_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "loginfmt"))
    )
    print("Email input field found. Entering email...")
    email_input.send_keys("youbest2@hotmail.com")
    email_input.send_keys(Keys.RETURN)
    
    print("Waiting for password input field...")
    password_input = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.NAME, "passwd"))
    )
    print("Password input field found. Entering password...")
    password_input.send_keys("TEZUS@Pal22")
    password_input.send_keys(Keys.RETURN)
    
    # Wait for 2FA input (e.g., code entry)
    print("Waiting for 2FA process to complete...")
    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.NAME, "DontAskAgain"))
    )
    print("2FA process completed. Ticking 'Don't ask again on this computer' checkbox...")
    
    # Tick the "Don't ask again on this computer" checkbox
    dont_ask_checkbox = driver.find_element(By.NAME, "DontAskAgain")
    dont_ask_checkbox.click()
    
    print("Submitting the 2FA form...")
    # Submit the 2FA form if needed
    submit_button = driver.find_element(By.ID, "idSIButton9")
    submit_button.click()
    
    # Wait for the URL to change after 2FA
    print("Waiting for the URL to change after 2FA...")
    WebDriverWait(driver, 120).until(
        EC.url_contains("https://account.microsoft.com/")
    )
    print("URL changed successfully. 2FA completed.")
    
    # Perform searches for each topic
    for topic in topics:
        search_url = f"https://www.bing.com/search?q={topic.replace(' ', '+')}"
        print(f"Opening a new tab for search URL: {search_url}")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(search_url)
        print(f"Searching for: {topic}")
        time.sleep(10)  # Wait for 10 seconds before the next search

        # Check if the search is performed as mobile or desktop
        user_agent = driver.execute_script("return navigator.userAgent;")
        if "Mobile" in user_agent:
            print("Search performed as mobile.")
        else:
            print("Search performed as desktop.")

except TimeoutException as e:
    print(f"TimeoutException occurred: {e}")
    print("Exception details:", e.__class__.__name__, e.args)
except Exception as e:
    print(f"An error occurred: {e}")
    print("Exception details:", e.__class__.__name__, e.args)

finally:
    print("Closing the browser...")
    driver.quit()
    print("Script finished.")
