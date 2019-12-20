import os
import time

class storyAgent():
    """ Mother class used by narrator in story telling classes like the narrator or the arena
    attributs : none
    methods : pause
    """
    def __init__(self):
        pass


    def pause(self, waiting_time):
        """This function implements a pause between story flow and clear the screen"""
        time.sleep(waiting_time)
        os.system('cls||clear')