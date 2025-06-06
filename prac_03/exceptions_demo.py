try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"The result is: {result}")
print("Finished.")

# Answers as comments:
# ValueError occurs if input is not a valid integer (e.g., "abc")
# ZeroDivisionError occurs if denominator is 0
# Yes, you can avoid ZeroDivisionError by checking if denominator != 0 before division
