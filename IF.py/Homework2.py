#CS 1300-Homework 2
# Name: Brayden Kuppusami
#Date: 11/28/2025
#Description: Variables, Input/Output, and Type Conversions

print("=" * 50)
print("CS 1300 - HOMEWORK 2")
print("=" * 50)

print("\n" + "=" * 40)
print("Problem 1: Personal Finance Calculator")
print("=" * 40)

print("\n" + "=" * 30)
print("PERSONAL FINANCE CALCULATOR".center(30))
print("=" * 30)

try:
    monthly_income = float(input("Enter your monthly income: "))
    rent_cost = float(input("Enter housing/rent cost: "))
    food_expenses = float(input("Enter food expenses: "))
    transport_cost = float(input("Enter transportation cost: "))
    other_expenses = float(input("Enter other expenses: "))

    total_expenses = rent_cost + food_expenses + transport_cost + other_expenses
    remaining_balance = monthly_income - total_expenses

    if monthly_income > 0:
        savings_rate = remaining_balance / monthly_income
        
    else:
        savings_rate = 0.0

    print("\n" + "=" * 30)
    print("MONTHLY BUDGET REPORT".center(30))
    print("=" * 30)

    print(f"Income: {'$'}{monthly_income:10.2f}")
    print("-" * 30)
    print("Expenses:")
    print(f"  Housing: {'$'}{rent_cost:10.2f}")
    print(f"  Food:    {'$'}{food_expenses:10.2f}")
    print(f"  Transport: {'$'}{transport_cost:10.2f}")
    print(f"  Other:   {'$'}{other_expenses:10.2f}")
    print("-" * 30)
    print(f"Total Expenses:  {'$'}{total_expenses:10.2f}")
    print(f"Remaining Balance: {'$'}{remaining_balance:10.2f}")
    print("-" * 30)
    # Savings Rate formatted as a percentage with one decimal place
    print(f"Savings Rate: {savings_rate:10.1%}")
    print("=" * 30)

except ValueError:
    print("\nError: Please enter valid numbers for all financial inputs.")

print("\n" + "=" * 40)
print("Problem 2: Grade Statistics Calculator")
print("=" * 40)

print("\n" + "*" * 40)
print("GRADE STATISTICS CALCULATOR".center(40))
print("*" * 40)

try:
    # Get scores and convert to float for precise calculations
    score1 = float(input("Enter score for Test 1 (out of 100): "))
    score2 = float(input("Enter score for Test 2 (out of 100): "))
    score3 = float(input("Enter score for Test 3 (out of 100): "))
    score4 = float(input("Enter score for Test 4 (out of 100): "))
    score5 = float(input("Enter score for Test 5 (out of 100): "))

    scores = [score1, score2, score3, score4, score5]

    if any(s < 0 or s > 100 for s in scores):
         print("\nWarning: Scores should be between 0 and 100. Calculations proceed with entered values.")

    total_points = sum(scores)  
    num_tests = len(scores)     
    highest_possible_total = num_tests * 100 
    average_score = total_points / num_tests
    overall_percentage = total_points / highest_possible_total 

    points_for_90 = (0.90 * highest_possible_total) - total_points

    points_needed_for_90 = max(0.0, points_for_90)

    print("\n" + "*" * 40)
    print("GRADE REPORT".center(40))
    print("*" * 40)

    print("Test Scores Entered:")
    for i, score in enumerate(scores):
        print(f"Test {i+1}: {score:8.1f}/100")

    print("-" * 40)

    print("Statistics:")
    print(f"Total Points:    {total_points:8.1f}/{highest_possible_total}")
    print(f"Average Score:   {average_score:8.1f}")
   
    print(f"Overall Grade:   {overall_percentage:8.1%}")
    print(f"Points needed for 90%: {points_needed_for_90:8.1f}")
    print("*" * 40)

except ValueError:
    print("\nError: Please enter valid numbers for all test scores.")

print("\n" + "=" * 40)
print("Problem 3: Time Zone Converter")
print("=" * 40)

print("\n+-----------------------+")
print("| TIME ZONE CONVERTER |")
print("+-----------------------+")

try:
    
    est_hour_input = int(input("Enter current hour (EST, 0-23): "))
    minute = int(input("Enter current minute (0-59): "))

    if not (0 <= est_hour_input <= 23 and 0 <= minute <= 59):
        print("\nError: Please enter a valid hour (0-23) and minute (0-59).")
    else:
        
        

        est_hour = est_hour_input
        
        
        cst_hour = (est_hour - 1) % 24
        
        
        mst_hour = (est_hour - 2) % 24
        
        
        pst_hour = (est_hour - 3) % 24
        
        
        def format_12hr(hr_24, mn):
            
            hr_12 = hr_24 % 12
            
            if hr_12 == 0:
                hr_12 = 12
            
            
            am_pm = "AM" if hr_24 < 12 else "PM" 
            
            mn_str = f"{mn:02d}"
            
            return f"{hr_12}:{mn_str} {am_pm}"

        
        times = {
            "EST": (est_hour, minute),
            "CST": (cst_hour, minute),
            "MST": (mst_hour, minute),
            "PST": (pst_hour, minute)
        }
        
        
        print("\n+-----------------------+")
        print("| CURRENT TIMES         |")
        print("+-----------------------+")
        
        
        print("| Time Zone | Time | 12-hr Format |")
        print("|-----------|------|--------------|")
        
        
        for zone, (hr_24, mn) in times.items():
            time_24hr = f"{hr_24:02d}:{mn:02d}"
            time_12hr = format_12hr(hr_24, mn)
            
            print(f"| {zone:<9} | {time_24hr:4} | {time_12hr:>12} |")
            
        print("+-----------------------+")
        print("Note: Simple conversion (no date change handling)")

except ValueError:
    print("\nError: Please enter valid integers for the hour and minute.")

print("\n" + "=" * 40)
print("Problem 4: Recipe Scaler")
print("=" * 40)

print("\n" + "#" * 50)
print("RECIPE SCALER".center(50))
print("#" * 50)

try:
    original_servings = int(input("Enter original serving size: "))
    desired_servings = int(input("Enter desired serving size: "))
    
    if original_servings <= 0:
        print("\nError: Original serving size must be greater than zero.")
    else:
        
        print("\nEnter 5 ingredients:")
        
        ingredients_data = [] 
        
        for i in range(1, 6):
            name = input(f"Ingredient {i} name: ")
            amount = float(input("Amount: "))
            unit = input("Unit: ")
            ingredients_data.append((name, amount, unit))
            
        
        scaling_factor = desired_servings / original_servings
        
        
        print("\n" + "#" * 50)
        print("RECIPE SCALING RESULTS".center(50))
        print("#" * 50)
        
        
        print(f"Scaling factor: {scaling_factor:.2f}x ({original_servings}->{desired_servings} servings)\n")
        
        
        header_original = f"Original Recipe ({original_servings} servings)"
        header_scaled = f"Scaled Recipe ({desired_servings} servings)"
        
        
        name_width = 10
        amount_width = 12
        
        print(f"{header_original:^{name_width+amount_width+1}} | {header_scaled:^{name_width+amount_width+1}}")
        print("-" * (name_width + amount_width + 1) + "+" + "-" * (name_width + amount_width + 1))
        
        
        for name, original_amount, unit in ingredients_data:
            scaled_amount = original_amount * scaling_factor
            
            
            original_display = f"{name:<{name_width}}: {original_amount:>{amount_width-1}.2f} {unit}"
            
            
            scaled_display = f"{name:<{name_width}}: {scaled_amount:>{amount_width-1}.2f} {unit}"
            
            
            print(f"{original_display:<{name_width+amount_width+1}} | {scaled_display}")

        print("#" * 50)

except ValueError:
    print("\nError: Please ensure serving sizes are integers and amounts are valid numbers.")

print("\n" + "=" * 50)
print("END OF HOMEWORK 2")
print("=" * 50)
