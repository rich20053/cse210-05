from game.scripting.action import Action
PACE = 3

class MoveActorsAction(Action):
    """
    An update action that handles movement of the actors.
    
    The responsibility of MoveActorsAction is to move each actor according to its velocity.

    Attributes:
        ???????????
    """

    def __init__(self):
        self.pace = PACE
        self.speed = self.pace
        pass

    def execute (self, cast, script):
        all_actors = cast.get_all_actors()
        self.speed -= 1
        if self.speed == 0:
            self.speed = self.pace
            for actor in all_actors:
                actor.move_next()



