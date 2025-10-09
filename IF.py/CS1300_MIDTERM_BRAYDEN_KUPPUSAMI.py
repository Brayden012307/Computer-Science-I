student_id = "2025-CS-0342"
student_email = "SMITH.JANE@SCHOOL.EDU"
course_code = "CS1300-001"
print("- - - Proceesing Student ID - - -")

year = student_id[:4]
print("1.1 Year: " + year)

student_number = student_id[-4:]
print("1.2 Student Number: " + student_number)

username = student_email.lower().split('@')[0]
print("1.3 Username: " + username)

starts_with_cs = course_code.startswith("CS")
print("1.4 Starts with 'CS': " + str(starts_with_cs))

new_id = year + "_" + student_number
print("1.5 New ID Format: " + new_id)

print("==============================")
print("Problem 3: Inventory Management")
print("==============================")

products = ["laptop" , "keyboard" , "monitor" , "cable"]
print("3.1 Initial Inventory: " + str(products))

products.append("headphones")
print("3.2 After Add (append): " + str(products))

products.insert(3, "webcam")
print("3.3 After Insert (webcam at index 3): " + str(products))

products.remove("cable")
print("3.4 After Remove (cable): " + str(products))

index_of_keyboard = products.index("keyboard")
products[index_of_keyboard] = "wireless mouse"
print("3.5 After Replace (wireless mouse): " + str(products))

last_three = products[-3:]
print("3.6 Last 3 Items (slicing): " + str(last_three))

print("- - - 3.7 Final Display - - -")

print("Total products in stock: " + str(len(products)))

first_product_alpha = sorted(products)[0]
print("First product alphabetically: " + first_product_alpha)

even_index_products = [products[0], products[2], products[4]]
("Products at even indices: " + str(even_index_products))
print("- - - - - - - - - - - - - - - - - -")



