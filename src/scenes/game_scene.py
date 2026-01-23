from src.settings import *

class GameScene:
    def __init__(self, game):
        self.game = game
    
    def draw_2d(self):
        draw_text("Game Scene is working!", 190, 200, 20, VIOLET)
    
    def draw_3d(self):
        pass
    
    def update(self, dt):
        if is_key_pressed(KEY_ESCAPE):
            self.game.set_scene(self.game.scenes["main"])