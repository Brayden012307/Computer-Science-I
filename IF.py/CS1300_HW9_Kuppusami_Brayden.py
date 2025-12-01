# Problem 1: Temperature Converter (30 points)

def celsius_to_fahrenheit (celsius):
    """Convert Celsius to Fahrenheit"""
    # Formula: F = C * 9/5 + 32
    # The formula is used to calculate the Fahrenheit equivalent of the input Celsius temperature.
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit

def fahrenheit_to_celsius (fahrenheit):
    """Convert Fahrenheit to Celsius"""
    # Formula: C = (F - 32) * 5/9
    # The formula is used to calculate the Celsius equivalent of the input Fahrenheit temperature.
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def temperature_report (temp, scale="C"):
    """
    Print temperature in both scales.

    Parameters:
    temp: temperature value
    scale: "C" for Celsius or "F" for Fahrenheit (default "C")
    """
    # Check if the input scale is Celsius ("C")
    if scale == "C":
        # Convert the Celsius temperature to Fahrenheit
        converted_temp = celsius_to_fahrenheit(temp)
        # Display the result in the format: X°C = Y.Y°F
        print(f"{temp}°C = {converted_temp:.1f}°F") # [cite: 38]
    # Check if the input scale is Fahrenheit ("F")
    elif scale == "F":
        # Convert the Fahrenheit temperature to Celsius
        converted_temp = fahrenheit_to_celsius(temp)
        # Display the result in the format: X°F = Y.Y°C
        print(f"{temp}°F = {converted_temp:.1f}°C") # [cite: 39]
    # Handle an invalid scale input
    else:
        print("Invalid scale parameter. Use 'C' for Celsius or 'F' for Fahrenheit.")

# Test cases for Problem 1
print("--- Problem 1 Test Cases ---")
# Test 1
print(celsius_to_fahrenheit(0)) # Should print 32.0 [cite: 28]
print(celsius_to_fahrenheit(100)) # Should print 212.0 [cite: 32]

# Test 2
print(fahrenheit_to_celsius(32)) # Should print 0.0 [cite: 34, 37]
print(fahrenheit_to_celsius(68)) # Should print 20.0 [cite: 34, 37]

# Test 3
temperature_report(25) # Should show: 25°C=77.0°F [cite: 35, 38]
temperature_report(77, "F") # Should show: 77°F=25.0°C [cite: 36, 39]
print("----------------------------")

# Problem 2: Grade Calculator with Multiple Parameters (35 points)

def calculate_weighted_grade (homework, midterm, final, hw_weight=0.3, mid_weight=0.3, final_weight=0.4):
    """
    Calculate weighted grade.

    Parameters:
    homework: homework average (0-100)
    midterm: midterm score (0-100)
    final: final exam score (0-100)
    hw_weight: homework weight (default 0.3)
    mid_weight: midterm weight (default 0.3)
    final_weight: final weight (default 0.4)

    Returns:
    Weighted average as float
    """
    # Calculate the weighted average by multiplying each score by its corresponding weight
    weighted_grade = (homework * hw_weight) + (midterm * mid_weight) + (final * final_weight)
    return weighted_grade

def get_letter_grade (score):
    """Convert numeric score to letter grade"""
    # A: >=90, B: >=80, C: >=70, D: >=60, F: < 60 [cite: 57]
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def print_grade_report (name, hw, mid, final):
    """Print complete grade report for a student"""
    # Calculate the weighted average using the default weights
    weighted_average = calculate_weighted_grade(hw, mid, final)
    # Get the letter grade for the weighted average
    letter_grade = get_letter_grade(weighted_average)

    # Print the formatted report
    print("\n--- Grade Report ---")
    print(f"Student Name: {name}") # [cite: 62]
    print(f"Individual Scores:")
    print(f"  Homework: {hw}") # [cite: 64]
    print(f"  Midterm: {mid}")
    print(f"  Final: {final}")
    print(f"Weighted Average: {weighted_average:.1f}") # [cite: 65]
    print(f"Letter Grade: {letter_grade}") # [cite: 67]
    print("--------------------")

# Test cases for Problem 2
print("\n--- Problem 2 Test Cases ---")
# Test 1: Default weights [cite: 73]
# Need to declare and assign 'grade1' outside the print statement for the provided test case structure
grade1 = calculate_weighted_grade(85, 78, 92) # [cite: 75]
print(f"Grade 1: {grade1:.1f}") # Should be ~85.9 [cite: 76]

# Test 2: Custom weights [cite: 77]
# Need to declare and assign 'grade2' outside the print statement for the provided test case structure
grade2 = calculate_weighted_grade(90, 85, 80, hw_weight=0.4, mid_weight=0.2, final_weight=0.4) # [cite: 79, 80]
print(f"Grade 2: {grade2:.1f}") # Should be 86.0 [cite: 81]

# Test 3: Complete report [cite: 82]
print_grade_report("Alice Smith", 88, 91, 85) # [cite: 83, 84]
print("----------------------------")

# Problem 3: Scope Challenge (35 points)

# Initial global variables
total_points = 0
bonus_multiplier = 1.1

def add_score (points):
    """Add points to total score"""
    # global keyword is needed here to modify the global variable total_points.
    # Without it, the function would create a local 'total_points' and crash when trying to read the global one. [cite: 107, 108]
    global total_points
    total_points = total_points + points
    return total_points

def apply_bonus():
    """Apply bonus multiplier to total"""
    # global keyword is needed here to modify the global variable total_points.
    # Without it, the function would create a local 'total_points' and crash when trying to read the global one. [cite: 107, 108]
    global total_points
    # We do NOT need 'global bonus_multiplier' because we are only reading its value, not modifying it.
    total_points = total_points * bonus_multiplier

def get_final_score():
    """Get the final score"""
    # The variable 'final' was not assigned, causing an error.
    # We should directly return the global 'total_points'.
    # We are only reading the global variable, so 'global total_points' is not strictly required,
    # but it's good practice for clarity in a scope-challenging problem.
    return total_points # Fixed to return total_points

# New function: reset_game() [cite: 109]
def reset_game():
    """Resets the global total_points to 0"""
    # global keyword is needed to modify the global total_points variable. [cite: 107]
    global total_points
    total_points = 0
    print("Total points reset to 0.")

# Test your fixes:
print("\n--- Problem 3 Test Cases (Fixes) ---")
reset_game() # Ensure a clean start before the main test

add_score(100) # [cite: 102]
add_score(50) # [cite: 103]
apply_bonus() # [cite: 104]
# total_points should now be (100 + 50) * 1.1 = 165.0
print(f"Final score: {get_final_score():.1f}") # Should print 165.0 [cite: 105]
print("------------------------------------")

# Bonus: Rewrite to avoid using global variables (5 extra points)

# Initial state for total_points and bonus_multiplier, now passed/returned
bonus_multiplier_B = 1.1

def add_score_B (current_points, points_to_add):
    """Add points to total score, returning the new total"""
    new_total = current_points + points_to_add
    return new_total

def apply_bonus_B(current_points, multiplier):
    """Apply bonus multiplier to total, returning the new total"""
    new_total = current_points * multiplier
    return new_total

def get_final_score_B(current_points):
    """Get the final score"""
    return current_points

# New function: reset_game_B() - Now just returns the starting value
def reset_game_B():
    """Returns the starting value of 0"""
    return 0

# Test the Bonus fixes:
print("\n--- Bonus Test Cases (No Globals) ---")
current_score = reset_game_B() # Start at 0

current_score = add_score_B(current_score, 100) # 0 + 100 = 100
current_score = add_score_B(current_score, 50) # 100 + 50 = 150
current_score = apply_bonus_B(current_score, bonus_multiplier_B) # 150 * 1.1 = 165.0
final_score = get_final_score_B(current_score)

print(f"Final score: {final_score:.1f}") # Should print 165.0
print("------------------------------------")

