from .characters import Character

class Warrior(Character):
    """Warrior character lassc"""
    def __init__(self, name = False):
        super().__init__(500, 50, 80, 10, name)