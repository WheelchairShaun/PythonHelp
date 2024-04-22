from battleLib import *

def gameover():
    if (bulbasaur <= 0 and squirtle <= 0):
        print("It's a draw!\n")
        return
    
    if (bulbasaur <= 0):
        print("Squirtle wins!")
    elif(squirtle <= 0):
        print("Bulbasaur wins!")
    
    print()


bulbasaur = 20
squirtle = 20

print()
print("Bulbasaur vs Squirtle")
print("=====================\n")

round = 1

while(bulbasaur > 0 and squirtle > 0):
    print("Round ", round, "!\n", sep="")

    printHealth("Bulbasaur", bulbasaur)
    printHealth("Squirtle", squirtle)
    print()

    damage = combat("Bulbasaur", "Squirtle")
    squirtle = squirtle - damage

    damage = combat("Squirtle", "Bulbasaur")
    bulbasaur = bulbasaur - damage

    round = round + 1
    print()
    input("Press Enter to continue...\n")

gameover()