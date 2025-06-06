import random

# Run these multiple times to observe outputs
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# Answers as comments:
# Line 1: Smallest = 5, Largest = 20
# Line 2: Possible values = 3, 5, 7, 9; Smallest = 3, Largest = 9; No, it can't be 4 (step is 2)
# Line 3: Smallest ≈ 2.5, Largest ≈ 5.5 (float within range)

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)
