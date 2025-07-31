from Modules import user_name , start_room

hp , defense, atk = user_name.is_archy()
print(hp)
print(defense)
print(atk)

room = start_room.start_room()
#TODO add items module
#items = items.inventory()
hp = 100  # Example starting health
while hp > 0:
    #action = input("What do you want to do? ").strip().lower()
    action = "help"
    if action == "quit":
        print("Exiting the game. Goodbye!")
        break
    elif action == "help":
        print("Available actions:")
        for user_action in start_room.user_actions:
            print(f"- {user_action}")
    else:
        start_room.start_room(action)