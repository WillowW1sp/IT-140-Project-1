import random
import fight
def right_room_description():
    print("a ghoul shambles about aimlessly within the destroyed room.")
    print("as you approach it lurches at you in an attack")

def right_room_actions(inventory, current_room, hp , defence , attack):
    actions = {
        "attack": "strike the enemy",
        "block": "brace for an attack",
        "spare": "Try to help the lost soul"
    }
    
    enemy = ghoul
    enemy_alive = True
    enemy_spared = False
    while enemy == ghoul:
        for i in actions:
            print(f"- {i}")
        act = input("What will you do? ").strip().lower()
        if act in actions:

            while enemy_alive == True and enemy_spared == False:
                if act == "spare":
                    fight.spare(enemy, enemy_alive, enemy_spared)
                elif act == "attack":
                    fight.attack(hp, attack , defence , enemy, enemy_alive)
                elif act == "block":
                    fight.block(hp, defence, enemy)
            # TODO: logic for different attack types, and for spare enemy
            
            if enemy_spared == True:
                print("You spare the ghoul.\n as it fades away, you hear the voice thanking you.\n you feel stronger having spared the ghoul")
                hp += 30
                attack += 20
                defence += 20
                current_room = "boss_room"
                print("All that's left now is to defeat Gurerren.")
            return inventory, current_room, hp , defence , attack
            
            else: 
                print("You have defeated the ghoul!")
                print("You feel sad inspite of your victory.")
                current_room = "boss_room"
                print("All that's left now is to defeat Gurerren.")
                return inventory, current_room, hp , defence , attack
        else:
            print("Invalid action. Please choose a valid action.")
        
        inventory, current_room, hp , defence , attack