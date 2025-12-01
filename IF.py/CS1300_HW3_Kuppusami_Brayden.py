"""
CS1300 Homework 3: String Manipulation
Name: Brayden Kuppusami
Date: 11/29/2025
Description: Programs that work with text and string operations
"""

print("PROBLEM 1: Business Card Generator")
print("=" * 40) 



print("=== Business Card Generator ===") 

name = input("Enter your full name: ") 
title = input("Enter your job title: ") 
email = input("Enter your email: ") 
phone = input("Enter your phone number: ") 


border = "*" * 40 
width = 40 


print(border)


print("*".ljust(1) + " " * (width - 2) + "*".rjust(1))


name_line = name.upper().center(width - 2)
print(f"*{name_line}*")


print("*".ljust(1) + " " * (width - 2) + "*".rjust(1))


title_line = title.center(width - 2)
print(f"*{title_line}*")


print("*".ljust(1) + " " * (width - 2) + "*".rjust(1))


email_text = f"Email: {email}"

email_line = email_text.ljust(width - 2) 
print(f"*{email_line}*")


phone_text = f"Phone: {phone}"
phone_line = phone_text.ljust(width - 2)
print(f"*{phone_line}*")


print("*".ljust(1) + " " * (width - 2) + "*".rjust(1))


print(border)


print("\nPROBLEM 2: Username Creator")
print("=" * 40) 



print("=== Username Generator ===") 

first_name = input("Enter your first name: ") 
last_name = input("Enter your last name: ") 


fn_lower = first_name.lower()
ln_lower = last_name.lower()
ln_length = len(last_name) 


option1 = fn_lower[0:3] + ln_lower[0:3]


option2 = fn_lower[0] + ln_lower


option3 = fn_lower + ln_lower[0] + str(ln_length)

print("\nYour username options:") 

print(f"1. {option1}")
print(f"2. {option2}")
print(f"3. {option3}")



print("\nPROBLEM 3: Text Message Formatter")
print("=" * 40) 


print("=== Text Message Formatter ===") 

message = input("Enter your message: ") 


length = len(message) 


print(f"\nOriginal: {message}") 
print(f"Length: {length} characters") 


shouting = message.upper()
print(f"SHOUTING: {shouting}")


whispering = message.lower()
print(f"whispering: {whispering}")


snake_case = message.replace(" ", "_")
print(f"Snake_case: {snake_case}")


first_half = message[0:length//2]
print(f"First half: {first_half}")


last_half = message[length//2:]
print(f"Last half: {last_half}")


reversed_message = message[::-1]
print(f"Reversed: {reversed_message}")



print("\nPROBLEM 4: Password Masker and Validator")
print("=" * 40) 



print("=== Password Validator ===") 

password = input("Create a password: ") 


length = len(password) 
has_minimum_length = length >= 8 


has_uppercase = password != password.lower() 

has_lowercase = password != password.upper() 

print("\nPassword Analysis:") 


if length >= 2:
    
    first_char = password[0]
    
    last_char = password[-1]
    
    middle_mask = "*" * (length - 2)
    masked_version = first_char + middle_mask + last_char
elif length == 1:
    masked_version = password[0] 
else: 
    masked_version = "" 


met_count = int(has_minimum_length) + int(has_uppercase) + int(has_lowercase)
total_requirements = 3


if met_count == total_requirements:
    strength = "STRONG"
elif met_count >= total_requirements // 2: 
    strength = "MODERATE"
else:
    strength = "WEAK"



length_check = "✓" if has_minimum_length else "x"
print(f"Length: {length} characters {length_check}") 


uppercase_status = "Yes" if has_uppercase else "No"
uppercase_check = "✓" if has_uppercase else "x"
print(f"Has uppercase: {uppercase_status} {uppercase_check}") 


lowercase_status = "Yes" if has_lowercase else "No"
lowercase_check = "✓" if has_lowercase else "x"
print(f"Has lowercase: {lowercase_status} {lowercase_check}") 


print(f"Masked version: {masked_version}") 


print(f"Password Strength: {strength} ({met_count}/{total_requirements} requirements met)") 



print("\nPROBLEM 5: Story Mad Libs (Bonus)")
print("=" * 40) 



print("=== Mad Libs Story Generator ===") 
print("I need some words to create your story!\n") 


name = input("Enter a name: ") 
place = input("Enter a place: ") 
animal = input("Enter an animal: ") 
food = input("Enter a type of food: ") 
adjective1 = input("Enter an adjective (describing word): ") 
adjective2 = input("Enter another adjective: ") 
verb1 = input("Enter a verb ending in -ing: ") 
verb2 = input("Enter another verb ending in -ing: ") 
number = input("Enter a number: ")
color = input("Enter a color: ")


name_upper = name.upper() 
place_upper = place.upper() 
animal_upper = animal.upper()
food_upper = food.upper()
adjective1_upper = adjective1.upper()
adjective2_upper = adjective2.upper()
verb1_upper = verb1.upper() 
verb2_upper = verb2.upper()
number_upper = number.upper()
color_upper = color.upper()



story = f"""
Once upon a time, {name_upper} was {verb1_upper} through {place_upper}
when they discovered a {adjective1_upper} {animal_upper}.
The {animal_upper} was eating {number_upper} pieces of {food_upper}
and wearing a {color_upper} hat.
"How {adjective2_upper}!" exclaimed {name_upper}.
They spent the rest of the day {verb2_upper} together.
THE END
"""

word_count = len(story.split()) 


print("\n" + "="*50) 
print("YOUR STORY") 
print("="*50) 
print(story) 


print(f"\nYour story has {word_count} words!") 