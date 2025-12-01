"""
CS1300 Homework 4: Decision Structures I
Name: [Your Name]
Date: [Submission Date]
Description: Programs using conditional statements for decision-making
"""


print("PROBLEM 1: Temperature Converter & Advisor")
print("=" * 40)


print("=== Temperature Converter & Weather Advisor ===")

temp = float(input("Enter temperature: "))

scale = input("Is this Celsius or Fahrenheit? (C/F): ").upper()


celsius = 0.0
fahrenheit = 0.0


if scale == 'C':
    celsius = temp
    
    fahrenheit = (temp * 9/5) + 32
    converted_scale = fahrenheit
    converted_unit = 'F'
elif scale == 'F':
    fahrenheit = temp
    
    celsius = (temp - 32) * 5/9
    converted_scale = celsius
    converted_unit = 'C'
else:
    print("Invalid scale entered. Please use 'C' or 'F'.")
    fahrenheit = None 


if fahrenheit is not None:
    
    print(f"{temp:.1f}°{scale} = {converted_scale:.1f}°{converted_unit}")

    
    print("Weather Advice:", end=" ")
    if fahrenheit < 32:
        print("Freezing! Bundle up warmly!") 
    elif fahrenheit <= 50:
        print("Cold - wear a warm jacket") 
    elif fahrenheit <= 70:
        print("Cool - a light jacket would be nice") 
    elif fahrenheit <= 85:
        print("Pleasant - enjoy the weather!") 
    else: 
        print("Hot - stay hydrated!") 

print("-" * 40)
print("\nPROBLEM 2: Movie Ticket Pricing System")
print("=" * 40)


print("=== Movie Theater Ticket System ===")

age = int(input("Enter customer age: "))
day = input("Enter day of week: ").lower()


base_price = 15.00 
discount_reason = "Regular"
final_price = 0.0


if day == 'tuesday':
    final_price = 7.00 
    discount_reason = "Tuesday Special!"
    
else:
    
    show_time = int(input("Enter show time (0-23): "))
    
    
    if age <= 12:
        base_price = 8.00 
        discount_reason = "Child"
    elif age >= 65:
        base_price = 10.00 
        discount_reason = "Senior"
    
    
    final_price = base_price
    
    
    is_matinee = show_time < 17
    
    if is_matinee:
        matinee_discount = 3.00 
        final_price -= matinee_discount
        
        
        if discount_reason != "Regular":
            discount_reason = f"{discount_reason} Matinee"
        else:
            discount_reason = "Matinee"
            

print(f"Your ticket price: ${final_price:.2f} ({discount_reason})")

print("-" * 40)



print("\nPROBLEM 3: Grade Calculator with Letter Grade")
print("=" * 40)


print("=== Grade Calculator ===")

test1 = float(input("Enter Test 1 score (0-100): "))
test2 = float(input("Enter Test 2 score (0-100): "))
test3 = float(input("Enter Test 3 score (0-100): "))


if (0 <= test1 <= 100) and (0 <= test2 <= 100) and (0 <= test3 <= 100):
    
    
    average = (test1 + test2 + test3) / 3
    
    
    letter_grade = ""
    if average >= 90:
        letter_grade = "A" 
    elif average >= 80:
        letter_grade = "B" 
    elif average >= 70:
        letter_grade = "C" 
    elif average >= 60:
        letter_grade = "D" 
    else:
        letter_grade = "F" 

    
    is_passing_grade = (letter_grade != "F")
    
    
    has_one_good_test = (test1 >= 60) or (test2 >= 60) or (test3 >= 60)
    
    
    if is_passing_grade and has_one_good_test:
        status = "PASSING"
    else:
        status = "FAILING"
        
    
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"Status: {status}")
    
else:
    
    print("Error: One or more test scores are outside the valid range (0-100).")

print("-" * 40)
print("\nPROBLEM 4: Password Strength Checker")
print("=" * 40)


print("=== Password Strength Checker ===")
password = input("Enter a password to check: ")


criteria_met = 0
feedback = []
common_passwords = ["password", "12345678", "qwerty"]


is_long_enough = len(password) >= 8
if is_long_enough:
    criteria_met += 1
else:
    feedback.append(f"- Password should be at least 8 characters (currently {len(password)})")
    

has_uppercase = password.lower() != password 
if has_uppercase:
    criteria_met += 1
else:
    feedback.append("- Password must contain at least one uppercase letter.")


has_lowercase = password.upper() != password 
if has_lowercase:
    criteria_met += 1
else:
    feedback.append("- Password must contain at least one lowercase letter.")


has_digit = any(char.isdigit() for char in password)
if has_digit:
    criteria_met += 1
else:
    feedback.append("- Password must contain at least one digit.")


is_not_common = password.lower() not in common_passwords
if is_not_common:
    criteria_met += 1
else:
    feedback.append("- Password is a common, easily guessable sequence.")


strength = ""
if criteria_met == 5:
    strength = "STRONG" 
elif criteria_met == 4:
    strength = "GOOD" 
elif criteria_met == 3:
    strength = "FAIR" 
else: 
    strength = "WEAK" 


print(f"Password Strength: {strength}")
print(f"Criteria met: {criteria_met} out of 5")
if feedback:
    print("Issues to improve:")
    for issue in feedback:
        print(issue)
else:
    print("No issues found. Excellent password!")

print("-" * 40)
print("\nPROBLEM 5: Restaurant Bill Calculator (Bonus)")
print("=" * 40)


print("=== Restaurant Bill Calculator ===")

food_total = float(input("Enter food total: $"))
is_holiday = input("Is today a holiday? (yes/no): ").lower()
party_size = int(input("How many people in your party? "))


final_bill = food_total
subtotal_after_discounts = food_total
total_discounts = 0.0
breakdown = [f"Food Total: ${food_total:.2f}"]


holiday_surcharge_rate = 0.15
if is_holiday == 'yes':
    surcharge_amount = food_total * holiday_surcharge_rate
    final_bill += surcharge_amount
    subtotal_after_discounts = final_bill 
    breakdown.append(f"Holiday Surcharge (15%): +${surcharge_amount:.2f}")


is_member = input("Are you a member? (yes/no): ").lower()
day = input("What day is it? ").lower()


member_discount_rate = 0.10
if is_member == 'yes':
    discount_amount = subtotal_after_discounts * member_discount_rate
    final_bill -= discount_amount
    total_discounts += discount_amount
    breakdown.append(f"Member Discount (10%): -${discount_amount:.2f}")

senior_discount_amount = 0.0
senior_discount_rate = 0.10
has_seniors = 'no'

if day == 'wednesday':
    
    has_seniors = input("Does your party include seniors (65+)? (yes/no): ").lower()
    
    if has_seniors == 'yes':
        
        discount_amount = final_bill * senior_discount_rate
        final_bill -= discount_amount
        total_discounts += discount_amount
        breakdown.append(f"Senior Wednesday Discount (10%): -${discount_amount:.2f}")


subtotal_after_discounts_and_surcharge = food_total + (food_total * holiday_surcharge_rate if is_holiday == 'yes' else 0) - total_discounts
breakdown.append(f"Subtotal: ${subtotal_after_discounts_and_surcharge:.2f}")


tax_rate = 0.085
tax_amount = subtotal_after_discounts_and_surcharge * tax_rate
final_bill += tax_amount
breakdown.append(f"Tax ({tax_rate * 100:.1f}%): ${tax_amount:.2f}")

gratuity_amount = 0.0
gratuity_rate = 0.18

if party_size >= 6:
    gratuity_amount = subtotal_after_discounts_and_surcharge * gratuity_rate
    final_bill += gratuity_amount
    breakdown.append(f"Automatic Gratuity ({gratuity_rate * 100:.0f}%): ${gratuity_amount:.2f}")


print("\nBill Breakdown")
for item in breakdown:
    print(item)

print(f"Total: ${final_bill:.2f}")
print("Thank you for dining with us!")

print("-" * 40)
