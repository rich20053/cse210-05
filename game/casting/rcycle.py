import constants
from game.casting.cycle import Cycle

class Rcycle(Cycle):
    """
    A long bicycle with a trailing tail.
    
    The responsibility of cycle is to move itself and avoid other cycle tails.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        """Constructs a new Cycle.
        
        Args:
            None.
        """
        super().__init__()

    def get_cycle_x_start(self):
        """Gets the cycle's start position x value.
        
        Returns:
            int: The cycle's start position x value.
        """
        return(int(constants.CELL_SIZE * (constants.COLUMNS / 6) * 5))

    def get_cycle_y_start(self):
        """Gets the cycle's start position y value.
        
        Returns:
            int: The cycle's start position y value.
        """
        return(int(constants.CELL_SIZE * (constants.ROWS / 2)))
    
    def get_color(self):
        """Gets the cycle's color.
        
        Returns:
            color: The cycle's color (r, g, b).
        """
        return(constants.GREEN)
  
