# this class is needed in order to cycle through multiple objects
class ObjectStateManager:
    def __init__(self, objects):
        self.__objects = objects
        self.__object_index = 0

    @property
    def current(self):
        return self.__objects[self.__object_index]

    def next(self):
        self.__object_index = (self.__object_index + 1) % len(self.__objects) # modulo will help us to cycle through the different objects