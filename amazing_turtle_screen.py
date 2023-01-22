import turtle

class MapScreen(turtle._Screen):
    def __init__(self, title):
        super().__init__()
        turtle.TurtleScreen.__init__(self, MapScreen._canvas)
        if turtle.Turtle._screen is None:
            turtle.Turtle._screen = self

        self.title(title)
        self.listen()

    def update_title():
        pass

    def set_key(self, key, func):
        self.onkey(func, key)


class tortoise(turtle.Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.pendown()

    def move(self):
        self.forward(100)

    def turn(self):
        self.left(90)


screen = MapScreen("wowowo")
pointer = tortoise()

screen.set_key("r", lambda: pointer.move() or pointer.turn())

screen.mainloop()