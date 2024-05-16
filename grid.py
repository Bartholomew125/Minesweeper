from tile import Tile

class Grid:

    def __init__(self, screen, width, height):
        self.screen = screen
        self.screen_height = screen.get_height()
        self.screen_width = screen.get_width()
        self.width = width
        self.height = height

        y_offset = 0
        x_offset = 0

        if self.height >= self.width:
            size = self.screen_height/self.height
            x_offset = self.screen_width/2 - (self.width*size)/2
        
        if self.width > self.height:
            size = self.screen_width/self.width
            y_offset = self.screen_height/2 - (self.height*size)/2

        self.tiles = []
        for i in range(self.width):
            for j in range(self.height):
                x = i*size + x_offset
                y = j*size + y_offset
                tile = Tile(self.screen, x, y, size, size, 0.2)
                self.tiles.append(tile)
    
    def update(self, mouse):
        for tile in self.tiles:
            if tile.rect.collidepoint(mouse.pos):
                tile.color = (128, 128, 128)
                if mouse.left_click:
                    tile.show()
            else:
                tile.color = tile.og_color

    def draw(self):
        for tile in self.tiles:
            tile.draw()