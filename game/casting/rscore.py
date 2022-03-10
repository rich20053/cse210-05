from game.casting.score import Score
from game.shared.point import Point

MAX_X = 900

class Rscore(Score):
    """
    A record of points made or lost for the right side. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self.max_x = MAX_X - 100
        self._position = Point(self.max_x, 0)
