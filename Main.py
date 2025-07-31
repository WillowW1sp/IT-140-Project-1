from colorama import Fore, Back , Style
from Modules import main_room
'''
i coded 80% of this in one go without testing most of it (thanks github codespaces for making a good chunk of testing impossible)
if this works at all I'll be shocked 
'''
#list of all rooms and which module to run for them
rooms = {
    "main_room": main_room.main_room_description(),
    "hallway": hallway.main_hallway_description(),

}

#variable for what room you are in
current_room = "main_room"

# Player inventory 
inventory = {
    
}
#win condition
win = False
#game maker chats
print(Fore.RED , "Welcome to my game." , Style.RESET_ALL)
print(Fore.RED , "Defeat Gurerren, free the captives." , Style.RESET_ALL)
print(Fore.RED , "First, What is your name?" , Style.RESET_ALL)

#name = input().strip().lower()
name = "archy" #name for testing purposes TODO remove this line when done testing

# little easter egg for archy (A joke character i use alot take a look at my youtube TODO add youtube. Archy will be appearing soon)
if name == "archy":
    print(Fore.RED , "Welcome back, Archy!/n It's been so long since we've played together" , Style.RESET_ALL)
    hp = 9999999999999999
    defence = 9999999999999999
    attack = 9999999999999999
elif name == "":
    print(Fore.RED , "Welcome, stranger!/n I hope you enjoy your stay." , Style.RESET_ALL)
    hp = 100
    defence = 10
    attack = 10
else:
    print(Fore.RED , "Welcome, " + name + "!/n I hope you enjoy your stay." , Style.RESET_ALL)
    hp = 100
    defence = 10
    attack = 10

#start room loop 
while win == False:
    if hp > 0:
    current_room()
    else: 
    print(Fore.RED , "Another victim for the horde" , Style.RESET_ALL)
    print(Fore.RED , Back.WHITE , "Game Over." , Style.RESET_ALL)
else: 
    print(Fore.RED , "Thank you" , Style.RESET_ALL)
    if "dusty book" and "lore book 1" in inventory:
        print("Gurerren the deciever, lost to the madness of his crypt locked away any who entered.")
        print("His fractured mind convincing him the only way to save his people was to lock them away.")
        print("With the help of the captives you have freed, you have defeated Gurerren and freed the captives.")
        print("Ending his life, and the curse holding him.")
        print(Fore.WHITE , "The End." , Style.RESET_ALL)
    elif "dusty book" in inventory and "lore book 1" not in inventory:
        print("You have defeated the cruel Gurerren, his monsterous form now lifeless.")
        print("the captives you have freed are now free to leave.")
        print(Fore.WHITE , "The End?" , Style.RESET_ALL)
    elif "lore book 1" in inventory and "dusty book" not in inventory:
        print("You have defeated the cruel Gurerren, his monsterous form now lifeless.")
        print("The once peaceful man now a monster of his own making. His mind fractured by the curse of his crypt.")
        print("Having abducted locals of the village to feed his curse, they seem to be free now.")
        print(Fore.WHITE , "The End?" , Style.RESET_ALL)