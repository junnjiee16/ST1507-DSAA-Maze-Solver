# tile object, stores necessary metadata for the tile
class Tile:
    def __init__(self, coordinates, tile_type):
        self.coordinates = coordinates
        self.tile_type = tile_type # one of 4: road, wall, start, end
        
        # determine color of tile depending on tile type
        if self.tile_type == "road":
            color = "white"
        elif self.tile_type == "wall":
            color = "grey"
        elif self.tile_type == "start":
            color = "#61ff6e"
        elif self.tile_type == "end":
            color = "#56defc"
        else:
            raise ValueError("Invalid tile type")

        self.__color = color

    
    @property
    def color(self):
        return self.__color