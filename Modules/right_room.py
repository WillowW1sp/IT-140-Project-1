import random
import fight
def right_room_description():
    print()

def right_room_actions(inventory, current_room, hp , defence , attack):
    actions = {
        "attack": "strike the enemy",
        "block": "brace for an attack",
        "spare": "Try to help the lost soul"
    }
    
    enemy = ghoul
    enemy_alive = True
    while enemy == ghoul:
        for i in actions:
            print(f"- {i}")
        act = input("What will you do? ").strip().lower()
        if act in actions:
            # TODO: logic for different attack types, and for spare enemy
            fight.attack(hp, attack , defence , enemy , enemy_alive)
        else:
            print("Invalid action. Please choose a valid action.")