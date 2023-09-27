# Version 1.17
# Fix Naming Conventions
import random
import time

# Imports the other files into main.
from data import data
from dice_functions import dice_roll, reward_and_pop
from hidden_area_functions import hidden_area
from monster_functions import monster_ambush

PLAYERS_STATS = data.chr

ITEMS_LIST = data.items
NPC_LIST = data.npcs
ENCOUNTER_LIST = data.encounters
MONSTER_LIST = data.monsters
AREA_LIST = data.hidden_areas
PLAYERS_INVENTORY = data.Inventory
NARRATIVE = data.story_narrative


def item_discovery(random_item: int) -> str:
    """
    random_item = the index of the item being used from the item list
    Function to discover an item.
    """

    found_item = ITEMS_LIST[random_item]
    dice_roll_plus_players_perception = random.randint(
        1, 20) + PLAYERS_STATS["Perception"]
    possible_stat_boost = "Perception"

    print("You find a mound of dirt along your path\nYou peform a perception check on the area\nA",
          found_item.perception_check, "is needed to find the item hidden along the path")
    time.sleep(4)

    # Peforms the diceroll function to check if you hit the correct target value to proceed.
    if dice_roll(dice_roll_plus_players_perception, found_item.perception_check, possible_stat_boost) is True:
        return reward_and_pop(ITEMS_LIST, random_item, found_item.reward)
    else:
        ITEMS_LIST.pop(random_item)
        return "You didn't find anything"


def npc_found(random_npc: int) -> str:
    """
    random_npc = the index of the item being used from the item list
    Function to discover an NPC.
    """

    current_npc_found = NPC_LIST[random_npc].npc_name
    dice_roll_plus_players_charisma = random.randint(
        1, 20) + PLAYERS_STATS["Charisma"]
    possible_stat_boost = "Charisma"

    print("You found", current_npc_found)
    time.sleep(2)
    # Provides a choice to the player of how they will communicate with the NPC.
    npc_choice = input(
        "What would you like to do?\n1: (Charisma) Convince him to help you\n2: Run away")
    match npc_choice:
        case "1":
            print(NPC_LIST[random_npc].charisma_check,
                  "is needed to convince them")
            if dice_roll(dice_roll_plus_players_charisma, NPC_LIST[random_npc].charisma_check, possible_stat_boost) is True:
                return reward_and_pop(NPC_LIST, random_npc, NPC_LIST[random_npc].reward)
        case "2":
            NPC_LIST.pop(random_npc)
            return current_npc_found + " confused, watched as you ran away"
    NPC_LIST.pop(random_npc)
    return current_npc_found + " cant help you"


def random_encounter():
    """Function chooses a random encounter each time its ran."""

    encounter_completed = False

    # Runs until at least 1 encounter is completed
    while encounter_completed is False:
        # Chooses a random number from 0 to 3.
        random_encounter = random.randint(0, 3)
        # Uses the random number to pick one of four different encounters
        match ENCOUNTER_LIST[random_encounter]:
            case "monster_ambush" if len(MONSTER_LIST) > 0:
                random_monster = random.randint(0, len(MONSTER_LIST)-1)
                print(monster_ambush(random_monster))
                # encounter is completed
                encounter_completed = True
            case "item_discovery" if len(ITEMS_LIST) > 0:
                random_item = random.randint(0, len(ITEMS_LIST)-1)
                print(item_discovery(random_item))
                encounter_completed = True
            case "hidden_area" if len(AREA_LIST) > 0:
                random_area = random.randint(0, len(AREA_LIST)-1)
                print(hidden_area(random_area))
                encounter_completed = True
            case "npc_found":
                random_npc = random.randint(0, len(NPC_LIST)-1)
                print(npc_found(random_npc))
                encounter_completed = True


if __name__ == "__main__":
    """Runs the games main functions"""
    # Prints 6 different lines of a already set narrative.
    # Perform 6 different random encounters.

    for i in range(0, 6):
        print("\n")
        print(NARRATIVE[i])
        print("\n")
        random_encounter()
        time.sleep(4)

    # Outputs last line of the adventure narrative.
    print(NARRATIVE[len(NARRATIVE)-1])
    battle_choice_text = "How will you proceed\n1:Charge into battle"
    # Checks if your inventory contains any unique items.
    if PLAYERS_INVENTORY.__contains__("Gorgon's Head"):
        # Unique text only added if the inventory contains the item.
        battle_choice_text += "\n2: Use Gorgon's Head"
    if PLAYERS_INVENTORY.__contains__("Minotaur Horn"):
        battle_choice_text += "\n3: Use Minotaur Horn"
    # User input based on the updated text.
    battle_choice = input(battle_choice_text)
    match battle_choice:
        case "1":
            print("You died")
        case "2" if PLAYERS_INVENTORY.__contains__("Gorgon's Head"):
            print("You use Medusa's Head and turn the Persian Army to stone")
        case "3" if PLAYERS_INVENTORY.__contains__("Minotaur Horn"):
            print("You use the Minotaur Horn improving your strength by 10")
            PLAYERS_STATS["Strength"] = PLAYERS_STATS["Strength"] + 10
        case _:
            print("You died")

    print("Your final stats were", PLAYERS_STATS)
