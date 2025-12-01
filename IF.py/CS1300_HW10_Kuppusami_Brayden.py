 
# --- Problem 1: Statistics Calculator (40 points) ---
# Create a modular statistics program using built-in functions.

def get_numbers():
    """
    Get numbers from user until they enter 'done'.
    Returns a list of floats.
    """
    numbers = []
    print("\nEnter numbers one by one. Enter 'done' to stop.")
    while True:
        # Use input()
        user_input = input("> ").strip().lower()
        
        # Handle 'done' to stop
        if user_input == 'done':
            break
        
        try:
            # Use float() conversion
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
            
    return numbers

def calculate_stats(numbers):
    """
    Calculate min, max, average, and range of a list of numbers.
    Returns all four values: minimum, maximum, average, range_val.
    """
    if not numbers:
        return None, None, None, None 

    # Use built-in functions: min(), max(), sum(), len()
    minimum = min(numbers)
    maximum = max(numbers)
    
    # Calculate average and range
    average = sum(numbers) / len(numbers)
    range_val = maximum - minimum 
    
    return minimum, maximum, average, range_val

def format_stats(minimum, maximum, average, range_val):
    """
    Format statistics for display.
    Returns a formatted string.
    """
    # Use round() for 2 decimal places in the output string
    formatted_output = (
        f"Minimum: {minimum:.2f}\n"
        f"Maximum: {maximum:.2f}\n"
        f"Average: {average:.2f}\n"
        f"Range: {range_val:.2f}"
    )
    return formatted_output

def problem_1_main():
    """Main program using modular design for Problem 1."""
    print("=== Statistics Calculator ===")
    
    # 1. Get numbers
    numbers = get_numbers()
    
    if not numbers:
        print("No numbers entered. Cannot calculate statistics.")
        return

    # 2. Calculate stats
    minimum, maximum, average, range_val = calculate_stats(numbers)
    
    # 3. Format output
    stats_string = format_stats(minimum, maximum, average, range_val)
    
    # 4. Display result
    print("\n--- Results ---")
    print(stats_string)
    print("-----------------\n")

# -------------------------------------------------------------

# --- Problem 2: Grade Processing System (40 points) ---
# Design a complete grade processing system with helper functions.

def validate_score(score_str):
    """
    Helper: Validate that string is a valid score (0-100).
    Returns True/False.
    """
    # Check if string is digit
    if not score_str.isdigit():
        return False
        
    score = int(score_str)
    
    # Check if in range 0-100
    return 0 <= score <= 100

def get_valid_score(prompt):
    """
    Helper: Get validated score from user.
    Keep asking until valid.
    Returns integer score.
    """
    while True:
        score_str = input(prompt).strip()
        
        # Use validate_score() helper
        if validate_score(score_str):
            # Return integer score
            return int(score_str)
        else:
            print("Invalid score. Please enter an integer between 0 and 100.")

def calculate_letter(score):
    """
    Helper: Convert score to letter grade.
    A: >= 90, B: >= 80, C: >= 70, D: >= 60, F: < 60
    """
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

def process_student():
    """
    Process one student's grades: get 3 scores, calculate average and letter.
    Returns name, scores list, average, and letter grade.
    """
    # Get name
    name = input("\nEnter student's name: ").strip()
    
    scores = []
    # Get 3 scores (Use helper function for input/validation)
    for i in range(1, 4):
        score = get_valid_score(f"Enter score for Test {i} (0-100): ")
        scores.append(score)

    # Calculate results
    if scores:
        # Use sum() and len() built-ins
        average = sum(scores) / len(scores)
    else:
        average = 0
        
    # Calculate letter (Use helper function)
    letter = calculate_letter(average)
    
    return name, scores, average, letter

def display_report(name, scores, average, letter):
    """
    Display formatted student report.
    """
    print("\n--- Student Grade Report ---")
    print(f"Student: {name}")
    print(f"Scores: {scores}")
    print(f"Average Score: {average:.2f}") 
    print(f"Letter Grade: {letter}")
    print("----------------------------")

def problem_2_main():
    """Main program process multiple students."""
    print("=== Grade Processing System ===")
    
    class_scores = []
    
    # Ask how many students
    while True:
        try:
            num_students = int(input("How many students to process? ").strip())
            if num_students >= 0:
                break
            else:
                print("Please enter a non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Process each student
    for i in range(num_students):
        print(f"\n--- Processing Student {i+1} of {num_students} ---")
        name, scores, average, letter = process_student()
        display_report(name, scores, average, letter)
        
        # Store average for class average calculation
        class_scores.append(average)
        
    # Calculate class average
    if class_scores:
        class_average = sum(class_scores) / len(class_scores)
        print("\n=== Class Summary ===")
        print(f"Total students processed: {len(class_scores)}")
        print(f"Class Average Score: {class_average:.2f}")
        print("=====================\n")

# -------------------------------------------------------------

# --- Problem 3: Shopping List Manager (20 points + 10 bonus) ---
# Fix and improve poorly designed code into a modular system.

def validate_price(price_str):
    """
    Helper: Validate that string is a valid non-negative price.
    Returns True/False.
    """
    try:
        price = float(price_str)
        # Price must be non-negative
        return price >= 0
    except ValueError:
        return False

def get_item_and_price():
    """
    Gets item name and validated price from the user.
    Uses validate_price helper.
    Returns (item, price) or ('done', None) to stop.
    """
    while True:
        item = input("Item (or done): ").strip()
        
        if item.lower() == "done":
            return 'done', None # Signal to stop collection

        while True:
            price_str = input("Price: ").strip()
            # Add validation helper for prices
            if validate_price(price_str):
                return item, float(price_str)
            else:
                print("Invalid price. Please enter a non-negative number.")

def collect_list_items():
    """
    Collects item names and prices from the user into a list of tuples.
    Returns a list of (item, price) tuples.
    """
    shopping_list = [] 
    
    while True:
        # Use helper function
        item, price = get_item_and_price()
        
        if item == 'done':
            break
            
        shopping_list.append((item, price))
        
    return shopping_list

def calculate_total(shopping_list):
    """
    Calculates the total cost and applies a 10% discount if total > $50.
    Returns (original_total, discount, final_total).
    """
    prices = [price for _, price in shopping_list]
    
    # Use built-in function sum()
    original_total = sum(prices)
    discount = 0.0
    final_total = original_total

    if original_total > 50:
        discount = original_total * 0.1 # Calculate 10% discount
        final_total = original_total - discount # Apply discount
        
    return original_total, discount, final_total

def display_shopping_report(shopping_list, original_total, discount, final_total):
    """
    Displays the formatted shopping list and total/discount report.
    """
    print("\n--- Shopping List ---")
    if not shopping_list:
        print("List is empty.")
        return

    for item, price in shopping_list:
        # Improve output formatting and use round() implicitly via f-string formatting
        print(f"{item}: ${price:.2f}")

    print("---------------------")
    print(f"Total: ${original_total:.2f}") # Display original total
    
    if discount > 0:
        print(f"10% discount: -${discount:.2f}") # Display discount
        print(f"Final Total: ${final_total:.2f}") # Display final total
    print("---------------------\n")


# Optional Bonus Functions (10 points)
def save_list_to_file(shopping_list, filename="shopping_list.txt"):
    """Saves the shopping list to a file."""
    try:
        with open(filename, 'w') as f:
            for item, price in shopping_list:
                f.write(f"{item},{price}\n")
        print(f"List saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def load_list_from_file(filename="shopping_list.txt"):
    """Loads the shopping list from a file."""
    loaded_list = []
    try:
        with open(filename, 'r') as f:
            for line in f:
                item, price_str = line.strip().split(',')
                if validate_price(price_str):
                    loaded_list.append((item, float(price_str)))
                else:
                    print(f"Skipping invalid price entry: {line.strip()}")
        print(f"List loaded from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"Error loading file: {e}")
    return loaded_list

def problem_3_main():
    """Main program for the Shopping List Manager."""
    print("=== Shopping List Manager ===")
    
    # shopping_list = load_list_from_file() # Uncomment to use bonus load function
    shopping_list = []
    
    # 1. Collect items
    shopping_list = collect_list_items()
    
    if not shopping_list:
        print("Shopping list is empty.")
        return

    # 2. Calculate totals
    original_total, discount, final_total = calculate_total(shopping_list)
    
    # 3. Display report
    display_shopping_report(shopping_list, original_total, discount, final_total)
    
    # save_list_to_file(shopping_list) # Uncomment to use bonus save function

# -------------------------------------------------------------

# --- Main Driver Function ---

def main():
    """Driver function to run all problem solutions."""
    
    print("---------------------------------")
    print("Running Problem 1: Statistics Calculator")
    problem_1_main()
    
    print("---------------------------------")
    print("Running Problem 2: Grade Processing System")
    problem_2_main()
    
    print("---------------------------------")
    print("Running Problem 3: Shopping List Manager")
    problem_3_main()
    
    print("---------------------------------")
    print("Homework completed.")
    
# Standard way to call the main function
if __name__ == "__main__":
    main()

