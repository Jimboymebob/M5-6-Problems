quantity = float(input("Enter quantity of item: "))

if quantity >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

extended_price = quantity * unit_price

tax = extended_price * 0.07

total = extended_price + tax

print("\n----- Invoice -----")
print(f"{'Quantity:':<20}{quantity:>10.2f}")
print(f"{'Unit Price:':<20}${unit_price:>9.2f}")
print(f"{'Extended Price:':<20}${extended_price:>9.2f}")
print(f"{'Tax (7%):':<20}${tax:>9.2f}")
print(f"{'Total:':<20}${total:>9.2f}")
