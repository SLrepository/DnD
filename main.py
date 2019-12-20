from game.narrator import Narrator
from game.factory import Factory
from game.arena import Arena

if __name__ == '__main__':
    # Start a narrator's story
    narrator = Narrator()
    # Initiate battlefield
    arena = Arena()

    introduction = [
        "Your are in the army now.",
        "You will suffer terrible pain.",
        "Enjoy anyway!"
    ]
    narrator.tell(introduction)
    # Player to choose is character
    choice = narrator.choose_character()
    player = Factory.get_character(choice)
    narrator.player_customization(player)
    # Retrieve player's opponent from factory (an orc in this case)
    enemy = Factory.get_character('orc')
    enemy.name = 'Orkozy'

    # New season
    story = [
        'You enter in the darkest forest ever',
        'Frozen to death, your little body covered of mud ',
        'You are so desperate that you are about to commit suicide',
        'When an orc just pops up from nowhere with his hands full of blood',
    ]
    narrator.tell(story)

    # Start a fight till death
    arena.fighters_enter(player, enemy)
    arena.battle()
