import random
import time


def left_room_description():
    print("the scortched door evidence of a tragedy, \n")
    print("the room is filled with the acrid smell of burnt wood and smoke.\n")
    print("in the center the scorched remains of what seems to be a long dead person, \n grasping for air they could not breath")
    print("a small wooden box layed out infront of them.")

def left_room2_description():
    print("A small storage room \n")
    print("the room is filled with the acrid smell of burnt wood and smoke.\n")
    print("the only thing still in one piece is a small cubbard")
    

def left_room_actions(inventory, current_room , attack):
    actions = {
        "check body" : "As you approach the body, you hear the creaking of the wood before you notice its hand shifting.",
        "examine room" : left_room_description(),
        "examine box" : "a ornate gold ring glowing with a green light: +15 attack , small chance of death when attacking" ,
        "return" : "You return to the hallway.",
        "left door": "a small door on the left",
        "right door" : "a large steel door", 
        "help" : "Possible actions"
    }
    ring = 1

    if current_room == "left":
        left_room_description()
        time.sleep(2)
    
    print("You can perform the following actions:")
    time.sleep(1)
    for i in actions:
        print(f"- {i}")
        time.sleep(.5)

    while current_room == "left":
        choice = input("Choose an action to perform: ").strip().lower()

        if choice in actions:
            if choice == "check body":
                print(actions[choice])
                time.sleep(1)
                print("The body speaks softly to you: \n Please help me. get me out of here.")
                print("help the person?:\nYes \n No: ")
                if input().strip().lower() == "yes":
                    print("You help the person out of the room.")
                    inventory["grateful captive"] = "A grateful captive, they owe you their life."
                    return inventory
                else:
                    print("You leave the person behind.")
            elif choice == "examine room":
                print(actions[choice])
                time.sleep(1)
            elif choice == "examine box":
                if ring == 1:
                    actions[choice]()
                    inventory["cursed ring"] = "a ornate gold ring glowing with a green light: +15 attack , small chance of death when attacking"
                    attack += 15
                    time.sleep(1)
                    for i in inventory:
                        print(f"{i} : {inventory[i]}")
                        time.sleep(1)
                    time.sleep(1)
                    ring = 0
                else: 
                    print("The box is empty.")
                return inventory, current_room, attack
            elif choice == "return":
                current_room = "hallway"
                return inventory, current_room, attack
            elif choice == "left door":
                current_room = "left2"
                return inventory, current_room, attack
            elif choice == "right door":
                current_room = "right2"
                return inventory, current_room, attack
            elif choice == "help":
                for i in actions:
                    print(f"- {i}")
        else:
            print("Invalid action. Please choose a valid action.")
    return inventory, current_room , attack  # Return both if no valid action is chosen

def left_room2_actions(inventory, current_room , attack):
    actions = {
        "check cubbard " : "A small piece of crumpled parchment is in there, you take it.",
        "examine room" : left_room2_description(),
        "return" : "You return to the hallway." , 
        "help" : "Possible actions"
    }
    ring = 1

    if current_room == "left2":
        left_room2_description()
        time.sleep(2)
    
    print("You can perform the following actions:")
    time.sleep(1)
    for i in actions:
        print(f"- {i}")
        time.sleep(.5)

    while current_room == "left2":
        choice = input("Choose an action to perform: ").strip().lower()

        if choice in actions:
            if choice == "check cubbard":
                print(actions[choice])
                time.sleep(1)
                inventory["scrap paper"] = "a piece of paper with the scripples of a doomed mind"
                return inventory, current_room, attack
            elif choice == "examine room":
                print(actions[choice])
                time.sleep(1)
            elif choice == "return":
                current_room = "hallway"
                return inventory, current_room, attack
            elif choice == "help":
                for i in actions:
                    print(f"- {i}")
        else:
            print("Invalid action. Please choose a valid action.")
    return inventory, current_room , attack  # Return both if no valid action is chosen

def left_room2_actions(inventory, current_room , attack):
    actions = {
        "check boxes " : "a small journal filled with scribblings about a curse and its affects on the villages",
        "examine room" : right_room2_description(),
        "return" : "You return to the hallway." , 
        "help" : "Possible actions"
    }
    ring = 1

    if current_room == "right2":
        left_room2_description()
        time.sleep(2)
    
    print("You can perform the following actions:")
    time.sleep(1)
    for i in actions:
        print(f"- {i}")
        time.sleep(.5)

    while current_room == "right2":
        choice = input("Choose an action to perform: ").strip().lower()

        if choice in actions:
            if choice == "check boxes":
                print(actions[choice])
                time.sleep(1)
                inventory["small journal"] = "a small journal filled with scribblings about a curse and its affects on the villages"
                return inventory, current_room, attack
            elif choice == "examine room":
                print(actions[choice])
                time.sleep(1)
            elif choice == "return":
                current_room = "left_room"
                return inventory, current_room, attack
            elif choice == "help":
                for i in actions:
                    print(f"- {i}")
        else:
            print("Invalid action. Please choose a valid action.")
    return inventory, current_room , attack  # Return both if no valid action is chosen