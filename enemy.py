from character import Character


class Enemy(Character):

    def __init__(self, name, max_hp, attack, defense, xp, gold):
        super().__init__(name, max_hp, max_hp, attack, defense, xp, gold)
        self.enemy = self.__class__.__name__


def rehydrate(self, name, hp, max_hp, attack, defense, xp, gold, enemy):
    self.name = name
    self.hp = hp
    self.max_hp = max_hp
    self.attack = attack
    self.defense = defense
    self.xp = xp
    self.gold = gold


class GiantRat(Enemy):
    min_level = 1

    def __init__(self):
        super().__init__("🐀 Giant Rat", 2, 1, 1, 1, 1)  # HP, attack, defense, XP, gold


class GiantSpider(Enemy):
    min_level = 1

    def __init__(self):
        super().__init__("🕷️ Giant Spider", 3, 2, 1, 1, 2)  # HP, attack, defense, XP, gold


class Bat(Enemy):
    min_level = 1

    def __init__(self):
        super().__init__("🦇 Bat", 4, 2, 1, 2, 1)  # HP, attack, defense, XP, gold


class Crocodile(Enemy):
    min_level = 2

    def __init__(self):
        super().__init__("🐊 Crocodile", 5, 3, 1, 2, 2)  # HP, attack, defense, XP, gold


class Wolf(Enemy):
    min_level = 2

    def __init__(self):
        super().__init__("🐺 Wolf", 6, 3, 2, 2, 2)  # HP, attack, defense, XP, gold


class Poodle(Enemy):
    min_level = 3

    def __init__(self):
        super().__init__("🐩 Poodle", 7, 4, 1, 3, 3)  # HP, attack, defense, XP, gold


class Snake(Enemy):
    min_level = 3

    def __init__(self):
        super().__init__("🐍 Snake", 8, 4, 2, 3, 3)  # HP, attack, defense, XP, gold


class Lion(Enemy):
    min_level = 4

    def __init__(self):
        super().__init__("🦁 Lion", 9, 5, 1, 4, 4)  # HP, attack, defense, XP, gold


class Dragon(Enemy):
    min_level = 5

    def __init__(self):
        super().__init__("🐉 Dragon", 10, 6, 2, 5, 5)  # HP, attack, defense, XP, gold
