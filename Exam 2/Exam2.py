# Mortgage program

# Ask user for loan amount  input
loanAmount = float(input("Enter loan amount from 50000 to 500000: "))

# Allow one more chance if loan amount is incorrect
if (loanAmount < 50000 or loanAmount > 500000):
    loanAmount = float(input("The amount is incorrect. Enter loan amount from 50000 to 500000: "))
    if (loanAmount < 50000 or loanAmount > 500000):
        print("The loan amount must be between 50000 and 500000.\nExiting program...\n")
        exit()

# Ask user for years
years = float(input("Enter how many years is the loan from 10 to 30: "))

# Allow one more chance if years is incorrect
if (years < 10 or years > 30):
    years = float(input("The years are incorrect. Enter how many years is the loan from 10 to 30: "))
    if (years < 10 or years > 30):
        print("The years must be between 10 and 30.\nExiting program...\n")
        exit()

# Ask user for interest
interest = float(input("Enter the interest rate from 3 to 6 percent: "))

# Allow one more chance if interest is incorrect
if (interest < 3 or interest > 6):
    interest = float(input("The interest is incorrect. Enter the interest rate from 3 to 6 percent: "))
    if (interest < 3 or interest > 6):
        print("The interest must be between 3 and 6.\nExiting program...\n")
        exit()

print()

# Calculate total amount of the loan
total = loanAmount * years * (1 + interest / 100)

print("Total Amount: $", format(total, ',.2f'))