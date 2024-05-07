numbers = []

print("Enter 5 Numbers:")
for i in range(1, 6):
    num = int(input("Enter number " + str(i) + ": "))
    numbers.append(num)

avg = sum(numbers) / len(numbers)

print("Average is", avg)
print()
