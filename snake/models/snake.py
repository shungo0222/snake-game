import time
import turtle

class Snake(object):
    """
    Class of snake object
    """
    
    def __init__(self, shape='square', color='blue'):
        """
        Initialize snake instance and place it on center
        """
        self.snake = turtle.Turtle()
        self.snake.speed(0)
        self.snake.shape(shape)
        self.snake.color(color)
        self.snake.penup()
        self.snake.goto(0, 0) # place on center
        self.direction = "stop"
        self.length = [] # snake body
        
    def move(self):
        """
        Make the snake move in the direction
        """
        if self.direction == "up":
            y = self.snake.ycor()
            self.snake.sety(y + 20)
        
        if self.direction == "down":
            y = self.snake.ycor()
            self.snake.sety(y - 20)
        
        if self.direction == "left":
            x = self.snake.xcor()
            self.snake.setx(x - 20)
        
        if self.direction == "right":
            x = self.snake.xcor()
            self.snake.setx(x + 20)
            
    def collision_with_the_border(self):
        """
        Check if the snake collided with the border
        
        Returns
        -------
        True : Boolean
            It means the snake collided with the border
        """
        if (self.snake.xcor() > 310) or (self.snake.xcor() < -310) \
            or (self.snake.ycor() > 260) or (self.snake.ycor() < -320):
            time.sleep(1)
            self.snake.goto(0, 0)
            self.direction = "stop"
            # Move the snake body outside of the window to reset
            for snake in self.length:
                snake.goto(1000, 1000)
            self.length.clear()
            return True
        
    def collision_with_the_body(self):
        """
        Check if the snake collided with the body
        
        Returns
        -------
        True : Boolean
            It means the snake collided with the body
        """
        for body in self.length:
            if body.distance(self.snake) < 20:
                time.sleep(1)
                self.snake.goto(0, 0)
                self.snake.direction = "stop"
                # Move the snake body outside of the window to reset
                for snake in self.length:
                    snake.goto(1000, 1000)
                self.length.clear()
                return True

    def add_snake_length(self):
        """
        When the snake can get the food, add the snake length
        """
        new_snakeLength = turtle.Turtle()
        new_snakeLength.speed(0)
        new_snakeLength.shape("square")
        new_snakeLength.color("white")
        new_snakeLength.penup()
        self.length.append(new_snakeLength)
        
    def update_snake_tails_position(self):
        """
        Update the snake body position by moving squares one by one
        """
        for index in range(len(self.length)-1, 0, -1):
            x = self.length[index-1].xcor()
            y = self.length[index-1].ycor()
            self.length[index].goto(x, y)
        if len(self.length) > 0:
            x = self.snake.xcor()
            y = self.snake.ycor()
            self.length[0].goto(x, y)