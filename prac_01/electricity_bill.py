"""
CP1404/CP5632 - Practical
Electricity bill estimator 2.0 - with tariff selection
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff = input("Which tariff? 11 or 31: ")

if tariff == "11":
    cost_per_kwh = TARIFF_11
elif tariff == "31":
    cost_per_kwh = TARIFF_31
else:
    print("Invalid tariff selected!")
    exit()

daily_use_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

estimated_bill = cost_per_kwh * daily_use_kwh * billing_days

print(f"Estimated bill: ${estimated_bill:.2f}")
