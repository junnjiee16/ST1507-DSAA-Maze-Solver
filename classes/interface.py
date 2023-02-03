import turtle

# custom interface class so that we can update title and set key event handlers
class Interface(turtle._Screen):
    """
    A Interface is a turtle Screen.
    This allows us to set custom key handlers and update the title bar.
    """
    def __init__(self, title):
        super().__init__()
        turtle.TurtleScreen.__init__(self, Interface._canvas)
        if turtle.Turtle._screen is None:
            turtle.Turtle._screen = self

        self.title(title)
        self.setup(width=1.0, height=1.0)
        self.listen()


