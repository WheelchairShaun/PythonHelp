bulbasaur = 20
squirtle = 20

print()
print("Bulbasaur vs Squirtle")
print("=====================\n")

round = 1

while True:
    print("Round ", round, "!\n", sep="")

    print("Bulbasaur attacks Squirtle for 6 damage!")
    squirtle = squirtle - 6

    print("Squirtle attacks Bulbasaur for 4 damage!")
    bulbasaur = bulbasaur - 4

    round = round + 1

    print()

    if (bulbasaur <= 0 or squirtle <= 0):
        break

    input("Press Enter to continue...\n")

if (bulbasaur <= 0):
    print("Squirtle wins!")
elif(squirtle <= 0):
    print("Bulbasaur wins!")

print()
