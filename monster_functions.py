import random
import time

from data import data
from dice_functions import dice_roll

MONSTER_LIST = data.monsters
PLAYERS_STATS = data.chr


def ambush_roll(random_monster: int, stat_to_boost: str, weakness_bonus: int) -> str:
    """
    random_monster = the index of the monster being used from the monster list,
    stat_to_boost = The characteristic being used to deal with the monster. eg. Strength
    weakness_bonus = IF a perception check is performed a weakness bonus could be applied to the dice roll.
    Function . Returns your reward text.
    """

    current_monster_fighting = MONSTER_LIST[random_monster]

    print("You require a", current_monster_fighting.to_kill,
          "to deal with the", current_monster_fighting.name)
    # LOOPS until your vigor/health reaches 0
    while PLAYERS_STATS["Vigor"] > 0:
        if dice_roll(random.randint(
                1, 20) + PLAYERS_STATS[stat_to_boost] + weakness_bonus,
                current_monster_fighting.to_kill, stat_to_boost) is True:
            PLAYERS_STATS[current_monster_fighting
                          .reward] = PLAYERS_STATS[current_monster_fighting.reward] + 1
            winning_text = "You dealt with the " + current_monster_fighting.name + " and looted the " + \
                current_monster_fighting.loot + ". This gives " + \
                current_monster_fighting.reward + " +1"
            MONSTER_LIST.pop(random_monster)
            return winning_text
        # IF the roll fails you take 1 Vigor/health
        else:
            PLAYERS_STATS["Vigor"] = PLAYERS_STATS["Vigor"] - 1
            print("Roll failed -1 Vigor")
            time.sleep(2)

    print("You died")
    time.sleep(3)
    quit()


def monster_ambush(random_monster: int) -> str:
    """
    random_monster = the index of the monster being used from the monster list,
    FUNCTION provides the player with the monster they encountered and a choice of action against it."""

    print("On your travels you encounter a",
          MONSTER_LIST[random_monster].name, "\nWhat would you like to do?")
    time.sleep(2)
    fighting = True
    weakness_bonus = 0
    while fighting:
        user_choice = input(
            "1:(Strength) Attack\n2: (Charisma) Persuade\n3:(Perception) Look for a weakness \n4: Flee")
        match user_choice:
            case "1":
                return ambush_roll(random_monster, "Strength", weakness_bonus)
            case "2":
                return ambush_roll(random_monster, "Charisma", 0)
            case "3":
                print("You need a 12 to discover an enemys weakness")
                time.sleep(2)
                if dice_roll(random.randint(1, 20) + PLAYERS_STATS["Perception"], 15, "Perception") is True:
                    print("You discover the", MONSTER_LIST[random_monster].name,
                          "weakness is its", MONSTER_LIST[random_monster].weakness)
                    weakness_bonus = 5
                    time.sleep(2)
                else:
                    print("No weakness discovered")
            case _:
                MONSTER_LIST.pop(random_monster)
                return "You ran away"
