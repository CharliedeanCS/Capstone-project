#Version 1.17
import random
import time

#Imports the other files into main.
from data import data
from dice_functions import dice_roll, reward_and_pop
from hidden_area_functions import hidden_area
from monster_functions import monster_ambush


# item_type = the index of the item being used from the item list
#Function to discover an item.
def item_discovery(item_type):
  print("You find a mound of dirt along your path\nYou peform a perception check on the area\nA",data.items[item_type].perception_check,"is needed to find the item hidden along the path")
  time.sleep(4)
  #Peforms the diceroll function to check if you hit the correct target value to proceed.
  if dice_roll(random.randint(1, 20) + data.chr["Perception"], data.items[item_type].perception_check, "Perception") is True:
      return reward_and_pop(data.items,item_type,data.items[item_type].reward)
  else:
    return "You didnt find anything"
  return 0

# item_type = the index of the item being used from the item list
#Function to discover an NPC.
def npc_found(npc_type):
    print("You found",data.npcs[npc_type].npc_name)
    time.sleep(2)
    #Provides a choice to the player of how they will communicate with the NPC.
    npc_choice = input("What would you like to do?\n1: (Charisma) Convince him to help you\n2: Run away")
    match npc_choice:
      case "1":
        print(data.npcs[npc_type].charisma_check,"is needed to convince them")
        if dice_roll(random.randint(1, 20) + data.chr["Charisma"], data.npcs[npc_type].charisma_check, "Charisma") is True:
          return reward_and_pop(data.npcs,npc_type,data.npcs[npc_type].reward)
      case "2":
        return data.npcs[npc_type].npc_name +" confused, watched as you ran away"
      case _:
        return data.npcs[npc_type].npc_name + " cant help you"
  
#Function chooses a random encounter each time its ran.
def random_encounter():
  encounter_completed = False
  #Runs untill atleast 1 encounter is completed
  while encounter_completed is False:
    #Chooses a random number from 0 to 3.
    encounter_type = random.randint(0,3)
    #Uses the random number to pick one of four different encounters
    match data.encounters[encounter_type]:
      case "monster_ambush" if len(data.monsters)>0:
          monster_type = random.randint(0, len(data.monsters)-1)
          print(monster_ambush(monster_type))
          #encounter is completed
          encounter_completed = True
      case "item_discovery" if len(data.items)>0:
        item_type = random.randint(0, len(data.items)-1)
        print(item_discovery(item_type))
        encounter_completed = True
      case "hidden_area" if len(data.hidden_areas)>0:
        area_type = random.randint(0, len(data.hidden_areas)-1)
        print(hidden_area(area_type))
        encounter_completed = True
      case "npc_found" if len(data.npcs)>0:
        npc_type = random.randint(0, len(data.npcs)-1)
        print(npc_found(npc_type))
        encounter_completed = True

#Main function for the game code. 
def main_game():

  #Prints 6 different lines of a already set narrative.
  #Peforms 6 different random encounters.
  for i in range(0, 6):
    print("\n")
    print(data.story_narrative[i])
    print("\n")
    random_encounter()
    time.sleep(4)

  #Outputs last line of the adventure narrative.
  print(data.story_narrative[len(data.story_narrative)-1])
  text = "How will you proceed\n1:Charge into battle"
  #Checks if your inventory contains any unique items.
  if data.Inventory.__contains__("Medusa's Head"):
    #Unique text only added if the inventory contains the item. 
    text += "\n2: Use Medusas Head"
  if data.Inventory.__contains__("Minotaurs Horn"):
    text += "\n3: Use Minotaurs Horn"
  #User input based on the updated text.
  battle_choice = input(text)
  match battle_choice:
    case "1":
      print("You died")
    case "2" if data.Inventory.__contains__("Medusa's Head"):
      print("You use Medusa's Head and turn the Persian Army to stone")
    case "3" if data.Inventory.__contains__("Minotaurs Horn"):
      print("You use the Minotaurs Horn improving your strength by 10")
      data.chr["Strength"] = data.chr["Strength"] + 10
    case _:
      print("You died")
    

  
  print("Your final stats were",data.chr)

main_game()


