# tile object, stores metadata for the tile
class Tile:
    def __init__(self, coordinates, tile_type):
        self.coordinates = coordinates
        self.tile_type = tile_type # one of 4: road, wall, start, end
        
        # determine color of tile
        if self.tile_type == "road":
            self.color = "white"
        elif self.tile_type == "wall":
            self.color = "grey"
        elif self.tile_type == "start":
            self.color = "#61ff6e"
        else:
            self.color = "#56defc"