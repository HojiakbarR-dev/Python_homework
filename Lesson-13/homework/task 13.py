# %% [markdown]
# ### Import datetime

# %%
###1. Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.

from datetime import date
from calendar import monthrange

def calculate_age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Fix negative days
    if days < 0:
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month != 1 else today.year - 1
        days_in_prev_month = monthrange(prev_year, prev_month)[1]
        days += days_in_prev_month
        months -= 1

    # Fix negative months
    if months < 0:
        months += 12
        years -= 1

    return years, months, days


# -----------------------------
# Ask user for input
# -----------------------------
year = int(input("Year (YYYY): "))
month = int(input("Month (1-12): "))
day = int(input("Day (1-31): "))

birth_date = date(year, month, day)
years, months, days = calculate_age(birth_date)

print(f"\nYour age is: {years} years, {months} months, {days} days.")



# %%
# 2. Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.

from datetime import date, timedelta

def days_until_next_birthday(birth_date):
    today = date.today()
    this_year_bday = date(today.year, birth_date.month, birth_date.day)
    if this_year_bday < today:
        next_bday = date(today.year + 1, birth_date.month, birth_date.day)
    else:
        next_bday = this_year_bday
    return (next_bday - today).days

# Example:
# print(days_until_next_birthday(date(1995, 12, 25)))


# %%
#3 Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.

from datetime import datetime, timedelta

print("Enter the current date and time")
date_str = input("Format YYYY-MM-DD HH:MM → ")

# parse input
start_time = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

print("\nEnter meeting duration:")
hours = int(input("Hours: "))
minutes = int(input("Minutes: "))

# calculate end time
duration = timedelta(hours=hours, minutes=minutes)
end_time = start_time + duration

# output
print("\nThe meeting will end at:", end_time.strftime("%Y-%m-%d %H:%M"))


# %%
from datetime import datetime
from zoneinfo import ZoneInfo

print("Enter a date and time")
dt_str = input("Format YYYY-MM-DD HH:MM → ")

# parse datetime
dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")

print("\nExample timezones: Europe/Rome, Asia/Tashkent, America/New_York, UTC")
from_tz = input("Enter your current timezone: ")
to_tz = input("Enter the timezone you want to convert to: ")

# attach original timezone
dt_with_tz = dt.replace(tzinfo=ZoneInfo(from_tz))

# convert to another timezone
converted = dt_with_tz.astimezone(ZoneInfo(to_tz))

print("\nConverted time:", converted.strftime("%Y-%m-%d %H:%M (%Z)"))


# %%
from datetime import datetime
import time

# ask the user for target datetime
print("Enter a future date and time:")
target_str = input("Format YYYY-MM-DD HH:MM:SS → ")

# convert to datetime object
target = datetime.strptime(target_str, "%Y-%m-%d %H:%M:%S")

print("\nCountdown started...\n")

while True:
    now = datetime.now()
    diff = target - now

    # if time is up
    if diff.total_seconds() <= 0:
        print("00:00:00 (Time reached!)")
        break

    # extract days, hours, minutes, seconds
    days = diff.days
    hours, remainder = divmod(diff.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # format output
    if days > 0:
        output = f"{days}d {hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        output = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    print(output, end="\r")
    time.sleep(1)


# %%
# 6. Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.

import re

# simple & practical regex for email validation
EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

email = input("Enter an email address: ")

if re.match(EMAIL_PATTERN, email):
    print("Valid email address ")
else:
    print("Invalid email address ")


# %%
# 7. Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".

import re

phone = input("Enter a phone number: ")

# remove all non-digits
digits = re.sub(r"\D", "", phone)

if len(digits) == 10:
    # standard US 10-digit format
    formatted = f"({digits[0:3]}) {digits[3:6]}-{digits[6:10]}"
    print("Formatted Number:", formatted)

elif len(digits) == 11 and digits[0] == "1":
    # US number with +1 country code
    formatted = f"+1 ({digits[1:4]}) {digits[4:7]}-{digits[7:11]}"
    print("Formatted Number:", formatted)

else:
    print("Invalid phone number length!")


# %%
import re

password = input("Enter a password: ")

# criteria
length_ok = len(password) >= 8
uppercase_ok = bool(re.search(r"[A-Z]", password))
lowercase_ok = bool(re.search(r"[a-z]", password))
digit_ok = bool(re.search(r"\d", password))

print("\nPassword Check Results:")
print("Minimum length (8 chars):", "Yes" if length_ok else "No")
print("Contains uppercase letter:", "Yes" if uppercase_ok else "No")
print("Contains lowercase letter:", "Yes" if lowercase_ok else "No")
print("Contains digit:",            "Yes" if digit_ok else "No")

# final verdict
if length_ok and uppercase_ok and lowercase_ok and digit_ok:
    print("\nPassword Strength: STRONG")
else:
    print("\nPassword Strength: WEAK")


# %%
#9. Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.

import re

# sample text (you can change it)
text = """
Python is a powerful programming language. Many people learn Python because
Python is easy to read and write. This makes Python one of the most popular
languages today.
"""

# ask user for a word
word = input("Enter a word to search: ")

# prepare regex (case-insensitive, matches whole word)
pattern = re.compile(rf"\b{re.escape(word)}\b", re.IGNORECASE)

matches = list(pattern.finditer(text))

if matches:
    print(f"\nFound {len(matches)} occurrence(s):\n")
    for m in matches:
        print(f" - Found '{m.group()}' at index {m.start()}")
else:
    print("\nNo occurrences found.")


# %%
# 10. Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.

import re

text = input("Enter your text: ")

# Regex patterns for different date formats
patterns = [
    r"\b\d{4}-\d{2}-\d{2}\b",                    # YYYY-MM-DD
    r"\b\d{2}/\d{2}/\d{4}\b",                    # DD/MM/YYYY
    r"\b\d{2}-\d{2}-\d{4}\b",                    # DD-MM-YYYY
    r"\b([A-Za-z]+)\s+\d{1,2},\s*\d{4}\b",       # Month DD, YYYY
    r"\b([A-Za-z]+)\s+\d{1,2}\s+\d{4}\b",        # Month DD YYYY
]

dates_found = []

# search using all patterns
for p in patterns:
    matches = re.findall(p, text)
    
    # some patterns return tuples (because of month name capture groups)
    for match in matches:
        if isinstance(match, tuple):
            dates_found.append(" ".join(match))
        else:
            dates_found.append(match)

# print results
if dates_found:
    print("\nDates found:")
    for d in dates_found:
        print(" -", d)
else:
    print("\nNo dates found in the text.")



