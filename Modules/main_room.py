import time

def main_room_description():
    print("You wake up in a dimly lit room, stained alabaster walls surround you. The air is thick with dust, and the faint sound of dripping water echoes in the distance. A single door stands before you, slightly ajar, inviting you to explore further.\n")
    print("You take a moment to survey your surroundings. The room is empty except for a few scattered pieces of furniture and a flickering light bulb overhead.")

def main_room_actions(inventory, current_room):
    actions = {
        "look around": main_room_description,  # Callable function for look around
        "open door": "You push the door open and step into the hallway, ready to face whatever challenges lie ahead.",
        "check furniture": "You examine the furniture, finding nothing of interest except for a dusty old book that seems to have been left behind.",
        "sit down": "You sit down on a nearby chair, taking a moment to catch your breath and gather your thoughts.",
        "help": "You can:\n -look around\n -open door\n -check furniture\n -sit down"
    }

    book = 1

    # Print the room description once at the start
    if current_room == "main_room":
        main_room_description()
        time.sleep(2)  # Adjust the delay as necessary

    print("You can perform the following actions:")
    time.sleep(1)
    print("Available actions:")
    for action in actions:
        print(f"- {action}")
        time.sleep(0.5)

    while current_room == "main_room":
        choice = input("Choose an action to perform: ").strip().lower()

        if choice in actions:
            # If it's a function (look around)
            if callable(actions[choice]):
                actions[choice]()  # Call the function directly

            # If it's just a string (open door, check furniture)
            elif choice == "check furniture":
                    if book == 1:
                        inventory["dusty book"] = "A dusty old book that seems to have been left behind."
                        print(f"Inventory updated: \n")
                        time.sleep(1)
                        for item in inventory:
                            print(f"{item} : {inventory[item]}")
                            time.sleep(1)
                        book = 0

                    else:
                        print("The furniture has nothing else of interest.")
                return inventory , current_room

            elif choice == "open door":
                print("You push the door open and step into the hallway, ready to face whatever challenges lie ahead.")
                current_room = "hallway"  # Update the current room
                return inventory , current_room  # Return both inventory and current room

            elif choice == "sit down":
                print(actions[choice])

            elif choice == "help":
                print(actions[choice])

        else:
            print("Invalid action. Please choose a valid action.")

    return inventory, current_room  # Return both if no valid action is chosen
