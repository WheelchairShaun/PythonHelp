import math, random

def combat(attacker, defender):
    damage = math.floor( random.random() * 10 )

    if(damage > 1):
        print(attacker, " attacks ", defender, " for ", damage, sep="", end="!\n")
    elif (damage == 0):
        print(attacker, " misses ", defender, sep="", end=".\n")
    else:
        print(defender, " dodges ", attacker, "\'s attack", sep="", end="!!\n")
        damage = 0

    return damage

def printHealth(name, health):
    print(name, ": ", health, sep="")

