import webbrowser
import time
from datetime import datetime

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# List of websites to open
websites = [
    f"https://www.bing.com/search?q=bing+search+is+not+working+{today_date}+&&sc=9-30&qs=n&sk=&cvid=BB2D03938855403A86DB94B81D261F71&FORM=QBRE&qs=RS&sc=3-38&sp=8&lq=0",
    # Add more websites here
]

# Path to Chrome executable
chrome_path = 'D:/Extra/Software_Local/Chrome/GoogleChromePortable/GoogleChromePortable.exe'

# Register Chrome browser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))

# Open each website with a 10-second gap
for website in websites:
    webbrowser.get('chrome').open(website)
    time.sleep(10)
