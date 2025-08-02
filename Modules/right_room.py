import random
from Modules import fight

def right_room_description():
    print("A ghoul shambles about aimlessly within the destroyed room.")
    print("As you approach, it lurches at you in an attack.")

def right_room_actions(inventory, current_room, hp, defence, attack):
    actions = {
        "attack": "strike the enemy",
        "block": "brace for an attack",
        "spare": "try to help the lost soul"
    }

    enemy = "ghoul"
    enemy_alive = True
    enemy_spared = False

    right_room_description()

    while enemy_alive and not enemy_spared:
        print("\nWhat will you do?")
        for action in actions:
            print(f"- {action}: {actions[action]}")
        act = input(">> ").strip().lower()

        if act == "spare":
            enemy, enemy_alive, enemy_spared = fight.spare(enemy, enemy_alive, enemy_spared)
        elif act == "attack":
            hp, attack, defence, enemy, enemy_alive = fight.attack(hp, attack, defence, enemy, enemy_alive)
        elif act == "block":
            hp, defence, enemy = fight.block(hp, defence, enemy)
        else:
            print("Invalid action. Please choose a valid option.")
            continue  # Skip to next loop iteration without checking victory

        if hp <= 0:
            print("You have fallen to the ghoul...")
            print("Game Over.")
            return inventory, current_room, 0, defence, attack

    # Handle the result
    if enemy_spared:
        print("You spare the ghoul.")
        print("As it fades away, you hear a voice whisper 'thank you'.")
        print("You feel stronger for having shown mercy.")
        hp += 30
        attack += 20
        defence += 20
    else:
        print("You have defeated the ghoul!")
        print("You feel a strange sadness despite your victory.")

    print("All that's left now is to defeat Gurerren.")
    current_room = "boss_room"
    return inventory, current_room, hp, defence, attack
