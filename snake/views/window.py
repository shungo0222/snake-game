import turtle

class Window(object):
    """
    Class of window object
    """
    
    def __init__(self):
        """
        Initialize a window instance
        """
        self.window = turtle.Screen()
        self.window.title('Snake Game')
        self.window.bgcolor('black')
        self.window.setup(width=700, height=700)
        self.window.tracer(0)
        self.draw_grid() # draw a grid line
        self.pen = turtle.Turtle()
        self.display_score() # write the score 
        
    def update(self):
        """
        Update the window
        """
        self.window.update()
        
    def draw_grid(self):
        """
        Draw a grid line
        """
        coordinates = [[-290, 270], [-310, -310]]
        
        for i in range(2):
            line = turtle.Turtle()
            line.hideturtle()
            line.color('white')
            if not i:
                line.right(90)
            for _ in range(30 - i):
                line.penup()
                line.goto(coordinates[i][0], coordinates[i][1])
                line.pendown()
                if i:
                    line.forward(620)
                else:
                    line.forward(600)
                coordinates[i][i] += 20
                
        line.penup()
        line.goto(-310, 270)
        line.pendown()
        line.width(5)
        for i in range(4):
            if i % 2:
                line.forward(600)
            else:
                line.forward(620)
            line.right(90)
            
    def display_score(self):
        """
        Display the score board
        """
        self.pen.speed(0)
        self.pen.color("green")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0,300)
        self.pen.write("Score: 0  High Score: 0", \
                        align="center", font=("Courier", 25, "normal"))
        
    def update_score(self, score, high_score):
        """
        Update the score board
        """
        self.pen.clear()
        self.pen.write("Score: {}  High Score: {}".format(score, high_score), \
                        align="center", font=("Courier", 25, "normal"))