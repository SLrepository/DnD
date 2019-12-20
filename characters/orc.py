from .characters import Character

class Orc(Character):
    """Orc character class"""
    def __init__(self, name = ""):
        super().__init__(400, 40, 70, 20, name)