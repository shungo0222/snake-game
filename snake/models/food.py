import turtle
import random

class Food(object):
    """
    Class of food object
    """
    
    def __init__(self, shape='circle', color='red'):
        """
        Initialize food instance and place it randomly
        """
        self.food = turtle.Turtle()
        self.food.speed(0)
        self.food.shape(shape)
        self.food.color(color)
        self.food.penup()
        self.food_x = random.randrange(-300, 320, 20)
        self.food_y = random.randrange(-320, 280, 20)
        self.food.goto(self.food_x, self.food_y)
        
    def move_to_random_place(self):
        """
        When the snake can get the food, replace the food randomly
        """
        self.food_x = random.randrange(-300, 320, 20)
        self.food_y = random.randrange(-320, 280, 20)
        self.food.goto(self.food_x, self.food_y)