from .characters import Character

class Zombie(Character):
    """ Zombie character class """
    def __init__(self, name = False):
        super().__init__(600, 15, 15, 5, name)
        