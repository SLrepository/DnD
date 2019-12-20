import random

class Character():
    """DnD main class used as generic character definition
    attributs: name, life, attack, defense, agility
    methods: attacks, escape
    """
    actions = {
        'a': 'attack',
        'f': 'flee'
    }

    def __init__(self, life, attack, defense, agility, name = False):
        self.name = name
        self.life = life
        self.attack = attack
        self.defense = defense
        self.agility = agility

    def fight(self, target):
        """This function triggers an attack between two oppoents.
        As a result life and defense attributs are impacted
        """
        print("{} is figthing against {}".format(self.name, target.name))
        # Give target the pportunity to avoid the attack
        # Exemple: 50% chance to dodge when agility set to 50
        if random.randrange(0,100) <= target.agility:
            print("{} has dodged opponent".format(target.name))
            return False
        # traget's life is reduced by opponent attack level less target's defense divided by 5
        target.life -= self.attack - (target.defense/5)
        # No negative life attribut allowed -> forced to 0
        if target.life < 0:
            target.life = 0
        print("{} life expectancy is now {}".format(target.name, target.life))
        return True

    def dodge(self):
        """This function trigger's character to dodge,  in short leave the fight"""
        # Lower agility
        agi = round(self.agility/5)
        if random.randrange(0,100) <= agi:
            return True
        return False

    def decision(self, action, enemy):
        """This function implements decided action (attack/flee)"""
        if action not in self.actions:
            print('In your dream!')
            return False
        if action == 'a':
            self.fight(enemy)
        elif action == 'f':
            if self.dodge():
                # Exception raised on successul escape as fight comes to an end
                print("Lucky you, that was a close shave!!")
                raise Exception('Well dodged hero!')
            else:
                print('The enemy is right in your back!')
        elif action == 'h':
            self.get_cure()
        return True

    def __repr__(self):
        return "{} : life = {}".format(self.name, self.life)
        
