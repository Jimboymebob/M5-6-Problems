tickets = int(input("Enter number of tickets: "))

if tickets >= 25:
    price = 50
elif tickets >= 10:
    price = 60
elif tickets >= 5:
    price = 70
else:
    price = 75

total = tickets * price

print("\n--- Ticket Summary ---")
print(f"{'Tickets:':20}{tickets:10}")
print(f"{'Price per Ticket:':20}${price:9.2f}")
print(f"{'Total Cost:':20}${total:9.2f}")
