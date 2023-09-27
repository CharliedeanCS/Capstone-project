import time

from data import data

PLAYERS_STATS = data.chr
NPC_LIST = data.npcs
ITEM_LIST = data.items
MONSTER_LIST = data.monsters
AREA_LIST = data.hidden_areas


def dice_roll(players_roll: int, what_player_needs_to_hit: int, stat_boost: str) -> bool:
    """ 
    players_roll = The roll the player got
    what_player_needs_to_hit = What the player must hit to pass
    stat_boost = What Characteristic check is being used on the roll. eg. Charisma
    Function checks if the players roll was more or equal to the target. Returns True or False
    """

    players_stat_to_boost = PLAYERS_STATS[stat_boost]

    print("You rolled a", players_roll)
    # IF the roll hits the target, the player receives a +1 bonus in the Characteristic check they used.
    if (players_roll >= what_player_needs_to_hit):
        players_stat_to_boost = players_stat_to_boost + 1
        print(stat_boost, "+1")
        time.sleep(3)
    return players_roll >= what_player_needs_to_hit


def reward_and_pop(current_encounter_list: list, random_encounter: int, stat_reward: str) -> str:
    """
    current_encounter_list = The current list being accessed. eg. monsters
    random_encounter = The index of the item in the list being accessed
    stat_reward = The Characteristic bonus reward you receive.
    This function pops the item from the list you are accessing so you dont access it again. Returns reward Text
    """

    players_rewarded_stat = PLAYERS_STATS[stat_reward]
    name_of_item_reward = current_encounter_list[random_encounter].name

    players_rewarded_stat = players_rewarded_stat + 1
    reward_text = "You now have " + name_of_item_reward + \
        ". This gives you " + stat_reward + " +1"
    if current_encounter_list == NPC_LIST:
        NPC_LIST.pop(random_encounter)
    elif current_encounter_list == MONSTER_LIST:
        MONSTER_LIST.pop(random_encounter)
    elif current_encounter_list == AREA_LIST:
        AREA_LIST.pop(random_encounter)
    elif current_encounter_list == ITEM_LIST:
        ITEM_LIST.pop(random_encounter)
    return reward_text
