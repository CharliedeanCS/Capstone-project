import random
import time

from data import data
from dice_functions import dice_roll, reward_and_pop

AREA_LIST = data.hidden_areas
PLAYER_INVENTORY = data.Inventory
PLAYERS_STATS = data.chr


def find_hidden_area(dice_roll: int, random_area: int) -> str:
    """dice_roll = True or False depending if the dice_roll function hit the target value.
       random_area = the index of the area being used from the hidden_area list
       FUNCTION finds and prints the hidden area located by the player."""

    current_area = AREA_LIST[random_area]

    # IF dice_roll is true then the hidden area is found and printed. Returns reward
    if dice_roll is True:
        print("A secret entrance was found")
        time.sleep(2)
        print("You found the", current_area.area, "\nWhile walking around the", current_area.shortname,
              "you find the", current_area.verb, current_area.enemy)
        time.sleep(4)
        print("You decide to walk around the",
              current_area.enemy, "and pick up the item on the ground")
        time.sleep(4)
        PLAYER_INVENTORY.append(current_area.name)
        return reward_and_pop(AREA_LIST, random_area, current_area.reward)
    # ELSE the area wasn't found
    AREA_LIST.pop(random_area)
    return "Nothing was found"


def hidden_area(random_area: int) -> str:
    """
    random_area = the index of the area being used from the hidden_area list
    FUNCTION provides the player with an empty area and a choice input of what they wish to do.
    """

    current_area = AREA_LIST[random_area]
    dice_roll_plus_perception = random.randint(
        1, 20) + PLAYERS_STATS["Perception"]
    dice_roll_plus_charisma = random.randint(1, 20) + PLAYERS_STATS["Charisma"]

    print("You find a suspiciously empty area")
    time.sleep(2)
    print(current_area.perception_check,
          "is needed to find the hidden area")
    time.sleep(2)
    # Provides the user with 3 options.
    user_choice = input(
        "What would you like to do?\n1:(Perception) Look around\n2:(Charisma) Ask a soldier to search around for you\n3:Leave")
    # Each option is put into a match-case which returns the find_hidden_area function with a different Characteristic check
    match user_choice:
        case "1":
            return find_hidden_area(dice_roll(dice_roll_plus_perception, current_area.perception_check, "Perception"), random_area)
        case "2":
            return find_hidden_area(dice_roll(dice_roll_plus_charisma, current_area.perception_check, "Charisma"), random_area)
        case _:
            AREA_LIST.pop(random_area)
            return "You leave"
