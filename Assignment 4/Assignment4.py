# Receipt version 2

# Create variable subtotal to hold the sum of the prices
subtotal = 0

# User can enter as many prices as needed, create a variable "price"
# Using infinite while loop
while True:
    price = int(input("Enter the price of the items or enter -1 to end:"))

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
print('=' * 75)
print("Subtotal:", ' ' * 30, "${:.2f}\n".format(subtotal))
print("Tax:", ' ' * 35, "${:.2f}\n".format(tax))
print("Total:", ' ' * 33, "${:.2f}\n".format(total))
