# String formatting examples
name = "Gibson L-5 CES"
year = 1922
cost = 16035.99
print(f"{year} {name} for about ${cost:,.0f}!")

# Power of 2 output using loop
for i in range(11):
    print(f"2 ^ {i:>2} is {2 ** i:>5}")
