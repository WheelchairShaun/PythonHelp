import locale
locale.setlocale(locale.LC_ALL, "")

#  Dictionary
apples = {
    "Fuji Apples" : 0.94,
    "Honeycrisp Apples" : 1.54,
    "Gala Apples" : 0.84,
    "Envy Apples" : 1.60,
    "Red Delicious Apples" : 1.00,
    "Granny Smith Apples" : 1.06,
    "Pink Lady Apples" : 0.99,
    "Jazz Apples" : 0.99,
    "Cosmic Crisp Apples" : 1.18,
    "Opal Apples" : 0.87,
    "SugarBee Apples" : 2.27,
    "Golden Delicious Apples" : 1.24
}

# 2D List
items = [[0 for i in range(4)] for j in range(12)]

# Items count
counter = 0

# Print price list
print("="*68)
print("                     Today's Apple Prices", end="\n\n")
print("*"*68)

for apple in apples:
    print("{:24s} :   $ {:4}".format(apple, locale.currency(apples[apple], symbol=False)))

print("*"*68, end="\n\n\n")

print("Please enter your selection (-1 when done):")

# While loop input
while (True):
    a = input("Enter Apple Name: ")

    # Check for -1
    if (a == "-1"):
        break

    p = float(input("Enter Price: $"))

    w = int(input("Enter Weight: "))

    # Check weight is greater than zero
    if (w <= 0):
        print("Weight must be greater than zero. Please try again.", end="\n\n")
        continue
    
    items[counter] = [a, locale.currency(p, symbol=False), str(w), locale.currency(p * w, symbol=False)]
    counter = counter + 1

    print()

print("\n")

print("                     Grocery Store Receipt")
print("="*68, end="\n\n")
print("-"*25, "Your items", "-"*33, sep="", end="\n\n")

print("{:14s} {:15s} {:13s} {:16s}".format("Apple Name", "Price($)", "Weight(lbs)",  "Item Subtotal($)"))

for i in range(counter):
    for j in range(4):
        print("{:17s}".format(items[i][j]), end="")

    print()

print("\n\n")

# Calculate uubtotal
subtotal = 0

for i in range(counter):
    subtotal = subtotal + float(items[i][3])

# Calculate tax
tax = subtotal * 0.065

# Calculate total
total = subtotal + tax

# Display subtotal, tax, and total
print("Subtotal:            $ ", locale.currency(subtotal, symbol=False), sep="")
print("Tax:                 $ ", locale.currency(tax, symbol=False), sep="")
print("The total amount is: $ ", locale.currency(total, symbol=False), sep="", end="\n\n\n")

print("-"*20, "Thank you for your business!", "-"*20, sep="", end="\n\n")