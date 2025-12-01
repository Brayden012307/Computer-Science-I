"""
CS1300 - Homework #5: Advanced Control Structures
Name: Brayden Kuppusami
Date: 11/29/2025
Description: Advanced conditional logic and validation
"""

print("=== SMART THERMOSTAT SYSTEM ===")

current_temp = float(input("Current temperature (F): "))
desired_temp = float(input("Desired temperature (F): "))
hour = int(input("Current hour (0-23): "))
season = input("Season (summer/winter/spring/fall): ").lower()


is_comfortable = 68 <= current_temp <= 76


is_night = (hour >= 22) or (hour <= 6)
night_adjustment = -3 if is_night else 0


target_temp = desired_temp + night_adjustment


original_target = target_temp

if season == "summer":
    
    target_temp = max(target_temp, 72)
elif season == "winter":
    
    target_temp = min(target_temp, 70)


adjustment_applied = original_target != target_temp
temp_difference = abs(current_temp - target_temp)
time_to_reach = temp_difference / 2.0  


diff = abs(current_temp - target_temp)
if diff <= 2:
    efficiency = "EXCELLENT"
elif diff <= 5:
    efficiency = "GOOD"
elif diff <= 10:
    efficiency = "FAIR"
else:
    efficiency = "POOR"


print("\nCurrent Status:")
comfort_status = "Comfortable" if is_comfortable else "Too warm" if current_temp > 76 else "Too cold"
print(f"Current temp: {current_temp}°F ({comfort_status})")
print(f"Night mode: {'ACTIVE (reducing target by 3°F)' if is_night else 'INACTIVE'}")
if adjustment_applied:
    print(f"Season: {season.capitalize()} limit applied.")

print("\nAdjustments:")
print(f"Desired: {desired_temp}°F")
print(f"Night adjustment: {desired_temp + night_adjustment}°F")
print(f"Final target: {target_temp}°F")

print(f"Heating/Cooling required: {temp_difference:.1f}°F")
print(f"Estimated time: {time_to_reach:.1f} hours")
print(f"Energy efficiency: {efficiency}")

import string

print("=== PASSWORD SECURITY ANALYZER ===")
password = input("Enter password to analyze: ")


score = 0
recommendations = []


length_points = 30 if len(password) >= 16 else (20 if len(password) >= 12 else (10 if len(password) >= 8 else 0))
score += length_points
if len(password) < 8:
    recommendations.append("Password is too short. Use at least 8 characters.")
elif len(password) < 16:
    recommendations.append("Consider using 16+ characters for maximum security.")


has_upper = any(c.isupper() for c in password)
upper_points = 15 if has_upper else 0
score += upper_points
if not has_upper:
    recommendations.append("Include uppercase letters (A-Z).")


has_lower = any(c.islower() for c in password)
lower_points = 15 if has_lower else 0
score += lower_points
if not has_lower:
    recommendations.append("Include lowercase letters (a-z).")


has_digit = any(c.isdigit() for c in password)
digit_points = 15 if has_digit else 0
score += digit_points
if not has_digit:
    recommendations.append("Include numbers (0-9).")


special_chars = string.punctuation
has_special = any(c in special_chars for c in password)
special_points = 15 if has_special else 0
score += special_points
if not has_special:
    recommendations.append("Include special characters (e.g., !@#$%^).")


common_patterns = ["123", "abc", "qwerty", "password", "111"]
has_pattern = any(pattern in password.lower() for pattern in common_patterns)
pattern_points = -10 if has_pattern else 0
score += pattern_points
if has_pattern:
    recommendations.append("Avoid common patterns (like '123' or 'password').")




strength_level = ("EXCELLENT" if score >= 90 else 
                  ("STRONG" if score >= 75 else 
                   ("GOOD" if score >= 50 else 
                    ("WEAK" if score >= 25 else "VERY WEAK"))))



def display_check(points, max_points, name, check_var):
    status = "✓" if check_var else "X"
    return f"{status} {name}: {'Yes' if check_var else 'No'} ({points}/{max_points} points)"

print("\nSecurity Analysis:")
print(f"Length: {len(password)} characters ({length_points}/30 points)")
print(display_check(upper_points, 15, "Uppercase letters", has_upper))
print(display_check(lower_points, 15, "Lowercase letters", has_lower))
print(display_check(digit_points, 15, "Numbers", has_digit))
print(display_check(special_points, 15, "Special characters", has_special))
pattern_status = "X Common patterns detected" if has_pattern else "✓ No common patterns detected"
print(f"{pattern_status} ({pattern_points} points)")

print(f"\nTotal Score: {score}/100")
print(f"Strength Level: {strength_level}")

print("\nRecommendations:")
if not recommendations:
    print("Great job! Your password is secure.")
else:
    for rec in recommendations:
        print(f"* {rec}")

print("=== GRADE VALIDATION SYSTEM ===")

try:
    test1 = float(input("Test 1 score: "))
    test2 = float(input("Test 2 score: "))
    test3 = float(input("Test 3 score: "))
    test4 = float(input("Test 4 score: "))
    scores = [test1, test2, test3, test4]
except ValueError:
    print("\nERROR: Scores must be numbers.")
    exit()


all_valid_range = (0 <= test1 <= 100) and \
                  (0 <= test2 <= 100) and \
                  (0 <= test3 <= 100) and \
                  (0 <= test4 <= 100)


all_identical = (test1 == test2) and (test2 == test3) and (test3 == test4)


huge_jump = (abs(test2 - test1) > 40) or \
            (abs(test3 - test2) > 40) or \
            (abs(test4 - test3) > 40)


all_perfect = all_identical and (test1 == 100)


is_suspicious = all_identical or huge_jump or all_perfect
validation_passed = all_valid_range and (not is_suspicious)

print("\nValidation Results:")
print(f"✓ All scores in valid range (0-100)" if all_valid_range else "X Invalid score range detected")
print(f"✓ Scores show normal variation" if not huge_jump else "X Huge jump in scores detected (>40 points)")
print(f"✓ Scores are not all identical" if not all_identical else "X All scores are identical (Suspicious)")
if all_perfect:
    print("X All perfect scores (Verify manually)")

if validation_passed:
    
    average = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)
    overall_improvement = test4 - test1
    trend = "IMPROVING" if overall_improvement > 5 else ("DECLINING" if overall_improvement < -5 else "CONSISTENT")

    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    status = "PASSING" if average >= 60 else "FAILING"

    print("\nStatistics:")
    print(f"Average: {average:.2f}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Trend: {trend} ({overall_improvement:+.0f} points overall)")
    print(f"Grade: {grade}")
    print(f"Status: {status}")
    print("\nPerformance: Consistent improvement shown!" if trend == "IMPROVING" else f"Performance: {trend} trend detected.")
else:
    print("\nStatus: VALIDATION FAILED. Cannot calculate statistics.")

import datetime

print("=== EVENT SCHEDULING SYSTEM ===")


valid_days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def time_to_minutes(time_float):
    hours = int(time_float)
    minutes = int((time_float - hours) * 60)
    return hours * 60 + minutes


print("\nEVENT 1 DETAILS:")
event1_name = input("Event name: ")
event1_day = input("Day (Mon-Sun): ").lower()[:3]
try:
    event1_start = float(input("Start time (0-24): "))
    event1_end = float(input("End time (0-24): "))
except ValueError:
    print("ERROR: Time must be a number.")
    exit()


print("\nEVENT 2 DETAILS:")
event2_name = input("Event name: ")
event2_day = input("Day (Mon-Sun): ").lower()[:3]
try:
    event2_start = float(input("Start time (0-24): "))
    event2_end = float(input("End time (0-24): "))
except ValueError:
    print("ERROR: Time must be a number.")
    exit()


event1_valid = (event1_day in valid_days) and \
               (0 <= event1_start <= 24) and \
               (0 <= event1_end <= 24) and \
               (event1_end > event1_start)

event2_valid = (event2_day in valid_days) and \
               (0 <= event2_start <= 24) and \
               (0 <= event2_end <= 24) and \
               (event2_end > event2_start)

all_valid = event1_valid and event2_valid

print("\nSchedule Analysis:")
print(f"✓ Both events have valid times" if all_valid else "X Validation failed for one or both events")

if all_valid:
    
    too_early = (event1_start < 6) or (event2_start < 6)
    too_late = (event1_end > 23) or (event2_end > 23)
    
    if too_early or too_late:
        print("X Warning: Events scheduled too early (before 6) or too late (after 23).")
    else:
        print("✓ Events are within reasonable hours.")

    
    same_day = event1_day == event2_day
    
    
    overlap = same_day and (event1_start < event2_end) and (event2_start < event1_end)
    
    
    gap = 0
    is_back_to_back = False

    if same_day:
        
        if event1_end <= event2_start: 
            gap = time_to_minutes(event2_start) - time_to_minutes(event1_end)
        elif event2_end <= event1_start: 
            gap = time_to_minutes(event1_start) - time_to_minutes(event2_end)
        else:
            
            gap = -1 
        
        is_back_to_back = (gap >= 0) and (gap < 30)

    if overlap:
        print("X **CONFLICT DETECTED**: Events have a direct time overlap.")
    else:
        print("✓ No direct time conflict.")

    if is_back_to_back:
        print(f"X Warning: Events are back-to-back ({gap} minute gap).")
    else:
        print(f"✓ Sufficient buffer time between events." if same_day and gap >= 30 else "")

    
    duration1 = event1_end - event1_start
    duration2 = event2_end - event2_start
    total_time = duration1 + duration2
    
    
    def format_time(time_float):
        hours = int(time_float)
        minutes = int((time_float - hours) * 60)
        return f"{hours:02d}:{minutes:02d}"

    print(f"\nEvent 1: {event1_name}")
    print(f"- {event1_day.capitalize()} {format_time(event1_start)} - {format_time(event1_end)} ({duration1:.1f} hours)")
    
    print(f"Event 2: {event2_name}")
    print(f"- {event2_day.capitalize()} {format_time(event2_start)} - {format_time(event2_end)} ({duration2:.1f} hours)")

    print(f"\nTotal time commitment: {total_time:.1f} hours")
    
    
    print("\nRecommendation:")
    if overlap:
        print("Reschedule one event to completely avoid overlap.")
    elif is_back_to_back:
        print("Consider adding buffer time (e.g., 30+ minutes) between events.")
    elif too_early or too_late:
        print("Try to shift events to be between 6:00 and 23:00.")
    else:
        print("Schedule looks good!")

print("=== RETAIL DISCOUNT CALCULATOR ===")

try:
    price = float(input("Item price: $"))
    quantity = int(input("Quantity: "))
except ValueError:
    print("\nERROR: Price and quantity must be valid numbers.")
    exit()
    
customer_type = input("Customer type (regular/member/vip/employee): ").lower()
day = input("Day of week: ").lower()
coupon = input("Coupon code (or 'none'): ").upper()


subtotal = price * quantity
current_price = subtotal
total_discount_amount = 0
total_discount_rate = 0
discount_breakdown = []


def apply_discount(rate, name):
    global current_price, total_discount_amount, total_discount_rate
    
    
    discount_amount = current_price * rate
    
    
    if total_discount_rate + rate > 0.40:
        rate_applied = 0.40 - total_discount_rate
        
        discount_amount = current_price * rate_applied
        name += " (Max Limit Reached)"
        
    else:
        rate_applied = rate

    if rate_applied > 0:
        current_price -= discount_amount
        total_discount_amount += discount_amount
        total_discount_rate += rate_applied
        
        
        discount_breakdown.append({
            'name': name,
            'rate': rate,
            'amount': discount_amount,
            'new_price': current_price
        })
    return rate_applied



bulk_rate = (0.20 if quantity >= 50 else (0.15 if quantity >= 20 else (0.10 if quantity >= 10 else 0.0)))
if bulk_rate > 0:
    apply_discount(bulk_rate, f"Bulk discount ({quantity} items): {int(bulk_rate * 100)}% off")


if customer_type == "employee":
    cust_rate = 0.15
elif customer_type == "vip":
    cust_rate = 0.10
elif customer_type == "member":
    cust_rate = 0.05
else:
    cust_rate = 0.0
    
if cust_rate > 0:
    apply_discount(cust_rate, f"{customer_type.capitalize()} discount: {int(cust_rate * 100)}% off")


day_rate = 0.0
if day == "tuesday":
    day_rate = 0.05
elif day in ["saturday", "sunday"]:
    day_rate = 0.10

if day_rate > 0:
    apply_discount(day_rate, f"{day.capitalize()} special: {int(day_rate * 100)}% off")


coupon_rate = 0.0
if coupon == "SAVE20":
    coupon_rate = 0.20
elif coupon == "SAVE10":
    coupon_rate = 0.10
elif coupon == "STUDENT":
    coupon_rate = 0.15
    
if coupon_rate > 0:
    apply_discount(coupon_rate, f"Coupon {coupon}: {int(coupon_rate * 100)}% off")


print("\nOrder Summary:")
print(f"Items: {quantity} x ${price:.2f} = ${subtotal:.2f}")

print("\nDiscounts Applied:")
if not discount_breakdown:
    print("No discounts applied.")
else:
    for i, item in enumerate(discount_breakdown):
        print(f"{i+1}. {item['name']} = -${item['amount']:.2f}")
        print(f"   Subtotal: ${item['new_price']:.2f}")

final_price = current_price
total_discount_percent = total_discount_amount / subtotal * 100

print(f"\nTotal Discount: ${total_discount_amount:.2f} ({total_discount_percent:.1f}%)")
print(f"Final Price: ${final_price:.2f}")
print(f"You saved: ${total_discount_amount:.2f}!")

