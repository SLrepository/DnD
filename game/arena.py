from .story_agent import storyAgent

class Arena(storyAgent):
    """Battlefield class nursing the fight
    attributs : player, enemy
    methods: fighters_enter, fighters_leave, battle
    """

    def __init__(self):
        # character object attributes
        self.player = False
        self.enemy = False

    def fighters_enter(self, player, enemy):
        """Store characters objects attributs"""
        self.player = player
        self.enemy = enemy

    def fighters_leave(self):
        """Cear character object attributs"""
        self.player = False
        self.enemy = False

    def battle(self):
        """This function processes fight player's decision"""
        self.pause(2)
        # As long as both characters are alive
        while self.player.life > 0 and self.enemy.life > 0:
            try:
                action_allowed = False
                # check if the character able to start action
                while not action_allowed:
                    print("{} || {}".format(self.player, self.enemy))
                    action = input('Wot have you decided {} ? : '.format(self.player.actions)).lower()
                    action_allowed = self.player.decision(action, self.enemy)
            # Show character successfuly dodged
            except Exception as e:
                break
            # Enemie's turn, if alive
            if self.enemy.life > 0:
                self.enemy.fight(self.player)
            self.pause(4)
        # End the fight
        print('End of fight')
        self.fighters_leave()