print((2+3)*6/2 and 18.0)

#other question

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)

#palidrome
def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
word1 = "1414884937242655719669145562427394884141"
word2 = "6800923757255865070000705685527573290086"
word3 = "6892149109325320763773670235239019412986"
word4 = "9847255590886266818998186626880955527489"

print(palindrome(word1))
print(palindrome(word2))
print(palindrome(word3))
print(palindrome(word4))


#pattern question
def find_pattern_occurrences(text):
    count = 0  # Initialize a counter to keep track of the number of matches

    # Iterate through the text
    for i in range(len(text) - 4):  # up to the 4th character from the end
        if text[i:i + 2] == "un" and text[i + 2:].find("an") != -1:  # Check if "un" is followed by "an"
            count += 1  # Increment the counter if the pattern is found

    return count  # Return the total number of matches

import random
random_numbers = [99,44,53,23,32,3,2,1,5,6,3,66,34,33,1,17]
for i in range(10):
    random_numbers.append(random.randint(1, 100))
modified_numbers = []
for num in random_numbers:
    if num % 2 == 0:
        modified_numbers.append(num * 2)
print(modified_numbers)

#url code
def is_valid_url(url):
    # Check if the URL starts with a valid prefix
    if url.startswith("http://") or url.startswith("https://"):
        return True
    else:
        return False

# Test the function
url1 = "https://www.example.com"
url2 = "not_a_valid_url"

print(is_valid_url(url1))  # Output: True
print(is_valid_url(url2))  # Output: False

#birthday code
def days_since_birthday(birthday):
    from datetime import datetime, timedelta

    # Convert birthday string to a datetime object
    birthdate = datetime.strptime(birthday, "%d-%m-%Y")

    # Get current date
    current_date = datetime.now()

    # Calculate the difference in days
    days_passed = (current_date - birthdate).days

    return days_passed

# Test the function
birthday = "01-01-2000"
print("Days since birthday:", days_since_birthday(birthday))


