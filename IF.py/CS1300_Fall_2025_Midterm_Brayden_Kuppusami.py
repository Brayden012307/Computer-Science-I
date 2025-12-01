print("==================================")
print("- - - - - - Problem 1 - - - - - -")

Full_name = "John Michael Smith"
email = "john.smith@university.edu"
phone = "555-123-4567"

print(Full_name.split()[0])

print(Full_name.split()[-1])

initials = Full_name.split()[0][0] + "." + Full_name.split()[1][0] + "." + Full_name.split()[2][0]
print(initials)

is_uni = "university" in email.lower()
print(is_uni)

print(phone.replace("-", " "))

print("==================================")

print("- - - - - - Problem 3 - - - - - -")

numbers = [3, 5, 4 , 3, 2, 1, 3] 
print(f"3.1 numbers: {numbers}")

numbers.append(4)
print(f"3.2 numbers: {numbers}")

numbers[2] = 3
print(f"3.3 numbers: {numbers}")

numbers.remove(1)
print(f"3.4 numbers: {numbers}")

numbers.insert(1, 3)
print(f"3.5 numbers: {numbers}")

sublist = numbers[0:3]
print(f"3.6 sublist: {sublist}")

print(f"3.7 How many: {len(numbers)}")
print(f"3.7 First: {numbers[0]}")
print(f"3.7 Last: {numbers[-1]}")

print("==================================")





