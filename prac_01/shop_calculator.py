"""
CP1404/CP5632 - Practical
Shop Calculator Program
Calculate total price of items with a 10% discount if total exceeds $100.
"""

DISCOUNT_THRESHOLD = 100  # dollars
DISCOUNT_RATE = 0.1       # 10%

# Get valid number of items
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

# Accumulate total price
total_price = 0
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total_price += price

# Apply discount if necessary
if total_price > DISCOUNT_THRESHOLD:
    total_price *= (1 - DISCOUNT_RATE)

# Display result
print(f"Total price for {number_of_items} items is ${total_price:.2f}")
