from colorama import Fore, Back, Style
from Modules import main_room, hallway , left_room, right_room, fight, boss_room
import time
#TODO: Cry because I might have bit off more than i can chew
# List of all rooms and which module to run for them
rooms = {
    "main_room": main_room.main_room_actions,
    "hallway": hallway.main_hallway_actions,
    "left": left_room.left_room_actions,
    "right": right_room.right_room_actions,
    "boss_room": boss_room.boss_room_main,
    "left2" : left_room.left_room2_actions,
    "right2" : left_room.right_room2_actions,
}
hp = 1
defence = 1
attack = 1
# Variable for what room you are in
current_room = "main_room"
room_module = rooms[current_room]

# Player inventory
inventory = {
    "cloths": "the cloths you woke up wearing"
}

# Win condition
win = 0

# Game maker chats
print(Fore.RED, "Welcome to my game.", Style.RESET_ALL)
time.sleep(1)
print(Fore.RED, "Defeat Gurerren, free the captives.", Style.RESET_ALL)
time.sleep(1)

name = input(Fore.RED + "First, What is your name?" + Style.RESET_ALL).strip().lower()
time.sleep(1)

# Little easter egg for archy (A joke character I use a lot)
if name == "archy":
    print(Fore.RED, "Welcome back, Archy!\n It's been so long since we've played together\n", Style.RESET_ALL)
    hp = 9999999999999999
    defence = 20
    attack = 9999999999999999
    
elif name == "":
    print(Fore.RED, "Welcome, stranger!\n I hope you enjoy your stay.\n", Style.RESET_ALL)
    hp = 100
    defence = 10
    attack = 10
    
else:
    print(Fore.RED, "Welcome, " + name + "!\n I hope you enjoy your stay.\n", Style.RESET_ALL)
    hp = 100
    defence = 10
    attack = 10
    

time.sleep(3)

# Start room loop
while win == 0:
    if hp > 0:
        # Pass inventory and current_room to the room module and update them
        if current_room in ["main_room" , "hallway"]:
            inventory , current_room = room_module(inventory, current_room)  # capture & update 3 vars
        elif current_room == "left":
            inventory, current_room , attack = room_module(inventory, current_room , attack)
        elif current_room == "right":
            inventory, current_room, hp , defence , attack = room_module(inventory, current_room, hp , defence , attack)
        elif current_room == "boss_room":
            inventory, current_room, hp , defence , attack, win = room_module(inventory, current_room, hp , defence , attack , win)

        # Update room_module after transition
        room_module = rooms[current_room]  # Update the room module based on the new room
        for i in inventory:
            print(i)
    else:
        print(Fore.RED, "Another victim for the horde", Style.RESET_ALL)
        print(Fore.RED, Back.WHITE, "Game Over.", Style.RESET_ALL)
        break

    print(Fore.RED, "Thank you", Style.RESET_ALL)
    # check for lore books
    if "dusty book" and "lore book 1" and "scrap paper" and "small journal" and "hand bound book" and "ghoul blessing" in inventory:
        print("Gurerren the deceiver, lost to the madness of his crypt locked away any who entered.")
        print("His fractured mind convincing him the only way to save his people was to lock them away.")
        print("With the help of the captives you have freed, you have defeated Gurerren and freed the captives.")
        print("Ending his life, and the curse holding him.")
        print(Fore.WHITE, "The End.", Style.RESET_ALL)
        win = 1
    elif "dusty book" in inventory and "lore book 1" not in inventory:
        print("You have defeated the cruel Gurerren, his monstrous form now lifeless.")
        print("The captives you have freed are now free to leave.")
        print("The mysteries of this crypt may never be discovered now")
        print(Fore.WHITE, "The End?", Style.RESET_ALL)
        win = 1
    else:
        print("You have defeated the cruel Gurerren, his monstrous form now lifeless.")
        print("The once peaceful man now a monster of his own making. His mind fractured by the curse of his crypt.")
        print("Having abducted locals of the village to feed his curse, they seem to be free now.")
        print("The mysteries of this crypt may never be discovered now.")
        print(Fore.WHITE, "The End?", Style.RESET_ALL)
        print(Fore.RED, "you defeated guerren but learned nothing of his plight. \n Try again, find the clues")
        win = 1
