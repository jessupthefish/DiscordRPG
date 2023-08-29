class Character(Actor):

    level_cap = 10

    def __init__(self, name, hp, max_hp, attack, defense, mana, level, xp, gold, inventory, mode, battling, user_id):
        super().__init__(name, hp, max_hp, attack, defense, xp, gold)
        self.mana = mana
        self.level = level
