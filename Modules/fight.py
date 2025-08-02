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

enemies = {
    "boss": boss,
    "ghoul": ghoul
}

def attack(hp, attack, defence, enemy, enemy_alive):
    enemy_stats = enemies[enemy]
    damage = attack - (0.5 * enemy_stats["defence"])
    if damage > 0:
        enemy_stats["hp"] -= damage
        print(f"You dealt {damage:.2f} damage to the {enemy}. It has {enemy_stats['hp']:.2f} HP left.")

    if enemy_stats["hp"] <= 0:
        enemy_alive = False
        print(f"The {enemy} has been defeated!")
        return hp, attack, defence, enemy, enemy_alive

    if randrange(1, 10) > 5:
        damage_taken = max(0, enemy_stats["attack"] - defence)
        hp -= damage_taken
        print(f"You took {damage_taken} damage! Your HP is {hp}")
    else:
        print("The enemy missed!")

    return hp, attack, defence, enemy, enemy_alive

def block(hp, defence, enemy):
    enemy_stats = enemies[enemy]
    if randrange(1, 10) > 5:
        damage_taken = max(0, enemy_stats["attack"] - defence)
        hp -= damage_taken
        print(f"You took {damage_taken} damage! Your HP is {hp}")
    else:
        print("You successfully blocked the attack!")

    return hp, defence, enemy

def spare(enemy, enemy_alive, enemy_spared):
    enemy_stats = enemies[enemy]
    if randrange(1, 10) > 7:
        print(f"The {enemy} has been spared!")
        enemy_spared = True
    else:
        print(f"The {enemy} ignores your pleas, but in the back of your mind you hear a voice begging for mercy.")
    return enemy, enemy_alive, enemy_spared
