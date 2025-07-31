
def main_room_description():
    print("You wake up in a dimly lit room, stained alabastor walls surround you. The air is thick with dust, and the faint sound of dripping water echoes in the distance. A single door stands before you, slightly ajar, inviting you to explore further.")
    print("You take a moment to survey your surroundings. The room is empty except for a few scattered pieces of furniture and a flickering light bulb overhead.")

def main_room_actions():
    actions = {
        "look around": main_room_description(),
        "open door": "You push the door open and step into the hallway, ready to face whatever challenges lie ahead.",
        "check furniture": "You examine the furniture, finding nothing of interest except for a dusty old book that seems to have been left behind.",
        "sit down": "You sit down on a nearby chair, taking a moment to catch your breath and gather your thoughts."
    }

    # Description of the main room
    main_room_description()

    print("You can perform the following actions:")
    print("Available actions:")
    for action in actions:
        print(f"- {action}")
    print("Choose an action to perform:")

    choice = input().strip().lower()
    while choice != "open door":
        if choice in actions:
            print(actions[choice])
            if choice == "check furniture": 
                inventory["dusty book"] = "A dusty old book that seems to have been left behind."
                return inventory[]  # return inventory if furniture is checked
        else: 
            print("Invalid action. Please choose a valid action.")
    else:
        print("You open the door and step into the hallway, ready to face whatever challenges lie ahead.")
        current_room = "hallway"
        return current_room  # change current room to hallway
    return current_room  # return current room if no valid action is chosen
    return inventory  # return inventory if no action is chosen