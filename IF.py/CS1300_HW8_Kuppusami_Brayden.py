
print("--- Problem 1: Multiplication Table Generator ---")

while True:
    try:
        table_size = int(input("Enter table size (1-12): "))
        
        if 1 <= table_size <= 12:
            break
        else:
            print("Invalid! Please enter a number between 1 and 12.")
    except ValueError:
        print("Invalid input. Please enter a whole number.")

CELL_WIDTH = 4
HEADER_WIDTH = 5
TABLE_WIDTH = HEADER_WIDTH + (table_size * CELL_WIDTH)
SEPARATOR = "=" * TABLE_WIDTH

print(f"\nMULTIPLICATION TABLE ({table_size}x{table_size})")
print(SEPARATOR)

header_row = f"{'X':>{HEADER_WIDTH-1}} |"

for col in range(1, table_size + 1):
    header_row += f"{col:>{CELL_WIDTH}}"
print(header_row)

print("-" * TABLE_WIDTH)

for row in range(1, table_size + 1):
    table_row = f"{row:>{HEADER_WIDTH-1}} |"

    for col in range(1, table_size + 1):
        result = row * col
        table_row += f"{result:>{CELL_WIDTH}}"
    
    print(table_row)

print(SEPARATOR)

print("\n" + "="*40)
print("--- Problem 2: Pattern Detective ---")

numbers = [23, 8, 45, 12, 78, 34, 67, 91, 15, 52, 41, 3]
print("\n=== PATTERN ANALYSIS ===")
print(f"Original numbers: {numbers}")

print("\n1. SEARCH PATTERN")
found_number = None
found_index = -1

for index, num in enumerate(numbers):
    if num > 75:
        found_number = num
        found_index = index
        break

if found_number is not None:
    print(f"First number > 75: {found_number} (at position {found_index})")
else:
    print("No number greater than 75 was found.")

print("\n2. FILTER PATTERN")
even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(f"Even numbers: {even_numbers}")

print("\n3. COUNTER PATTERN")
count_0_25 = 0
count_26_50 = 0
count_51_75 = 0
count_76_100 = 0

for num in numbers:
    if 0 <= num <= 25:
        count_0_25 += 1
    elif 26 <= num <= 50:
        count_26_50 += 1
    elif 51 <= num <= 75:
        count_51_75 += 1
    elif 76 <= num <= 100:
        count_76_100 += 1

print(f"Range 0-25: {count_0_25} numbers")
print(f"Range 26-50: {count_26_50} numbers")
print(f"Range 51-75: {count_51_75} numbers")
print(f"Range 76-100: {count_76_100} numbers")

print("\n4. ACCUMULATOR PATTERN")
sum_divisible_by_3 = 0
divisible_by_3_list = []

for num in numbers:
    if num % 3 == 0:
        sum_divisible_by_3 += num
        divisible_by_3_list.append(num)

print(f"Numbers divisible by 3: {divisible_by_3_list}")
print(f"Sum of these numbers: {sum_divisible_by_3}")

print("\n5. SENTINEL PATTERN")
updated_numbers = list(numbers)

print("Add more numbers (enter -1 to stop):")
while True:
    try:
        new_number = input("Enter number: ")
        
        if new_number == "-1":
            break
        
        num_to_add = int(new_number)
        
        updated_numbers.append(num_to_add)
    
    except ValueError:
        print("Invalid input. Please enter a whole number or -1 to stop.")

print(f"Updated list: {updated_numbers}")
print(f"New count: {len(updated_numbers)} numbers")
print("="*40)

print("\n" + "="*40)
print("--- Problem 3: Grade Report Generator (BONUS) ---")
print("=== GRADE REPORT SYSTEM ===")

students = ["Alice", "Bob", "Carol", "David", "Emma"]
assignments = ["HW1", "HW2", "Quiz1", "Exam1", "Quiz2"]
grades = [
    [92, 88, 95, 87, 90],
    [78, 82, 73, 85, 80],
    [95, 91, 98, 92, 94],
    [65, 70, 68, 72, 75],
    [88, 85, 82, 90, 87]
]
NUM_STUDENTS = len(students)
NUM_ASSIGNMENTS = len(assignments)
results = {}

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

student_averages = []
for i in range(NUM_STUDENTS):
    student_sum = sum(grades[i]) 
    student_avg = student_sum / NUM_ASSIGNMENTS
    student_averages.append(student_avg)
    
    results[students[i]] = {
        'average': student_avg,
        'grade': get_letter_grade(student_avg)
    }

print("\nGrade Table:")

NAME_WIDTH = 10
GRADE_WIDTH = 6
AVG_WIDTH = 8
LINE = "-" * (NAME_WIDTH + (NUM_ASSIGNMENTS * GRADE_WIDTH) + AVG_WIDTH + GRADE_WIDTH + 2)

header = f"{'Student':<{NAME_WIDTH}}"
for assign in assignments:
    header += f"{assign:>{GRADE_WIDTH}}"
header += f"{'AVG':>{AVG_WIDTH}}"
header += f"{'Grade':>{GRADE_WIDTH}}"
print(header)
print(LINE)

for i in range(NUM_STUDENTS):
    student_name = students[i]
    row = f"{student_name:<{NAME_WIDTH}}"
    
    for grade in grades[i]:
        row += f"{grade:>{GRADE_WIDTH}}"
    
    avg = results[student_name]['average']
    grade_letter = results[student_name]['grade']
    row += f"{avg:>{AVG_WIDTH}.1f}"
    row += f"{grade_letter:>{GRADE_WIDTH}}"
    print(row)
print(LINE)

print("\nAssignment Statistics:")

assignment_stats = []

for j in range(NUM_ASSIGNMENTS):
    assignment_sum = 0
    min_grade = 101
    max_grade = -1
    min_student_name = ""
    max_student_name = ""
    
    for i in range(NUM_STUDENTS):
        current_grade = grades[i][j]
        
        assignment_sum += current_grade
        
        if current_grade > max_grade:
            max_grade = current_grade
            max_student_name = students[i]
        
        if current_grade < min_grade:
            min_grade = current_grade
            min_student_name = students[i]
    
    class_avg = assignment_sum / NUM_STUDENTS

    assignment_stats.append({
        'name': assignments[j],
        'avg': class_avg,
        'max': (max_grade, max_student_name),
        'min': (min_grade, min_student_name)
    })

for stat in assignment_stats:
    print(f"{stat['name']:<5}: Class Avg: {stat['avg']:<5.1f} | Highest: {stat['max'][0]} ({stat['max'][1]:<5}) | Lowest: {stat['min'][0]} ({stat['min'][1]:<5})")

print("\nSpecial Recognition:") 
honor_roll = []
warning_list = []

for student, data in results.items():
    if data['average'] >= 90:
        honor_roll.append(student)
    elif data['average'] < 70:
        warning_list.append(student)

print(f"Honor Roll (90+ average): {', '.join(honor_roll) if honor_roll else 'None'}")
print(f"Academic Warning (<70 average): {', '.join(warning_list) if warning_list else 'None'}")

all_averages = student_averages
highest_avg = max(all_averages)
lowest_avg = min(all_averages)

highest_student = students[all_averages.index(highest_avg)]
lowest_student = students[all_averages.index(lowest_avg)]

overall_class_avg = sum(all_averages) / NUM_STUDENTS

print("\nClass Summary:") 
print(f"Highest Overall Average: {highest_student} ({highest_avg:.1f}%)")
print(f"Lowest Overall Average: {lowest_student} ({lowest_avg:.1f}%)")
print(f"Class Average: {overall_class_avg:.1f}%")

print("\nGrade Distribution:")

grade_a_count = 0
grade_b_count = 0
grade_c_count = 0
grade_d_count = 0
grade_f_count = 0

for avg in all_averages:
    if avg >= 90:
        grade_a_count += 1
    elif avg >= 80:
        grade_b_count += 1
    elif avg >= 70:
        grade_c_count += 1
    elif avg >= 60:
        grade_d_count += 1
    else:
        grade_f_count += 1

print(f"A (90-100): {grade_a_count} students")
print(f"B (80-89): {grade_b_count} student{'s' if grade_b_count != 1 else ''}")
print(f"C (70-79): {grade_c_count} student{'s' if grade_c_count != 1 else ''}")
print(f"D (60-69): {grade_d_count} student{'s' if grade_d_count != 1 else ''}")
print(f"F (0-59): {grade_f_count} student{'s' if grade_f_count != 1 else ''}")
print("="*40)

print("\n" + "="*40)
print("--- Bonus Challenge: Advanced Pattern Printer ---")

def print_diamond(size=5):
    print("\n--- Pattern 1: Diamond ---")
    
    for i in range(1, size + 1):
        print(" " * (size - i), end="")
        print("*" * (2 * i - 1))

    for i in range(size - 1, 0, -1):
        print(" " * (size - i), end="")
        print("*" * (2 * i - 1))

def print_hollow_square(size=5):
    print("\n--- Pattern 2: Hollow Square ---")
    
    for row in range(1, size + 1):
        output = ""
        for col in range(1, size + 1):
            if row == 1 or row == size or col == 1 or col == size:
                output += "*"
            else:
                output += " "
        print(output)

def print_number_pyramid(size=5):
    print("\n--- Pattern 3: Number Pyramid ---")
    
    for i in range(1, size + 1):
        output = ""
        for j in range(1, i + 1):
            output += str(i)
        print(output)

while True:
    print("\nSelect a pattern to display (enter the number):")
    print("1. Diamond (Size 5)")
    print("2. Hollow Square (Size 5)")
    print("3. Number Pyramid (Size 5)")
    print("4. Display All Three")
    print("5. Exit Bonus Challenge")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == '1':
        print_diamond()
    elif choice == '2':
        print_hollow_square()
    elif choice == '3':
        print_number_pyramid()
    elif choice == '4':
        print_diamond()
        print_hollow_square()
        print_number_pyramid()
    elif choice == '5':
        print("\nExiting Bonus Challenge. Good luck with your submission!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

print("="*40)


