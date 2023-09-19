import random
import time

from data import data
from dice_functions import dice_roll

# monster_type = the index of the monster being used from the monster list,
# type = The charactistic being used to deal with the monster. eg. Strength
# weakness_bonus = IF a perception check is peformed a weakness bonus could be applied to the dice roll.
# Function . Returns your reward text.
def ambush_roll(monster_type, type,weakness_bonus):
  print("You require a", data.monsters[monster_type].to_kill,
        "to deal with the", data.monsters[monster_type].name)
  #LOOPS untill your vigor/health reaches 0
  while data.chr["Vigor"] > 0: 
    if dice_roll(random.randint(1, 20) + data.chr[type] + weakness_bonus, 
                 data.monsters[monster_type].to_kill, type) is True:
      data.chr[data.monsters[monster_type].reward] = data.chr[data.monsters[monster_type].reward] + 1
      text = "You dealt with the " + data.monsters[monster_type].name + " and looted the " + data.monsters[monster_type].loot + ". This gives "+ data.monsters[monster_type].reward +" +1"
      data.monsters.pop(monster_type)
      return text
    #IF the roll fails you take 1 Vigor/health
    else:
      data.chr["Vigor"] = data.chr["Vigor"] - 1
      print("Roll failed -1 Vigor")
      time.sleep(2)
      
  print("You died")
  time.sleep(3)
  quit()

# monster_type = the index of the monster being used from the monster list,
#FUNCTION provides the player with the monster they encountered and a choice of action against it.
def monster_ambush(monster_type):
  print("On your travels you encounter a",
        data.monsters[monster_type].name, "\nWhat would you like to do?")
  time.sleep(2)
  fighting = True
  weakness_bonus = 0
  while fighting:
    choice = input("1:(Strength) Attack\n2: (Charisma) Persuade\n3:(Perception) Look for a weakness \n4: Flee")
    match choice:
      case "1":
        return ambush_roll(monster_type, "Strength",weakness_bonus)
      case "2":
        return ambush_roll(monster_type, "Charisma",0)
      case "3":
        print("You need a 12 to discover an enemys weakness")
        time.sleep(2)
        if dice_roll(random.randint(1, 20) + data.chr["Perception"], 15, "Perception") is True:
          print("You discover the",data.monsters[monster_type].name,"weakness is its", data.monsters[monster_type].weakness)
          weakness_bonus = 5
          time.sleep(2)
        else:
          print("No weakness discovered")
      case _:
        return "You ran away"