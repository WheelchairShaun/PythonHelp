bulbasaur = 20
squirtle = 20

print()
print("Bulbasaur vs Squirtle")
print("=====================\n")

print("Round 1!", "\n")
print("Bulbasaur attacks Squirtle for 12 damage!")
squirtle = squirtle - 12
print("Squirtle attacks Bulbasaur for 8 damage!")
bulbasaur = bulbasaur - 8

if (bulbasaur <= 0):
    print("Squirtle wins!")
    exit()
elif(squirtle <= 0):
    print("Bulbasaur wins!")
    exit()

print()
input("Press Enter to continue...\n")

print("Round 2!", "\n")
print("Bulbasaur attacks Squirtle for 12 damage!")
squirtle = squirtle - 12
print("Squirtle attacks Bulbasaur for 8 damage!")
bulbasaur = bulbasaur - 8

if (bulbasaur <= 0):
    print("Squirtle wins!\n")
    exit()
elif(squirtle <= 0):
    print("Bulbasaur wins!\n")
    exit()
