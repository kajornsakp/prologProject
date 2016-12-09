from Character import MapTile
from tmx import tmx


class TileMap:
    def __init__(self,tilemap,screen):
        self.screen = screen
        self.tilemap = tmx.load(tilemap, screen.get_size())
        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers['wall'].find('wall')[0]
        self.wall = MapTile(start_cell.px,start_cell.py,self.sprites)
        self.tilemap.layers.append(self.sprites)

        for wall in self.tilemap.layers['wall'].find('wall'):
            MapTile()