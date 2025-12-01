print("=== CORNER STORE ===")

items = {
    1: ("Apple", 1.00),
    2: ("Banana", 0.50),
    3: ("Milk", 2.50),
    4: ("Bread", 2.00),
    5: ("Eggs (dozen)", 3.00)
}
print("\nAvailable Items:")
for key, (name, price) in items.items():
    print(f"{key}. {name} - ${price:.2f}")
    choice = int(input("\nEnter the number of the item you want to buy: "))
if choice not in items:
    print("Invalid choice. Exiting...")
    exit()
    item_name, item_price = items[choice]
    subtotal = item_price * quantity
discount = 0
if quantity >= 10:
    discount += 0.10
    is_member = input("Are you a store member? (yes/no): ").strip().lower()
if is_member == "yes":
    discount += 0.05
discount_amount = subtotal * discount
subtotal_after_discount = subtotal - discount_amount
tax = subtotal_after_discount * 0.08
total = subtotal_after_discount + tax
print("\n=== RECEIPT ===")
print(f"Item: {item_name}")
print(f"Unit Price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount_amount:.2f}")
print(f"Subtotal after discount: ${subtotal_after_discount:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"TOTAL: ${total:.2f}")
print("Thank you for shopping at Corner Store!")

