# Even and Odd Numbers
from Function import *

evenCount = 0
oddCount = 0

counter = 0

while (counter < 5):
    num = int(input("Enter a number: "))

    if (CheckEvenOdd(num) == 1):
        evenCount += 1
    else:
        oddCount += 1
    
    counter += 1

print("Number of even numbers:", evenCount)
print("Number of odd numbers:", oddCount)
print()
