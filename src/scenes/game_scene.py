from src.settings import *
from src.entities.ship import Ship

class GameScene:
    def __init__(self, game):
        self.game = game
        
    def create(self):
        self.ship = Ship()
    
    def draw_2d(self):
        ...
    
    def draw_3d(self):
        draw_grid(10, 0.5)
        self.ship.draw()
    
    def update(self, dt):
        if is_key_pressed(KEY_ESCAPE):
            self.game.set_scene("main")
            
        self.ship.update(dt)