from random import randint

class Die():
    """Class representing a die"""
    
    def __init__(self,sides = 6):
        """Initializes die attributes"""
        self.sides = sides
        
    def roll(self):
        """Return a value between 1 and the number of sides"""
        return randint(1,self.sides)
