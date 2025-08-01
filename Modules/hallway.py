import time

def hallway_description():
    print("the halway is seemingly endless, plastered with fading green wallpaper\n")
    print("long, old scratch marks score the length of the hallway\n")
    print("Three doors are visible in the hallway, one behind you where you came from\n")
    print("one on your left, marred with scorch marks\n and on on your right, strange sounds echoing from within")
def main_hallway_actions(inventory , current_room):
    actions = {
        # TODO go back and edit the descriptions here
        "return" : "you turn back to the previous room to see if you missed anything.",
        "left door": "A door marred with scorch marks, the smell of a long dead fire comes from the door",
        "right door": "A door on the right, strange sounds echoing from within",
        "examine hallway" : "as you look around the hallway you notice a small depress on the wall\n when you push it a panel pops out of the wall with a *click*\n " ,
        "help" : "possible actions"
    }

    if current_room == "hallway":
        hallway_description()
        time.sleep(2)
    
    print("You can perform the following actions:")
    time.sleep(1)
    for actions in actions:
        print(f"- {actions}")
        time.sleep(.5)
    
    while current_room == "hallway":
        choice = input("Choose an action to perform: ").strip().lower()

        if choice in actions:
            if choice == "return":
                current_room = "main_room"
                print(actions[choice])
                return inventory , current_room
            elif choice == "left door":
                current_room = "left"
                print(actions[choice])
                return inventory , current_room
            elif choice == "right door":
                current_room = "right"
                print(actions[choice])
                return inventory, current_room
            elif choice == "examine hallway":
                print(actions[choice])
                inventory["hand bound book"] = "A hand bound book covered in a light stiff leather embossed in gold"
                print(f"Inventory updated: \n")
                time.sleep(1)
                for item in inventory:
                    print(f"{item} : {inventory[item]}")
                    time.sleep(1)
            elif choice == "help":
                for i in actions:
                    print(f"- {i}")
                return inventory , current_room
        else: 
            print("Invalid action. Please choose a valid action.")
    return inventory, current_room  # Return both if no valid action is chosen