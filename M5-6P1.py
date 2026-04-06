qty = int(input("Enter quantity: "))
if qty >= 1000:
    price = 3.00
else:
    price = 5.00
extended = qty * price
tax = extended * 0.07
total = extended + tax
print("\n--- Invoice ---")
print(f"{'Quantity:':<20}{qty:<10}")
print(f"{'Unit Price:':<20}${price:9.2f}")
print(f"{'Extended Price:':<20}${extended:9.2f}")
print(f"{'Tax:':<20}${tax:9.2f}")
print(f"{'Total:':<20}${total:9.2f}")
