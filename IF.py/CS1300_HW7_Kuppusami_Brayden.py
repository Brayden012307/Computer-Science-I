
def temperature_analyzer():
    print("\nTemperature Analysis Report")
    print("=============================")

    temperatures = [72, 68, 75, 71, 69, 77, 74, 70, 73, 76]

    temp_sum = 0
    highest_temp = temperatures[0]
    lowest_temp = temperatures[0]
    days_above_72 = 0
    
    for i, fahrenheit in enumerate(temperatures):
        temp_sum += fahrenheit
        
        if fahrenheit > highest_temp:
            highest_temp = fahrenheit
            
        if fahrenheit < lowest_temp:
            lowest_temp = fahrenheit
            
        if fahrenheit > 72:
            days_above_72 += 1
            
        celsius = (fahrenheit - 32) * 5/9 
        
        celsius_rounded = round(celsius, 1)
        
        print(f"Day {i + 1}: {fahrenheit}°F ({celsius_rounded}°C)")

    average_temp = temp_sum / len(temperatures)
    average_temp_rounded = round(average_temp, 1)

    print("\nStatistics:")
    print("Average Temperature: {}°F".format(average_temp_rounded))
    print(f"Highest Temperature: {highest_temp}°F")
    print(f"Lowest Temperature: {lowest_temp}°F")
    print(f"Days Above 72°F: {days_above_72} days")

def guessing_game():
    print("\n=== NUMBER GUESSING GAME ===")

    secret_number = random.randint(1, 20)
    
    max_guesses = 5
    guesses = []

    print("I'm thinking of a number between 1 and 20.")
    print(f"You have {max_guesses} guesses!")

    for attempt in range(max_guesses):
        try:
            guess = int(input(f"Guess {attempt + 1}: "))
            guesses.append(guess)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess == secret_number:
            break
        elif guess < secret_number:
            print("Too low! Try higher.")
        else:
            print("Too high! Try lower.")
    
    
    
    else: 
        print("\nSorry! You've run out of guesses.")
        print(f"The number was {secret_number}.")
        print("Better luck next time!")

    guesses_used = len(guesses)   
    
    if  guesses_used > 0 and guesses[-1] == secret_number:
        print(f"\nCorrect! You got it in {guesses_used} guesses!")
        
        if guesses_used == 1:
            print("Amazing! You're a mind reader!")
        elif 2 <= guesses_used <= 3:
            print("Great job!")
        else:
            print("Good work!")
            
    print(f"Your guesses were: {guesses}")

def grade_processor():
    print("\nProcessing Grades...")
    print("==================")

    grades = [85, 10, 92, 150, 78, 0, 95, 88, 5, 100, 73, 200]
    
    total_valid_grades = 0
    total_valid_sum = 0
    invalid_count = 0
    
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0

    for grade in grades:
        if grade < 0 or grade > 100:
            invalid_count += 1
            print(f"Skipping invalid grade: {grade}")
            continue

        total_valid_grades += 1
        total_valid_sum += grade
        
        if grade >= 90:
            letter_grade = "A"
            a_count += 1
        elif grade >= 80:
            letter_grade = "B"
            b_count += 1
        elif grade >= 70:
            letter_grade = "C"
            c_count += 1
        elif grade >= 60:
            letter_grade = "D"
            d_count += 1
        else:
            letter_grade = "F"
            f_count += 1
            
        print(f"Grade {total_valid_grades}: {grade} ({letter_grade})")

    print("\nSummary Report")
    print("==============")
    
    print(f"Total valid grades processed: {total_valid_grades}")
    print(f"Invalid grades skipped: {invalid_count}")

    class_average = 0
    if total_valid_grades > 0:
        class_average = total_valid_sum / total_valid_grades
    
    print("\nGrade Distribution:")
    print(f"A: {a_count} students")
    print(f"B: {b_count} students")
    print(f"C: {c_count} students")
    print(f"D: {d_count} students")
    print(f"F: {f_count} student")

    print(f"Class Average: {round(class_average, 1)}")

if __name__ == "__main__":
    temperature_analyzer()
    guessing_game()
    grade_processor()