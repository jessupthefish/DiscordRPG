import random


class Character:

    def __init__(self, name, hp, max_hp, attack, defense, xp, gold):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.xp = xp
        self.gold = gold

    def fight(self, other):
        defense = min(other.defense, 19)  # cap defense
        chance_to_hit = random.randint(0, 20 - defense)  # determine hit
        if chance_to_hit:
            damage = self.attack
        else:
            damage = 0

        other.hp -= damage  # apply damage

        return self.attack, other.hp <= 0  # damage, fatal
