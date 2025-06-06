# Complete the program to safely get a valid integer from the user
valid_input = False
while not valid_input:
    try:
        result = int(input("Enter a valid integer: "))
        valid_input = True
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
print(f"You entered: {result}")
