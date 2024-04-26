import locale

locale.setlocale(locale.LC_ALL, "")

prices = []

print("Type -1  after all prices have been entered to show receipt.\n")

while True:
    p = float(input("Enter a price: "))

    if (p == -1):
        break
    elif (p < 0):
        print("Prices must be greater than zero.")
    else:
        prices.append(p)

subtotal = sum(prices)
tax = subtotal * 0.06
total = subtotal + tax

print("\n\n\n")

print("                           Receipt V3")
print("--------------------------------------------------------------------------------")
print("\n\n")

for i in range(len(prices)):
    print("Item", i + 1, "\t\t\t\t\t\t\t\t", locale.currency(prices[i]))

print()

print("Tax:", "\t\t\t\t\t\t\t\t", locale.currency(tax))
print("Subtotal:", "\t\t\t\t\t\t\t", locale.currency(subtotal), end="\n\n")

print("Total:", "\t\t\t\t\t\t\t\t", locale.currency(total), end="\n\n")
