from .story_agent import storyAgent

class Narrator(storyAgent):
    """ Story telling and player character choice class.
        attributs: none
        methods: tell, choose_character, player_customization
    """

    roles = {
        "warrior" : "warrior",
        "archer" : "archer",
        "wizzard" : "wizzard"
    }

    def __init__(self):
        pass

    def tell(self, story):
        """Function implements the story flow from a given list, including the pauses"""
        if not isinstance(story, list):
            raise ValueError("Narator class method tell expects a list as argument")
        for sentence in story:
            self.pause(3)
            print(sentence)

    def choose_character(self):
        """this function allows the player to choose a character out of the roles list
           Leave infinite loop as soon as a valid character has been chosen
        """
        self.pause(3)
        print("""First you need to chosse the character you want to play, between the followings:
- A warrior, brutal but efficient
- An archer, accurate and agile
- A wizzard, a cunning and mystical character""")
        while True:
            try:
                player_choice = input('I choose the : ').lower()
                # Check if player_choice is a valid role
                player_class = Narrator.roles[player_choice]
                break
            except:
                print('No idea whom you are talking about, mate')
        return player_class

    def player_customization(self, player):
        """This function assigns the name of the chosen character"""
        self.pause(1)
        name = input("What is your rogue name ? : ")
        player.name = name
