from .characters import Character

class Wizzard(Character):
    """Wizzard character class.
    Attributs: mana
    methods = heal, __repr__"""
    actions: Character.actions.update({'h': 'heal itself'})

    def __init__(self, name = False):
        super().__init__(600, 20, 50, 25, name)
        # Magical attribut
        self.mana = 200

    def get_cure(self):
        """This function brings additionnal amount of life to the wizzard thanks to his supernatural power (or mana)"""
        # Needs 50 pts of mana to heal itself
        if self.mana >= 50:
            print("{} uses some of his supernatural power".format(self.name))
            self.mana -= 50
            self.life += 20
            print("{} regains 20 pts of life, now : {}".format(self.name, self.life))
        else :
            print("{} has lost most of his mana, sorry".format(self.name))

    def __repr__(self):
        return "{} : life = {}, mana = {}".format(self.name, self.life, self.mana)