principal = float(input("Enter principal amount: "))
years = int(input("Enter years to maturity: "))

if principal > 100000 and years == 5:
    rate = 0.06
elif 50000 <= principal <= 100000 and years == 10:
    rate = 0.05
elif 50000 <= principal <= 100000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principal * rate

print("\n--- CD Interest ---")
print(f"{'Principal:':20}${principal:9.2f}")
print(f"{'Interest Rate:':20}{rate*100:9.2f}%")
print(f"{'Interest:':20}${interest:9.2f}")
