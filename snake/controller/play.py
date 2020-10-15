"""
Controller for playing the game
"""
import time
from snake.views import window
from snake.models import snake
from snake.models import food

# Create instances from classes
screen = window.Window()
player = snake.Snake()
target = food.Food()


# Function that change direction of snake
def up():
    if player.direction != "down":
        player.direction = "up"

def down():
    if player.direction != "up":
        player.direction = "down"

def left():
    if player.direction != "right":
        player.direction = "left"

def right():
    if player.direction != "left":
        player.direction = "right"



def play_game():
    """
    Main function for playing the game
    """
    screen.update()
    
    score = 0
    high_score = 0
    delay = 0.1
    
    # methods for listening keyboard action
    screen.window.listen()
    screen.window.onkeypress(up, "Up")
    screen.window.onkeypress(down, "Down")
    screen.window.onkeypress(left, "Left")
    screen.window.onkeypress(right, "Right")
    screen.window.onkeypress(screen.window.bye, "Escape")
    
    # Main loop when playing
    while True:
        
        # Check if the snake collided with the border or body
        if player.collision_with_the_border() \
            or player.collision_with_the_body():
            score = 0
            delay = 0.1
            
        # Check if the snake could get the food
        if player.snake.distance(target.food) < 20:
            player.add_snake_length()
            target.move_to_random_place()
            score += 10
            delay -= 0.001
        
        high_score = max(score, high_score)
        screen.update_score(score, high_score)
        player.update_snake_tails_position()
        player.move()
        screen.update()
        time.sleep(delay)

    screen.window.mainloop()