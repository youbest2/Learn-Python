import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# List of topics to search
topics = [
    "Climate Change and Environmental Sustainability",
    "Quantum Computing",
    "Space Exploration and Astronomy",
    "Renewable Energy Technologies",
    "Global Health and Pandemics",
    "Cryptocurrencies and Blockchain",
    "Psychology and Human Behavior",
    "History of Ancient Civilizations",
    "Modern Art and Design",
    "Genetic Engineering and Biotechnology",
    "Cybersecurity and Data Privacy",
    "Philosophy and Ethics",
    "Economics and Global Markets",
    "Robotics and Automation",
    "Cultural Anthropology",
    "Virtual Reality and Augmented Reality",
    "Education and E-Learning",
    "Political Science and International Relations",
    "Neuroscience and Brain Research",
    "Literature and Literary Criticism",
    "Sustainable Agriculture and Food Security",
    "Urban Development and Smart Cities",
    "Music Theory and History",
    "Sports Science and Medicine",
    "Fashion and Textile Design",
    "Marine Biology and Oceanography",
    "Artificial Intelligence in Healthcare",
    "Social Media and Digital Communication",
    "Ethnobotany and Traditional Medicine",
    "Film Studies and Cinematography"
]

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
    
    # Wait for 1 minute (60 seconds) before starting the search
    time.sleep(60)

    # Perform searches for each topic
    for topic in topics:
        search_url = f"https://www.bing.com/search?q={topic.replace(' ', '+')}+{today_date}+&form=QBLH&sp=-1&ghc=1&lq=0&pq={topic.replace(' ', '+')}+{today_date}+&&sc=10-11&qs=n&sk=&cvid=78E2A1E05FBF43AF90D3489912B8CA0C&ghsh=0&ghacc=0&ghpl="
        print(f"Opening a new tab for search URL: {search_url}")
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(search_url)
        print(f"Searching for: {topic}")
        print(f"Search URL: {driver.current_url}")
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
    print("The browser will remain open. Close it manually when done.")
    while True:
        time.sleep(1)  # Keep the script running to keep the browser open
