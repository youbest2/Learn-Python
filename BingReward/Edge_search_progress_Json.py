import webbrowser # Import the webbrowser module to interact with web browsers.
import time # Import the time module to use sleep function for pausing execution.
from datetime import datetime # Import datetime to get the current date.
import urllib.parse # Import urllib.parse to encode URLs correctly.
import json # Import json to work with JSON data for storing progress.
import random # Import random to generate random sleep durations.

# Settings
searches_per_run = 4 # Define how many searches to perform in each run of the script.
data_file = 'search_progress.json' # Name of the JSON file to store and retrieve search progress.

# Get today's date
today_date = datetime.now().strftime("%Y-%m-%d") # Get the current date in YYYY-MM-DD format.

# List of topics to search
topics = [ 
    # List of search terms for Bing searches.
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

# Path to the Edge browser executable 
chrome_path = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe' 

# Register the Edge browser with the webbrowser module
webbrowser.register('Edge', None, webbrowser.BackgroundBrowser(chrome_path)) 

def load_progress():
    """Loads the last performed search index from the data file."""
    try:
        # Attempt to open the data file in read mode ('r').
        with open(data_file, 'r') as f: 
            # If the file is found, load and return the JSON data as a dictionary.
            return json.load(f) 
    except FileNotFoundError:
        # If the data file is not found (first-time run),
        # return a dictionary indicating the starting index as -1 (beginning of the list).
        return {'last_index': -1}

def save_progress(last_index):
    """Saves the index of the last performed search to the data file."""
    # Open the data file in write mode ('w'), creating it if it doesn't exist,
    # and overwriting its contents if it does.
    with open(data_file, 'w') as f: 
        # Store the 'last_index' in a dictionary and write it to the data file as JSON.
        json.dump({'last_index': last_index}, f) 

def perform_searches(start_index, end_index):
    """Performs Bing searches for a specified range of topics."""
    searches_performed = 0 # Initialize a counter to keep track of the number of searches performed.

    # Iterate through the topics list, starting from the provided start_index and going up to (but not including) the end_index.
    for i in range(start_index, end_index): 
        # If the current index (i) goes beyond the bounds of the 'topics' list, break the loop.
        if i >= len(topics): 
            break

        topic = topics[i] # Get the search topic based on the current index.

        # Construct the Bing search URL using the current topic and today's date.
        search_url = f"https://www.bing.com/search?q={topic.replace(' ', '+')}+{today_date}&form=STARH1&refig=61aecd7031604bed8cc8985e756471a3&mkt=en-in&ocid=&pc=&pq={topic.replace(' ', '+')}+{today_date}&qs=AS&smvpcn=0&swbcn=10&sc=10-8&sp=1&ghc=0&cvid=61aecd7031604bed8cc8985e756471a3&clckatsg=1&hsmssg=0"

        # Open the constructed search URL in the registered Edge browser.
        webbrowser.get('Edge').open(search_url) 

        # Generate a random sleep duration between 10 and 20 seconds.
        sleep_duration = random.randint(10, 20) 
        print(f"Waiting for {sleep_duration} seconds...")
        time.sleep(sleep_duration) # Pause execution for the generated sleep duration.

        searches_performed += 1 # Increment the searches_performed counter after each successful search.

        # If 4 searches have been completed, print an exit message and break the loop.
        if searches_performed >= searches_per_run: 
            print("4 searches completed. Exiting...")
            break 

# Main execution block (this code runs only when the script is executed directly).
if __name__ == '__main__': 
    progress = load_progress() # Load the last performed search index from the JSON data file.
    start_index = progress['last_index'] + 1 # Determine the starting index for the current run by adding 1 to the last performed search index.
    end_index = start_index + searches_per_run # Calculate the ending index for the current run.

    perform_searches(start_index, end_index) # Execute the searches, passing the calculated start and end indexes.
    save_progress(end_index - 1)  # Save the index of the last performed search to the JSON data file for the next run.