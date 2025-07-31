def user_action() :
    user_actions = [
        "look around",
        "examine {}",
        "examine {}",
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

    print("Welcome to my game/n First, what is your name?")
    user_name= input()
    print("{} how interesting.".format(user_name))
    
    while True:
        action = input("What do you want to do? ").strip().lower()

        if action == "help":
            print("Available actions:")
            for user_action in user_actions:
                print(f"- {user_action}")
        elif action == "quit":
            print("Exiting the game. Goodbye!")
            quit()
        elif action in user_actions:
            print(f"You chose to: {action}")

        else:
            print("Invalid action. Type 'help' for a list of actions.")