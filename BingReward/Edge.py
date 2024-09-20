import webbrowser
import time
from datetime import datetime

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# List of websites to open
websites = [
    f"https://www.bing.com/search?q=bing+search+is+not+working+{today_date}+&qs=LT&pq=bing+search+is+not+&sc=10-19&cvid=65B28A3E29E843B99717D7DC914D28E2&FORM=QBLH&sp=1&ghc=1&lq=0",
    # Add more websites here
]

# Path to Edge executable
edge_path = 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'

# Register Edge browser
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

# Open each website with a 10-second gap
for website in websites:
    webbrowser.get('edge').open(website)
    time.sleep(10)




'''
Write a python script for below requirements
1. It should open edge browse
2. It should open list of websites
3. there should be 10 second gaps in between opening of 2 websites
4. Do not use selenium, use simple "import webbrowser"
5. Use a sample website remaining i will add my self
6. sample website: https://www.bing.com/search?q=bing+search+is+not+working&qs=LT&pq=bing+search+is+not+&sc=10-19&cvid=65B28A3E29E843B99717D7DC914D28E2&FORM=QBLH&sp=1&ghc=1&lq=0

'''
