bulbasaur = 20
squirtle = 20

print()
print("Bulbasaur vs Squirtle")
print("=====================\n")

round = 1

while(bulbasaur > 0 and squirtle > 0):
    print("Round ", round, "!\n", sep="")

    print("Bulbasaur attacks Squirtle for 3 damage!")
    squirtle = squirtle - 3

    print("Squirtle attacks Bulbasaur for 4 damage!")
    bulbasaur = bulbasaur - 4

    round = round + 1

    print()
    input("Press Enter to continue...\n")

if (bulbasaur <= 0):
    print("Squirtle wins!")
elif(squirtle <= 0):
    print("Bulbasaur wins!")

print()
