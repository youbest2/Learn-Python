import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException

# Set up Edge options to simulate a mobile device and ignore SSL errors
mobile_emulation = {
    "deviceMetrics": {"width": 360, "height": 640, "pixelRatio": 3.0},
    "userAgent": ("Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36")
}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# Path to the EdgeDriver
edge_service = Service('D:/Extra/Software_Local/Chrome/edgedriver_win32/msedgedriver.exe')

# Initialize the WebDriver
driver = webdriver.Edge(service=edge_service, options=options)

try:
    print("Starting the script...")

    # Navigate to Bing.com
    print("Navigating to Bing.com...")
    driver.get("https://www.bing.com/")
    
    # Record clicked links and activity
    clicked_links = []
    
    while True:
        print("Finding all links on the page...")
        links = driver.find_elements(By.XPATH, "//a[@href]")
        
        for link in links:
            try:
                href = link.get_attribute('href')
                if href not in clicked_links:
                    print(f"Attempting to click link: {href}")
                    if link.is_displayed() and link.is_enabled():
                        link.click()
                        clicked_links.append(href)
                        print(f"Clicked link: {href}")
                        time.sleep(2)  # Wait for 2 seconds before clicking the next link
                        
                        # Check if the landing page loaded successfully
                        if driver.current_url != href:
                            print(f"Failed to land on: {href}")
            except (NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException) as e:
                print(f"Exception occurred while clicking link: {href}")
                print(f"Exception details: {e.__class__.__name__}, {e.args}")
                continue
            except StaleElementReferenceException:
                print(f"Stale element reference for link: {href}. Retrying...")
                continue

except Exception as e:
    print(f"An error occurred: {e}")
    print("Exception details:", e.__class__.__name__, e.args)

finally:
    print("The browser will remain open. Close it manually when done.")
    while True:
        time.sleep(1)  # Keep the script running to keep the browser open
