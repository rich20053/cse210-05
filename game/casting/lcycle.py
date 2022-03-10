import constants
from game.casting.cycle import Cycle

class Lcycle(Cycle):
    """
    A long bicycle with a trailing tail.
    
    The responsibility of cycle is to move itself and avoid other cycle tails.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
    
    def get_cycle_x_start(self):
        return(int(constants.CELL_SIZE * (constants.COLUMNS / 6)))

    def get_cycle_y_start(self):
        return(int(constants.CELL_SIZE * (constants.ROWS / 2)))
    
    def get_color(self):
        return(constants.RED)
  

