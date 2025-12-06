# %%
# 1. Task: JSON Parsing - write a Python script that reads the students.jon JSON file and prints details of each student.

import json


with open("students.json", "r") as file: # Read the JSON file
    data = json.load(file)

for student in data: # Print details of each student
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Major: {student['major']}")


# %%
# 2. Task: Weather API
#    1. Use this url : https://openweathermap.org/
#    2. Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).

# This wheather API which is given in the task is required OWM_API_KEY, so I don't have it right now, that's why I use free wheather API for this task

import requests

# Tashkent coordinates
latitude = 41.3111
longitude = 69.2797

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "current_weather": "true"
}

response = requests.get(url, params=params)

# Convert to JSON
data = response.json()

# Extract values
weather = data["current_weather"]

print("Current weather in Tashkent:")
print(f"Temperature: {weather['temperature']}°C")
print(f"Windspeed: {weather['windspeed']} km/h")
print(f"Weather Code: {weather['weathercode']}")
print(f"Time: {weather['time']}")




# %%
# 3. Task: JSON Modification
#    1. Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.

import json

# Load JSON file
def load_books():
    with open("books.json", "r") as f:
        return json.load(f)

# Save JSON file
def save_books(books):
    with open("books.json", "w") as f:
        json.dump(books, f, indent=4)


# 1. ADD BOOK
def add_book():
    books = load_books()
    new_id = books[-1]["id"] + 1 if books else 1

    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }

    books.append(new_book)
    save_books(books)
    print("Book added successfully!\n")


# 2. UPDATE BOOK
def update_book():
    books = load_books()
    book_id = int(input("Enter book ID to update: "))

    for book in books:
        if book["id"] == book_id:
            book["title"] = input("New title: ")
            book["author"] = input("New author: ")
            book["year"] = input("New year: ")
            save_books(books)
            print("Book updated!\n")
            return

    print("Book not found!\n")


# 3. DELETE BOOK
def delete_book():
    books = load_books()
    book_id = int(input("Enter book ID to delete: "))

    books = [b for b in books if b["id"] != book_id]
    save_books(books)
    print("Book deleted!\n")


# SIMPLE MENU
while True:
    print("1. Add Book")
    print("2. Update Book")
    print("3. Delete Book")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        update_book()
    elif choice == "3":
        delete_book()
    elif choice == "4":
        break
    else:
        print("Invalid choice!\n")




# %%
#!/usr/bin/env python3
"""
movie_recommender_freeapi.py

- Picks a random movie title from a local genre list
- Fetches details (if available) from the free FM-DB API:
  https://imdb.iamidiotareyoutoo.com/search?q=...
No API key required.
"""

import requests
import random
import urllib.parse

# Local small genre->titles map (extend as you like)
LOCAL_GENRE_DB = {
    "action": ["Die Hard", "Mad Max: Fury Road", "John Wick", "The Dark Knight"],
    "comedy": ["Superbad", "Groundhog Day", "The Big Lebowski", "Monty Python and the Holy Grail"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "Fight Club", "Parasite"],
    "sci-fi": ["Inception", "The Matrix", "Blade Runner 2049", "Interstellar"],
    "horror": ["The Exorcist", "Get Out", "Hereditary", "A Nightmare on Elm Street"],
    "romance": ["Casablanca", "Before Sunrise", "Lost in Translation", "La La Land"]
}

FMDB_SEARCH_BASE = "https://imdb.iamidiotareyoutoo.com/search"

def fetch_movie_from_fmdb(title):
    """
    Query the FM-DB search endpoint.
    Returns JSON (parsed) or None on failure.
    Example endpoint: https://imdb.iamidiotareyoutoo.com/search?q=Inception
    """
    try:
        params = {"q": title}
        # Build URL (requests will encode params)
        r = requests.get(FMDB_SEARCH_BASE, params=params, timeout=8)
        r.raise_for_status()
        # API returns JSON — try to parse
        data = r.json()
        return data
    except requests.RequestException as e:
        print("Network/API error when contacting FM-DB:", e)
        return None
    except ValueError:
        # failed to parse JSON
        print("Received non-JSON response from FM-DB.")
        return None

def pretty_print_fmdb_search(data):
    """
    Attempt to print useful info from FM-DB response.
    The exact structure may vary depending on the service.
    """
    if not data:
        print("No data from FM-DB.")
        return

    # Inspect possible keys
    # Common pattern: a top-level 'results' or list
    if isinstance(data, dict):
        # try to find keys we can use
        if "results" in data and isinstance(data["results"], list):
            results = data["results"]
        elif isinstance(data.get("data"), list):
            results = data.get("data")
        else:
            # fallback: if dict looks like a single movie, print fields
            # Try some common keys
            title = data.get("title") or data.get("Title") or data.get("name")
            year = data.get("year") or data.get("Year")
            imdb_id = data.get("imdb_id") or data.get("imdbID") or data.get("id")
            plot = data.get("plot") or data.get("Plot") or data.get("description")
            print("Title:", title)
            if year: print("Year:", year)
            if imdb_id: print("IMDB ID:", imdb_id)
            if plot: print("Plot:", plot)
            return
    elif isinstance(data, list):
        results = data
    else:
        print("Unrecognized FM-DB response structure.")
        return

    if not results:
        print("No results found in FM-DB response.")
        return

    # Print first result as the most relevant
    first = results[0]
    # attempt to print fields that might be present
    title = first.get("title") or first.get("Title") or first.get("name")
    year = first.get("year") or first.get("Year") or first.get("release_year")
    imdb_id = first.get("imdb_id") or first.get("imdbID") or first.get("id") or first.get("tt")
    plot = first.get("plot") or first.get("Plot") or first.get("overview") or first.get("description")
    print("\n--- FM-DB Result (first match) ---")
    if title: print("Title :", title)
    if year:  print("Year  :", year)
    if imdb_id: print("IMDB ID:", imdb_id)
    if plot: print("Plot  :", (plot[:400] + '...') if len(str(plot))>400 else plot)
    # try to print poster/url if exists
    poster = first.get("poster") or first.get("image") or first.get("Poster")
    if poster and poster != "N/A":
        print("Poster :", poster)
    print("---------------------------------\n")

def main():
    print("Available genres:", ", ".join(sorted(LOCAL_GENRE_DB.keys())))
    genre = input("Enter a genre (e.g. action, comedy, drama): ").strip().lower()
    if genre not in LOCAL_GENRE_DB:
        print("Genre not found in local list. Try one of:", ", ".join(sorted(LOCAL_GENRE_DB.keys())))
        return

    choice = random.choice(LOCAL_GENRE_DB[genre])
    print(f"\nI recommend: {choice}  (from local list)")

    # Fetch details from FM-DB (no key required)
    print("Looking up additional details online (no API key required)...")
    data = fetch_movie_from_fmdb(choice)
    if data:
        pretty_print_fmdb_search(data)
    else:
        print("Could not fetch online details — showing local recommendation only.")

if __name__ == "__main__":
    main()



