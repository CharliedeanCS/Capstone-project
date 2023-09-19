import time

from data import data


# roll = The roll the player got
# to_hit = What the player must hit to pass
# type = What Charactistic check is being used on the roll. eg. Charisma
# Function checks if the players roll was more or equal to the target. Returns True or False
def dice_roll(roll, to_hit, type):
  print("You rolled a", roll)
  #IF the roll hits the target, the player recieves a +1 bonus in the Charactistic check they used.
  if (roll >= to_hit):
    data.chr[type] = data.chr[type] + 1
    print(type,"+1")
    time.sleep(3)
  return roll >= to_hit

# list = The current list being accessed. eg. monsters
# type = The index of the item in the list being accessed
# reward = The Charactistic bonus reward you receive.
# This function pops the item from the list you are accesing so you dont access it again. Returns reward Text
def reward_and_pop(list,type,reward):
      data.chr[reward] = data.chr[reward] + 1
      text = "You now have " + list[type].name + ". This gives you " + reward + " +1"
      match list:
        case data.npcs:
          data.npcs.pop(type)
        case data.monsters:
          data.monsters.pop(type)
        case data.hidden_areas:
          data.hidden_areas.pop(type)
        case data.items:
          data.items.pop(type)
      return text