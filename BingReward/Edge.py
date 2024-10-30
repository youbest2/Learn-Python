import webbrowser
import time
from datetime import datetime
import urllib.parse

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# List of topics to search
topics = [
    "History of Technology",
    "Psychological Thrillers and Mystery Novels",
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
    "Genetics and Biotechnology",
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
    "Travel and World Cultures"
]

# Path to Chrome executable
chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Register Chrome browser
webbrowser.register('Edge', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each topic search with a 10-second gap
for topic in topics:
    search_url = f"https://www.bing.com/search?q={topic.replace(' ', '+')}+{today_date}&form=STARH1&refig=61aecd7031604bed8cc8985e756471a3&mkt=en-in&ocid=&pc=&pq={topic.replace(' ', '+')}+{today_date}&qs=AS&smvpcn=0&swbcn=10&sc=10-8&sp=1&ghc=0&cvid=61aecd7031604bed8cc8985e756471a3&clckatsg=1&hsmssg=0"
    
    #search_url = f"https://www.bing.com/search?q={urllib.parse.quote(topic)}&form=hpmscl"
    
    webbrowser.get('Edge').open(search_url)
    time.sleep(10)
