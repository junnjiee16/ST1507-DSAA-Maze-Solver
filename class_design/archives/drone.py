# drone object, stores metadata for drone
class Drone:
    def __init__(self, orientation=0):
        self.__orientation = orientation

    @property
    def orientation(self):
        return self.__orientation

    @orientation.setter
    def orientation(self, value):
        self.__orientation = value