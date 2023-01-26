import turtle

# custom MapScreen class so that we can update title and set key event handlers
class Screen(turtle._Screen):
    def __init__(self, title):
        super().__init__()
        turtle.TurtleScreen.__init__(self, Screen._canvas)
        if turtle.Turtle._screen is None:
            turtle.Turtle._screen = self

        self.title(title)
        self.setup(width=1.0, height=1.0)
        self.listen()

    def update_title(self, title):
        self.title(title)

    def set_key(self, func, key):
        self.onkey(func, key)
