import constants

from game.casting.cast import Cast
from game.casting.rscore import Rscore
from game.casting.lscore import Lscore
from game.casting.lcycle import Lcycle
from game.casting.rcycle import Rcycle
from game.casting.obstacle import Obstacle
from game.casting.prize import Prize
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("lcycle", Lcycle())
    cast.add_actor("rcycle", Rcycle())
    cast.add_actor("lscore", Lscore())
    cast.add_actor("rscore", Rscore())
   
    # add obstacles
    for n in range(constants.OBSTACLES):
        cast.add_actor("obstacles", Obstacle())

    # add prizes
    for n in range(constants.PRIZES):
        cast.add_actor("prizes", Prize())

    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("check", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()