obj_in_rm = [
    "north door",
    "south door",
    "east door",
    "west door",
    "a table dripping with a purple liquid",
    "a chair with a broken leg",    
]

user_actions = [
    "look around",
    "examine north door",
    "examine south door",
    "examine east door",
    "examine west door",
    "examine table",
    "examine chair",
    "open north door",
    "open south door",
    "open east door",
    "open west door",
    "sit on chair",
    "drink purple liquid",
    "leave room",
    "help",
    "quit"
]
def start_room():
    print("You are in a room with four doors and some furniture.")
    print("You can interact with the objects in the room or leave.")
    print("Type 'help' for a list of actions or 'quit' to exit.")

    while True:
        action = input("What do you want to do? ").strip().lower()
        
        if action == "help":
            print("Available actions:")
            for user_action in user_actions:
                print(f"- {user_action}")
        elif action == "quit":
            print("Exiting the game. Goodbye!")
            break
        elif action in user_actions:
            print(f"You chose to: {action}")
        else:
            print("Invalid action. Type 'help' for a list of actions.")