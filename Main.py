from Modules import user_name , start_room , user_action

hp , defense, atk = user_name.is_archy()
print(hp)
print(defense)
print(atk)

room = start_room.start_room()
#TODO add items module
#items = items.inventory()
hp = 100  # Example starting health

while hp > 0 :
    #action = input("What do you want to do? ").strip().lower()
    act = user_action.user_action()
   # room = start_room.start_room()
print("done?")