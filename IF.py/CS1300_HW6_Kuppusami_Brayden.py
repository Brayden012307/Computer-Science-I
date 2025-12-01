"""
CS 1300 - Homework #6
Name: Your Name
Date: Submission Date
Description: Introduction to Lists
"""

# ==============================================================================
# Part 1: List Creation Basics (15 points)
# ==============================================================================
print("="*50)
print("PART 1: LIST CREATION")
print("="*50)

# Problem 1.1: Your First Lists (5 points)
print("\n--- Problem 1.1 ---")
example_colors = ["red", "blue", "green"]
print("Example:", example_colors)

my_classes = ["CS 1300", "Calculus I", "Physics", "English Comp"]
my_grades = [92, 85, 95, 78, 100]
my_notes = []
print("my_classes:", my_classes)
print("my_grades:", my_grades)
print("my_notes:", my_notes)


# Problem 1.2: Different Types in Lists (5 points)
print("\n--- Problem 1.2 ---")
about_me = ["Gemini", 1, 5.9, True]
mixed_bag = [42, "Hello", 3.14, [1, 2, 3]]
print("about_me:", about_me)
print("mixed_bag:", mixed_bag)


# Problem 1.3: Creating Lists Different Ways (5 points)
print("\n--- Problem 1.3 ---")
zeros = [0] * 10
print("List of 10 zeros:", zeros)

letters = list("HELLO")
print("String converted to list:", letters)

pattern = [1, 2] * 3
print("Repeating pattern list:", pattern)


# ==============================================================================
# Part 2: Accessing List Elements (20 points)
# ==============================================================================
print("\n"+"="*50)
print("PART 2: ACCESSING LIST ELEMENTS")
print("="*50)

# Problem 2.1: Reading from Lists (7 points)
print("\n--- Problem 2.1 ---")
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print("The list:", months)
print("List length:", len(months))

print("1. First month:", months[0])
print("2. Sixth month:", months[5])
print("3. Last month (pos index):", months[len(months) - 1])
print("4. Last month (neg index):", months[-1])
print("5. December (pos index):", months[11])
print("6. January (neg index):", months[-12])
print("7. Month at index 7:", months[7])


# Problem 2.2: Modifying List Elements (7 points)
print("\n--- Problem 2.2 ---")
temperatures = [72, 75, 71, 73, 74, 76, 70]
print("Original temperatures:", temperatures)

temperatures[1] = 77
temperatures[5] = 78
temperatures[0] = 74
temperatures[-1] = 72
temperatures[3] = 75

print("Corrected temperatures:", temperatures)
print("6. Number of days:", len(temperatures))
print("7. Index of the last day:", len(temperatures) - 1)


# Problem 2.3: Index Errors and Safety (6 points)
print("\n--- Problem 2.3 ---")
colors = ["red", "blue", "green"]
print("Colors:", colors)

if 1 < len(colors):
    print("Color at index 1:", colors[1])
else:
    print("Index 1 doesn't exist")

index_to_check = 5
if index_to_check < len(colors):
    print(f"Color at index {index_to_check}:", colors[index_to_check])
else:
    print(f"2. Index {index_to_check} doesn't exist.")

if len(colors) > 0:
    print("3. First element:", colors[0])
else:
    print("3. List is empty, cannot access the first element.")

if len(colors) >= 1:
    print("4. Last element safely accessed:", colors[-1])
else:
    print("4. List is empty, cannot access the last element.")

index_to_try = 4
if index_to_try < len(colors):
    print(f"5. Element at index {index_to_try}:", colors[index_to_try])
else:
    print(f"5. Index {index_to_try} is invalid.")

smallest_neg_index = -len(colors)
print("6. Smallest valid negative index:", smallest_neg_index)


# ==============================================================================
# Part 3: List Slicing (20 points)
# ==============================================================================
print("\n"+"="*50)
print("PART 3: LIST SLICING")
print("="*50)

# Problem 3.1: Basic Slicing (7 points)
print("\n--- Problem 3.1 ---")
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original list:", numbers)
print("Remember: list[start:end] gives elements from start up to (but not including) end")

print("Example numbers[0:3]:", numbers[0:3])

print("1. First 4 numbers (numbers[:4]):", numbers[:4])
print("2. Last 3 numbers (numbers[-3:]):", numbers[-3:])
print("3. Index 2 to 6 (numbers[2:7]):", numbers[2:7])
print("4. Index 5 to end (numbers[5:]):", numbers[5:])
print("5. Start up to index 4 (numbers[:4]):", numbers[:4])
copy_of_numbers = numbers[:]
print("6. Complete copy (numbers[:]):", copy_of_numbers)
print("7. Empty slice (numbers[3:3]):", numbers[3:3])


# Problem 3.2: Slicing with Steps (7 points)
print("\n--- Problem 3.2 ---")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
print("Alphabet:", alphabet)

print("Every other letter:", alphabet[::2])

print("1. Every third letter:", alphabet[::3])
print("2. Every other from 'b':", alphabet[1::2])
print("3. Reversed list:", alphabet[::-1])
middle_index = len(alphabet) // 2
print("4. First half:", alphabet[:middle_index])
print("5. Second half:", alphabet[middle_index:])
print("6. Index 2 to 8, step 2 (alphabet[2:9:2]):", alphabet[2:9:2])
print("7. First 5 letters reversed:", alphabet[:5][::-1])


# Problem 3.3: Practical Slicing Applications (6 points)
print("\n--- Problem 3.3 ---")
hourly_temps = [55, 54, 53, 52, 52, 54, 58, 62, 66, 70, 73, 75,
                76, 77, 77, 76, 74, 71, 68, 65, 62, 59, 57, 55]
print(f"24-hour temperature data ({len(hourly_temps)} readings)")

print("1. Morning temps (12am-5am):", hourly_temps[:6])
print("2. Afternoon temps (12pm-5pm):", hourly_temps[12:18])
print("3. Evening temps (6pm-11pm):", hourly_temps[-6:])
print("4. Every other hour:", hourly_temps[::2])
print("5. Middle 4 hours (10-13):", hourly_temps[10:14])
print("6. Temps for 6am-9am:", hourly_temps[6:10])


# ==============================================================================
# Part 4: List Methods - Adding Items (15 points)
# ==============================================================================
print("\n"+"="*50)
print("PART 4: ADDING ITEMS")
print("="*50)

# Problem 4.1: Using append() (5 points)
print("\n--- Problem 4.1 ---")
shopping_list = []
print("Starting with empty list:", shopping_list)

shopping_list.append("milk")
shopping_list.append("bread")
shopping_list.append("eggs")
shopping_list.append("cheese")
shopping_list.append("apples")

print("Final shopping list:", shopping_list)

print("6. If you try to append two items at once, you get a TypeError because append() takes exactly one argument.")

favorites = []
favorites.append("pasta")
favorites.append("tacos")
favorites.append("ice cream")
print("My favorites:", favorites)


# Problem 4.2: Using insert() (5 points)
print("\n--- Problem 4.2 ---")
line = ["Alice", "Bob", "Charlie"]
print("Original line:", line)

line.insert(0, "David")
print("After David cuts:", line)

line.insert(2, "Eve")
print("After Eve joins:", line)

line.insert(len(line), "Frank")
print("Final line:", line)

schedule = ["Math", "History", "Science"]
print("\nOriginal schedule:", schedule)

schedule.insert(2, "Lunch")
schedule.insert(0, "Homeroom")

print("Updated schedule:", schedule)


# Problem 4.3: Using extend() (5 points)
print("\n--- Problem 4.3 ---")
primary_colors = ["red", "blue", "yellow"]
print("Primary colors:", primary_colors)

secondary_colors = ["green", "orange", "purple"]
primary_colors.extend(secondary_colors)
print("All colors:", primary_colors)

list1= [1, 2, 3]
list2= [1, 2, 3]

list1.append([4, 5])
print("After append([4, 5]):", list1)

list2.extend([4, 5])
print("After extend([4, 5]):", list2)

my_list_append = ["a", "b"]
my_list_extend = ["a", "b"]
my_list_append.append(["c", "d"])
my_list_extend.extend(["c", "d"])
print("5. Custom Append:", my_list_append)
print("5. Custom Extend:", my_list_extend)


# ==============================================================================
# Part 5: List Methods - Removing Items (15 points)
# ==============================================================================
print("\n"+"="*50)
print("PART 5: REMOVING ITEMS")
print("="*50)

# Problem 5.1: Using remove() (5 points)
print("\n--- Problem 5.1 ---")
pets = ["dog", "cat", "bird", "cat", "fish", "cat"]
print("Original pets:", pets)

pets.remove("bird")
print("1. After removing bird:", pets)

pets.remove("cat")
print("2. After removing one cat:", pets)

if "hamster" in pets:
    pets.remove("hamster")
else:
    print("3. hamster not found in list")

numbers = [5, 3, 8, 3, 9, 3, 2]
print("\nNumbers:", numbers)

if 3 in numbers:
    numbers.remove(3)
    print("5. Removed first 3:", numbers)

if 3 in numbers:
    numbers.remove(3)
    print("5. Removed second 3:", numbers)

if 3 in numbers:
    numbers.remove(3)
    print("5. Removed third 3:", numbers)

if 3 in numbers:
    numbers.remove(3)
    print("5. Removed final 3:", numbers)
else:
    print("5. No more 3's to remove.")


# Problem 5.2: Using pop() (5 points)
print("\n--- Problem 5.2 ---")
stack = [10, 20, 30, 40, 50]
print("Original stack:", stack)

last_item = stack.pop()
print(f"1. Popped (last_item = {last_item}), stack is now: {stack}")

first_item = stack.pop(0)
print(f"2. Popped (first_item = {first_item}), stack is now: {stack}")

popped_at_index_1 = stack.pop(1)
print("3. Item popped at index 1:", popped_at_index_1)
print("Current stack:", stack)

queue = ["Person1", "Person2", "Person3", "Person4"]
print("\nQueue:", queue)

served_person = queue.pop(0)
print("4. Served:", served_person)

queue.pop()
print("Remaining queue:", queue)


# Problem 5.3: Using del and clear() (5 points)
print("\n--- Problem 5.3 ---")
data = [100, 200, 300, 400, 500, 600, 700]
print("Original data:", data)

del data[0]
print("1. After deleting first:", data)

del data[2]
print("2. After deleting index 2:", data)

del data[1:3]
print("3. After deleting slice:", data)

readings = [0, 5, 999, 10, 15, 999, 20]
print("\nReadings with errors:", readings)

if 999 in readings:
    readings.remove(999)
print("4. Removed first 999:", readings)

if 999 in readings:
    readings.remove(999)

print("5. Clean readings:", readings)


# ==============================================================================
# Part 6: Membership and Length Operations (15 points)
# ==============================================================================
print("\n"+"="*50)
print("PART 6: MEMBERSHIP AND LENGTH")
print("="*50)

# Problem 6.1: Using 'in' and 'not in' (8 points)
print("\n--- Problem 6.1 ---")
valid_grades = ['A', 'B', 'C', 'D', 'F']
print("Valid grades:", valid_grades)

print("1. Is 'B' valid?", 'B' in valid_grades)

print("2. Is 'E' NOT valid?", 'E' not in valid_grades)

user_grade = 'C'
if user_grade in valid_grades:
    print(f"3. Grade '{user_grade}' is VALID.")
else:
    print(f"3. Grade '{user_grade}' is NOT VALID.")

menu_options = [1, 2, 3, 4, 5]
print("\nMenu options:", menu_options)

print("4. Is option 3 available?", 3 in menu_options)

print("5. Is option 9 NOT available?", 9 not in menu_options)

enrolled = ["Alice", "Bob", "Charlie", "Diana"]
print("\nEnrolled students:", enrolled)

if "Eve" not in enrolled:
    print("6. Eve needs to be added (not enrolled).")
else:
    print("6. Eve is already enrolled.")

frank = "Frank"
if frank not in enrolled:
    enrolled.append(frank)
    print(f"7. {frank} added. Enrolled list:", enrolled)
else:
    print(f"7. {frank} is already enrolled. Enrolled list:", enrolled)

to_check = ["Alice", "Eve", "Bob", "George"]
print("\n8. Checking student enrollment:")
print(f"Is {to_check[0]} enrolled?", to_check[0] in enrolled)
print(f"Is {to_check[1]} enrolled?", to_check[1] in enrolled)
print(f"Is {to_check[2]} enrolled?", to_check[2] in enrolled)
print(f"Is {to_check[3]} enrolled?", to_check[3] in enrolled)


# Problem 6.2: Using len() and List Size (7 points)
print("\n--- Problem 6.2 ---")
tasks = ["homework", "dishes", "laundry", "shopping", "exercise"]
print("Tasks:", tasks)

num_tasks = len(tasks)
print("1. Number of tasks:", num_tasks)

last_index = len(tasks) - 1
print("2. Index of the last task:", last_index)

if len(tasks) > 3:
    print("3. Yes, the list has more than 3 tasks.")
else:
    print("3. No, the list has 3 or fewer tasks.")

middle_index_val = len(tasks) // 2
print("4. Middle index:", middle_index_val)

if len(tasks) > 0:
    middle_task = tasks[middle_index_val]
    print("5. Middle task:", middle_task)
else:
    print("5. Cannot access middle task, list is empty.")

inbox = []
print("\nInbox:", inbox)

if len(inbox) == 0:
    print("6. Way 1: Inbox is empty (using len() == 0)")

if not inbox:
    print("6. Way 2: Inbox is empty (using 'not inbox')")

waiting = ["P1", "P2"]
max_capacity = 4
print(f"\nWaiting list ({len(waiting)}/{max_capacity}):", waiting)

spaces_available = max_capacity - len(waiting)
print(f"Spaces available: {spaces_available}")

if len(waiting) < max_capacity:
    waiting.append("P3")
if len(waiting) < max_capacity:
    waiting.append("P4")

print(f"Updated waiting list ({len(waiting)}/{max_capacity}):", waiting)


# ==============================================================================
# Challenge Problem (Bonus: 10 points)
# ==============================================================================
print("\n"+"="*50)
print("CHALLENGE PROBLEM: INVENTORY SYSTEM")
print("="*50)

inventory = ["apples", "bananas", "milk", "bread", "eggs"]
quantities = [10, 15, 5, 8, 24]

print("=== Store Inventory System ===")
print("Items:", inventory)
print("Quantities:", quantities)
print()

# Task 1: Display the inventory nicely
print("Current Inventory:")
print(f"  {inventory[0]}: {quantities[0]}")
print(f"  {inventory[1]}: {quantities[1]}")
print(f"  {inventory[2]}: {quantities[2]}")
print(f"  {inventory[3]}: {quantities[3]}")
print(f"  {inventory[4]}: {quantities[4]}")

# Task 2: A customer buys 3 apples
apples_index = 0
quantities[apples_index] = quantities[apples_index] - 3
print("\nTask 2: 3 apples sold.")

# Task 3: Restock milk
milk_index = 2
quantities[milk_index] = quantities[milk_index] + 10
print("Task 3: Milk restocked by 10.")

# Task 4: Add a new item
inventory.append("cheese")
quantities.append(12)
print("Task 4: Cheese added to inventory.")

# Task 5: Remove items with 0 quantity
print("\nTask 5: Removing items with 0 or less quantity.")

# Checking in reverse order (safer when deleting without a loop): Index 5, 4, 3, 2, 1, 0
if quantities[5] <= 0:
    del inventory[5]
    del quantities[5]
    print("  Removed item at index 5.")

if quantities[4] <= 0:
    del inventory[4]
    del quantities[4]
    print("  Removed item at index 4.")

if quantities[3] <= 0:
    del inventory[3]
    del quantities[3]
    print("  Removed item at index 3.")

if quantities[2] <= 0:
    del inventory[2]
    del quantities[2]
    print("  Removed item at index 2.")

if quantities[1] <= 0:
    del inventory[1]
    del quantities[1]
    print("  Removed item at index 1.")

if quantities[0] <= 0:
    del inventory[0]
    del quantities[0]
    print("  Removed item at index 0.")

# Task 6: Report
print("\nTask 6: Report")

print("Total number of different items:", len(inventory))

print("Items that need restocking (quantity < 5):")

current_length = len(inventory)

if current_length > 0 and quantities[0] < 5:
    print(f"  {inventory[0]}")
if current_length > 1 and quantities[1] < 5:
    print(f"  {inventory[1]}")
if current_length > 2 and quantities[2] < 5:
    print(f"  {inventory[2]}")
if current_length > 3 and quantities[3] < 5:
    print(f"  {inventory[3]}")
if current_length > 4 and quantities[4] < 5:
    print(f"  {inventory[4]}")
if current_length > 5 and quantities[5] < 5:
    print(f"  {inventory[5]}")

print("\nFinal Inventory:")
print("Items:", inventory)
print("Quantities:", quantities)

print("="*50)
print("END OF HOMEWORK")
print("="*50)

