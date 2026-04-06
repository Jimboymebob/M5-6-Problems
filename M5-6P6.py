name = input("Enter employee last name: ")
salary = float(input("Enter salary: "))
level = int(input("Enter job level: "))

if level >= 10:
    rate = 0.25
elif level >= 5:
    rate = 0.20
else:
    rate = 0.10

bonus = salary * rate

print("\n--- Employee Bonus ---")
print(f"{'Employee:':20}{name:10}")
print(f"{'Bonus:':20}${bonus:9.2f}")
