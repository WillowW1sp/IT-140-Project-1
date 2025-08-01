import math

boss_stats = {
    "hp": 500,
    "attack": 50,
    "defence": 20
}

ghoul1_stats = {
    "hp": 200,
    "attack": 30,
    "defence": 10
}

def attack(attack , enemy , enemy_stats):
    enemy_stats = enemy
    damage = attack - enemy_stats["defence"]
    if damage > 0:
        enemy_stats["hp"] -= damage
    return enemy_stats
