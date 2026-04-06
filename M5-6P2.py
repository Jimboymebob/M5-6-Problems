qty = int(input("Enter quantity of widgets: "))

if qty > 10000:
    price = 10
elif qty >= 5000:
    price = 20
else:
    price = 30

extended = qty * price
tax = extended * 0.07
total = extended + tax

print("\n--- Widget Cost ---")
print(f"{'Extended Price:':20}${extended:9.2f}")
print(f"{'Tax:':20}${tax:9.2f}")
print(f"{'Total:':20}${total:9.2f}")
