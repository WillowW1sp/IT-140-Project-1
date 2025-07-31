from colorama import Fore, Back , Style
from Modules import main_room

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

# little easter egg for archy (A character in my games)
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