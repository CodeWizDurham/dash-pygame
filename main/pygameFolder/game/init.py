def get_name():
    plr_name = str(input("What is your name? (for the leaderboard.) "))
    print("Starting game.")
    return(plr_name)

def get_map():
    map_id = int(input("What map do you want to play? (0 for backrooms, 1 for ballpit, 2 for napoleonic wars, 3 for SCP.) "))
    if map_id != 0 and map_id != 1 and map_id != 2 and map_id != 3:
        print("Not a valid map. Try again.")
        get_map()
    return(map_id)

def get_char():
    char_id = int(input("what character do you want to play as? (0 for Cheetah, 1 for Borzoi, 2 for Labrador, 3 for Beagle, 4 for SCP Guard.) "))
    return(char_id)