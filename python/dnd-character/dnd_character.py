import random

class Character:
    def __init__(self):
        self.strength = Character.ability_generator()
        self.dexterity = Character.ability_generator()
        self.constitution = Character.ability_generator()
        self.intelligence = Character.ability_generator()
        self.wisdom = Character.ability_generator()
        self.charisma = Character.ability_generator()

        self.const_modifier = modifier(self.constitution)
        self.hitpoints = self.const_modifier + 10

    def ability(self):
        return Character.ability_generator()

    @staticmethod
    def ability_generator():
        abilities = []
        for i in range(4):
            abilities.append(random.randint(1,6))
        sorted(abilities)
        return sum(abilities[1:])

def modifier(int):
    return (int - 10) // 2