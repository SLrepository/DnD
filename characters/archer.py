from .characters import Character

class Archer(Character):
    """Archer character class"""
    def __init__(self, name = False):
        super().__init__(350, 80, 30, 50, name)