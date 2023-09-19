import random
import time

from data import data
from dice_functions import dice_roll, reward_and_pop


# dice_roll = True or False depending if the dice_roll function hit the target value.
# area_type = the index of the area being used from the hidden_area list
# FUNCTION finds and prints the hidden area located by the player.
def find_hidden_area(dice_roll,area_type):
    #IF dice_roll is true then the hidden area is found and printed. Returns reward
    if dice_roll is True:
      print("A secret entrace was found")
      time.sleep(2)
      print("You found the", data.hidden_areas[area_type].area,"\nWhile walking around the",data.hidden_areas[area_type].shortname,"you find the",data.hidden_areas[area_type].verb,data.hidden_areas[area_type].enemy)
      time.sleep(4)
      print("You decide to walk around the",data.hidden_areas[area_type].enemy,"and pick up the item on the ground")
      time.sleep(4)
      data.Inventory.append(data.hidden_areas[area_type].name)
      return reward_and_pop(data.hidden_areas,area_type,data.hidden_areas[area_type].reward)
    #ELSE the area wasnt found
    return "Nothing was found"

# area_type = the index of the area being used from the hidden_area list
#FUNCTION provides the player with an empty area and a choice input of what they wish to do.
def hidden_area(area_type):
  print("You find a suspiciously empty area")
  time.sleep(2)
  print(data.hidden_areas[area_type].perception_check,"is needed to find the hidden area")
  time.sleep(2)
  #Provides the user with 3 options.
  choice = input("What would you like to do?\n1:(Perception) Look around\n2:(Charisma) Ask a soldier to search around for you\n3:Leave")
  #Each option is put into a match-case which returns the find_hidden_area function with a different Characteristic check
  match choice:
    case "1":
      return find_hidden_area(dice_roll(random.randint(1, 20) + data.chr["Perception"], data.hidden_areas[area_type].perception_check, "Perception"),area_type)
    case "2":
      return find_hidden_area(dice_roll(random.randint(1, 20) + data.chr["Charisma"], data.hidden_areas[area_type].perception_check, "Charisma"),area_type)
    case _:
      return "You leave"
