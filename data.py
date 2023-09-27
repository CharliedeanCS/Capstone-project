# 4 classes storing the variables linked with each encounter that can occur during the adventure.
class npc_class:
    def __init__(self, name, charisma_check, bonus, reward):
        self.npc_name = name
        self.charisma_check = charisma_check
        self.name = bonus
        self.reward = reward


class monsters:
    def __init__(self, name, weakness, to_kill, reward, loot):
        self.name = name
        self.weakness = weakness
        self.to_kill = to_kill
        self.reward = reward
        self.loot = loot


class hidden_areas:
    def __init__(self, area, perception_check, enemy, shortname, verb, name, reward):
        self.area = area
        self.perception_check = perception_check
        self.enemy = enemy
        self.shortname = shortname
        self.verb = verb
        self.name = name
        self.reward = reward


class items:
    def __init__(self, name, perception_check, reward):
        self.name = name
        self.perception_check = perception_check
        self.reward = reward


class data:
    # chr Stats
    chr = {"Strength": 5, "Perception": 5, "Vigor": 5, "Charisma": 5}

    # Base narrative of the game
    story_narrative = ["Leaving Sparta's stoic mountains, you journey eastward, rugged terrain yielding to lush lands.", "You arrive in Athens, wisdom flourished, democracy thrived, its knowledge ignited a Spartan ember.",
                       "At Thermopylae, Leonidas' valor etched in stone, a shrine to honor sacrifice.",
                       "You see Susa's lavish courts, Persia's opulence unveiled, a stark contrast to Spartan simplicity.",
                       "You make it to Persepolis, an empire's heart, its grandeur and might held me captive.",
                       "The horizon revealed Persia's colossal army, an awe-inspiring force, ready for battle.",
                       "Spartan spirit unwavering, you face the Persian behemoth with resolve unbroken."]

    # Different types of encouters that can occur along the story
    encounters = ["monster_ambush",
                  "item_discovery", "hidden_area", "npc_found"]

    # Array of monsters,items and hidden areas you can find
    monsters = [
        monsters("Cyclops", "Eye", 15, "Strength", "Cyclops Hammer"),
        monsters("Hydra", "Stomach", 16, "Vigor", "Hydra Scale")
    ]
    items = [
        items("Poseidon's Trident", 10, "Strength"),
        items("Armor of Diomedes", 10, "Vigor")
    ]
    hidden_areas = [
        hidden_areas("Minotaur Maze", 12, "Minotaur", "maze",
                     "sleeping", "Minotaur Horn", "Charisma"),
        hidden_areas("Gorgon's Cave", 12, "Gorgon", "cave",
                     "dead", "Gorgon's Head", "Perception")
    ]
    npcs = [
        npc_class("Ray the Aoidos", 8, "Aoidos Inspiration", "Charisma"),
        npc_class("Hercules", 10, "Power of Hercules", "Strength")
    ]

    # Players Inventory
    Inventory = []
