# this class is needed in order to cycle through multiple objects
class ObjectStateManager:
    '''
    This class is used to cycle through multiple objects
    Parameters:
        objects (list): list of objects
    Attributes:
        objects (list): list of objects
        object_index (int): index of the current object
    '''
    def __init__(self, objects):
        self.__objects = objects
        self.__object_index = 0

    @property
    def current(self):
        return self.__objects[self.__object_index]

    def next(self):
        self.__object_index = (self.__object_index + 1) % len(self.__objects) # modulo will help us to cycle through the different objects
