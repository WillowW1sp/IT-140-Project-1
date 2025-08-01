import math
from random import randrange

boss = {
    "hp": 500,
    "attack": 50,
    "defence": 20
}

ghoul = {
    "hp": 200,
    "attack": 30,
    "defence": 10
}

def attack(hp, attack , defence , enemy, enemy_alive):
    enemy_stats = enemy
    damage = attack - (0.5 * enemy_stats["defence"])
    if damage > 0:
        enemy_stats["hp"] -= damage
        if randrange(1, 10, 1) > randrange(1, 6, 1):
            hp -= enemy_stats["attack"] - defence
            if enemy_stats["hp"] <= 0:
                enemy_alive = False
            print(f"You took {enemy_stats['attack'] - defence} damage! Your HP is {hp}")
        else:
            break()
    return hp, attack, defence, enemy, enemy_alive
def block(hp, defence, enemy):
    enemy_stats = enemy
    if randrange(1, 10, 1) > randrange(1, 6, 1):
        hp -= enemy_stats["attack"] / defence
        print(f"You took {enemy_stats['attack'] - defence} damage! Your HP is {hp}")
    else:
        print("You successfully blocked the attack!")

    return hp, defence, enemy, enemy_stats
def spare(enemy, enemy_alive, enemy_spared)
    enemy_stats = enemy
    if randrange(1, 10, 1) > randrange(1, 8, 1):
        print("The ghoul has been spared!")
        enemy_spared = True
    else:
        print("The ghoul ignores your pleads, but in the back of your mind you hear a voice begging for mercy.")
    return enemy, enemy_alive, enemy_spared