import random
from gamemode import GameMode
from enemy import Enemy
from game import str_to_class
from character import Character
from database_handler import RPGDatabase


class Player(Character):
    level_cap = 10

    def __init__(self, name, hp, max_hp, attack, defense, mana, level, xp, gold, inventory, mode, battling, user_id):
        super().__init__(name, hp, max_hp, attack, defense, xp, gold)
        self.mana = mana
        self.level = level

        self.inventory = inventory
        self.mode = mode
        self.battling = battling
        if battling is not None:
            enemy_class = str_to_class(battling["enemy"])
            self.battling = enemy_class()
            self.battling.rehydrate(**battling)
        else:
            self.battling = None
        self.user_id = user_id

    def hunt(self):
        # Generate random enemy to fight
        while True:
            enemy_type = random.choice(Enemy.__subclasses__())

            if enemy_type.min_level <= self.level:
                break

        enemy = enemy_type()

        # Enter battle mode
        self.mode = GameMode.BATTLE
        self.battling = enemy

        # Save changes to DB after state change
        RPGDatabase.save_to_db(self)

        return enemy
