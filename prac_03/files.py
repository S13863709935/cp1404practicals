# Part 1: Get name and write to file
name = input("Enter your name: ")
with open("name.txt", "w") as name_file:
    name_file.write(name)

# Part 2: Read name from file and print greeting
with open("name.txt", "r") as name_file:
    name = name_file.read().strip()
    print(f"Hi {name}!")

# Part 3: Read and sum first two numbers from numbers.txt
with open("numbers.txt", "r") as numbers_file:
    number1 = int(numbers_file.readline())
    number2 = int(numbers_file.readline())
    print(number1 + number2)
