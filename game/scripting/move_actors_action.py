from game.scripting.action import Action
PACE = 3

# TODO: Implement MoveActorsAction class here! 

# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor

class MoveActorsAction(Action):
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



