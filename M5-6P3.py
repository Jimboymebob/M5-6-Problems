part = input("Enter part number: ")
qty = int(input("Enter quantity: "))

if part == "10" or part == "55":
    cost = 1.00
elif part == "99":
    cost = 2.00
elif part == "80" or part == "70":
    cost = 3.00
else:
    cost = 5.00

total = qty * cost

print("\n--- Part Cost ---")
print(f"{'Part Number:':20}{part:10}")
print(f"{'Unit Cost:':20}${cost:9.2f}")
print(f"{'Total Cost:':20}${total:9.2f}")
