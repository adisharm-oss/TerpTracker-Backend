# TerpTracker 🥗

TerpTracker is a Python-based command-line tool that helps UMD students access accurate calorie and protein information from campus dining halls by scraping data directly from UMD’s nutrition website.

## Features
- Fetches dining hall menus for a user-selected date  
- Lists available food items interactively  
- Searches for specific foods using partial, case-insensitive matching  
- Extracts calorie and protein values for selected items  

## How to Run

### Requirements
- Python 3.x  
- requests  
- beautifulsoup4  

Install dependencies:
```bash
pip install requests beautifulsoup4
```

Run the program:
```bash
python terptracker.py
```

## How It Works (Program Flow)

1. Displays a welcome message  
2. Prompts the user for a date (MM/DD/YYYY)  
3. Builds the corresponding UMD dining menu URL  
4. Fetches and parses the menu page  
5. Lists all available food items  
6. Prompts the user to search for a food  
7. Matches the input against menu items (case-insensitive)  
8. Follows the nutrition link for the selected item  
9. Extracts and displays calorie and protein values  

## Motivation
UMD dining hall nutrition data isn’t always easy to access before eating. TerpTracker lowers this barrier by turning scattered web data into a simple, interactive workflow that helps students make more informed nutrition decisions.
