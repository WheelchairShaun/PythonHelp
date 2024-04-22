# M Shape

for line in range(1, 10):
    for stars in range(0, line):
        print("*", end="")
    
    for spaces in range(9 - line, 0, -1):
        print(" ", end=" ")

    for stars in range(0, line):
        print("*", end="")
    
    print()

print("\n")

# Smallest number
print("Use while to find out the smallest number (user can enter as many numbers as they want, -1 is used to stop the entry)")

smallest = int(input("Enter a number (-1 is used to stop the program): "))

while (True):
    n = int(input("Enter a number: "))

    if (n == -1):
        break
    
    if (n < smallest):
        smallest = n

print()

print("The smallest number is", smallest, end="\n\n")
