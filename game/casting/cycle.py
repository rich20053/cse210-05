import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long Cycle with a trailing tail.
    
    The responsibility of cycle is to move itself and avoid other cycle tails.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._velocity = Point(0, -constants.CELL_SIZE)
        self.is_game_over = False
        self._segments = []
        self._prepare_body()

    def get_segments(self):
        return self._segments

    def move_next(self):
        # move all segments
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
        
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self.get_color())
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = self.get_cycle_x_start()
        y = self.get_cycle_y_start()
    
        for i in range(constants.CYCLE_LENGTH):
            position = Point(x, y + i * constants.CELL_SIZE)
            velocity = Point(0, -1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            color = self.get_color()
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
    
    def get_cycle_x_start(self):
        return(int(constants.CELL_SIZE * (constants.COLUMNS / 6)))

    def get_cycle_y_start(self):
        return(int(constants.CELL_SIZE * (constants.ROWS / 2)))
    
    def get_color(self):
        return(constants.RED)

    def set_game_over(self):
        self.is_game_over = True
  
    def is_game_over(self):
        return(self.is_game_over)
  

        