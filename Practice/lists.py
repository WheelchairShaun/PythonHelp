from battleLib import *

pokemon = ["Bulbasaur", "Charizard", "Blastoise", "Squirtle", "Pikachu"]

def printList():
    for i in range(len(pokemon)):
        print(i + 1, ": ", pokemon[i], sep="")

def choose(n):
    return pokemon[n - 1]

def gameover():
    if (attacker <= 0 and squirtle <= 0):
        print("It's a draw!\n")
        return
    
    if (attacker <= 0):
        print("Squirtle wins!")
    elif(squirtle <= 0):
        print(attackerName, "wins!")
    
    print()

printList()
choice = int(input("Choose a Pokémon by number: "))

attackerName = pokemon[choice - 1]
print("\nI choose you, ", attackerName, "!!", sep="", end="\n\n")

attacker = 20
squirtle = 20

print()
print(attackerName, "vs Squirtle")
print("=====================\n")

round = 1

while(attacker > 0 and squirtle > 0):
    print("Round ", round, "!\n", sep="")

    printHealth(attackerName, attacker)
    printHealth("Squirtle", squirtle)
    print()

    damage = combat(attackerName, "Squirtle")
    squirtle = squirtle - damage

    damage = combat("Squirtle", attackerName)
    attacker = attacker - damage

    round = round + 1
    print()
    input("Press Enter to continue...\n")

gameover()