# Receipt version 2

# Create variable subtotal to hold the sum of the prices
subtotal = 0

# User can enter as many prices as needed, create a variable "price"
# Using infinite while loop
while True:
    price = float(input("Enter the price of the items or enter -1 to end:"))

    # Check price for -1
    if (price == -1):
        break
    else:
        subtotal = subtotal + price

# Create variables tax and total
tax = subtotal * 0.065

total = subtotal + tax

# Print receipt
print("                   Walmart Receipt")
print("============================================================")
print("Subtotal:                              $", format(subtotal, '.2f'))
print()
print("Tax:                                   $", format(tax, '.2f'))
print()
print("Total:                                 $", format(total, '.2f'))
