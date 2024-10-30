import webbrowser
import time
from datetime import datetime
import random

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# List of topics to search
topics = [
    "Renewable Energy Sources",
    "Cultural Anthropology",
    "Cybersecurity and Data Privacy",
    "Classical Literature",
    "Music Theory and Composition",
    "Global Political Systems",
    "Health and Nutrition",
    "Robotics and Automation",
    "Mythology and Folklore",
    "Digital Marketing and Social Media",
    "Marine Biology and Oceanography",
    "Architecture and Urban Planning",
    "Film Studies and Cinematography",
    "Astronomy and Space Missions",
    "Artificial Intelligence in Healthcare",
    "History of Technology",
    "Psychological Thrillers and Mystery Novels",
    "Travel and World Cultures",
    "Artificial Intelligence and Machine Learning",
    "Space Exploration and Astronomy",
    "History of Ancient Civilizations",
    "Climate Change and Environmental Science",
    "Quantum Physics and Mechanics",
    "World War II History",
    "Psychology and Human Behavior",
    "Modern Art and Art History",
    "Cryptocurrency and Blockchain Technology",
    "Global Economic Trends",
    "Philosophy and Ethics",
    "Genetics and Biotechnology"
]

# Path to Chrome executable
chrome_path = 'D:\Extra\Software_Local\Chrome\GoogleChromePortable\IronPortable\IronPortable.exe'

# Register Chrome browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each topic search with a 10-second gap
for topic in topics:
    search_url = f"https://www.bing.com/search?q={topic.replace(' ', '+')}+{today_date}+&form=QBLH&sp=-1&lq=0&pq={topic.replace(' ', '+')}+{today_date}+&sc=11-42&qs=n&sk=&cvid=B3A9DC74AE0B4FDDBCEA7C42AC070FA1&ghsh=0&ghacc=0&ghpl="
    
    webbrowser.get('chrome').open(search_url)
    
    # Generate a random sleep duration between 10 and 20 seconds.
    sleep_duration = random.randint(12, 15) 
    print(f"Waiting for {sleep_duration} seconds...")
    time.sleep(sleep_duration) # Pause execution for the generated sleep duration.
