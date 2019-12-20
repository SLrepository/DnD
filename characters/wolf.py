from .characters import Character

class Wolf(Character):
    """ Wolf character class """
    def __init__(self, name = False):
        super().__init__(300, 30, 15, 40, name)