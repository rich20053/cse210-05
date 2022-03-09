# cse210-05
Team Repository for Cycle program

# Cycle Game 

Cycle is played according to the following rules.

Players can move up, down, left and right...
Player one moves using the W, S, A and D keys.
Player two moves using the I, K, J and L keys.
Each player's trail grows as they move.
Players try to maneuver so the opponent collides with their trail.
If a player collides with their opponent's trail...
A "game over" message is displayed in the middle of the screen.
The cycles turn white.
Players keep moving and turning but don't run into each other.

# Extra Functionality

1. We have added a new Game Over message with the ability to restart the game by pressing the letter 'n'.
2. We have added a point for each turn a player makes to enhance the point collection.
3. We have added some obstacles represented by a yellow letter 'O'.  If a player hits them, he loses the game.
4. We have added some prizes represented by a blue '*'.  If a player hits them, he gets 25 points and the prize is removed.
5. We have added the ability to change the speed.  A player can press the numbers 1-5 and change speed with 1 being the slowest and 5 being the fastest.

# Files

__main__.py
director.py
actor.py
cast.py
cycle.py
lcycle.py
rcycle.py
score.py
lscore.py
rscore.py
obstacle.py
prize.py
script.py
action.py
control_actors_action.py
move_actors_action.py
handle_collisions_action.py
draw_actors_action.py
point.py
color.py
keyboard_service.py
video_service.py

# Classes

classes: 
	__main__/constants (Mark)
	Director 
	Point
	Color
	VideoService
	KeyboardService
	Cast
	Actor
	Cycle (Jake)
	Lcycle (Jake)
	Rcycle (Jake)
	Score (Johanna)
	Lscore (Johanna)
	Rscore (Johanna)
	Obstacle (Mark)
	Prize (Mark)
	Script
	Action
	ControlActorsAction (Alexander)
	DrawActorsAction (Didier)
	HandleCollisionsAction (Alexander)
	MoveActorsAction (Didier)

# Team

Alexander Calva
Mark Richmond
Johanna Schick
Jake Soulier
Didier Virguez

