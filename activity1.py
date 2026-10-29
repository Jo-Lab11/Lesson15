def calculate_change(paid, price):
    return (paid - price)

snack_price = 25
print("===== SNAK VENDING MACHINE =====")
print("Snack Price:", snack_price)
print("Accepted coins: 1, 5, 10, 25")

total = 0
count = 0
while total < snack_price:
    coin = int(input("Insert coin (1, 5, 10,25): "))

    if coin not in [1, 5, 10, 25]:
        print("Invalid coin!")
        continue
    total += coin
    count += 1
    print("Total inserted:", total)
change = calculate_change(total, snack_price)

print("\nDispensing your snack...")
if change > 0:
    print("Change:", change)
else:
    pass
print("\n ===== PURCHASE SUMMARY =====")
print("Snack Price:", snack_price)
print("Coins Insered:", count)
print("Total Paid:", total)
print("Change Given:", change)
print("Thanks for your purchase!")