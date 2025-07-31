
def is_archy():
    '''
    A little easter egg for me and my friends.
    '''
    #user_name = input("Enter your user name: ").strip().lower()
    user_name = "Archy".strip().lower()  # Simulating the user name for testing purposes
    if user_name == "archy":
        health = 99999999999999999999
        attack = 99999999999999999999
        defense = 99999999999999999999
    else:
        health = 100
        attack = 10
        defense = 5
    return health, attack, defense

is_archy()