import requests
from bs4 import BeautifulSoup

# asks user for the date
print("Welcome to TerpTracker!")
print("-" * 50)
user_date = input("What's today's date? (MM/DD/YYYY): ")

# builds the menu URL using the user's date
menu_url = f"https://nutrition.umd.edu/?locationNum=19&dtdate={user_date}"
print(f"\nFetching menu for {user_date}...")

response = requests.get(menu_url)
soup = BeautifulSoup(response.text, 'html.parser')

# creates a list of all food items
food_links = soup.find_all('a', class_='menu-item-name')

# shows the user all available food items for that day
print(f"\nAvailable foods on {user_date}:")
print("-" * 50)
for i, link in enumerate(food_links):
    print(f"{i + 1}. {link.text.strip()}")
print("-" * 50)

# asks the user to type the desired food name
user_input = input("\nType the name of the food you want (or part of it): ")

# searchs for matching foods
found_food = None
for link in food_links:
    food_name = link.text.strip()
    # checks if what the user typed is anywhere in the food name (case doesn't matter)
    if user_input.lower() in food_name.lower():
        found_food = link
        print(f"\nFound: {food_name}")
        break

# if a match is found, get the calorie and protein values
if found_food:
    food_href = found_food.get('href')
    
    # builds the full URL for the nutrition page
    nutrition_url = "https://nutrition.umd.edu/" + food_href
    
    # fetchs the nutrition page
    nutrition_response = requests.get(nutrition_url)
    nutrition_soup = BeautifulSoup(nutrition_response.text, 'html.parser')
    
    # finds the calories using p tags, then strips the number
    p_tags = nutrition_soup.find_all('p')
    for p in p_tags:
        if p.text.strip().isdigit():
            calories = p.text.strip()
            print(f"Calories: {calories}")
            break
    
    # finds protein using nutrition spans, then looking for the one with keyword "Protein", then extracts just the value
    nutrient_spans = nutrition_soup.find_all('span', class_='nutfactstopnutrient')
    for span in nutrient_spans:
        if 'Protein' in span.text:
            protein_text = span.text.split()[-1]
            print(f"Protein: {protein_text}")
            break
else:
    # if food requested is not found, gives an error message.
    print(f"\nSorry, couldn't find anything matching '{user_input}'")
    print("Try typing just part of the name, like 'egg' or 'bacon'")