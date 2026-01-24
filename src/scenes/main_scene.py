from src.settings import *
from src.engine.button import Button

class MainScene:
    def __init__(self, game):
        self.game = game
    
    def draw_2d(self):
        draw_text("Hello world", 335, 150, 20, VIOLET)
        self.button()        
    
    def draw_3d(self):
        pass
    
    def update(self, dt):
        pass
    
    def button(self):
        play_button = Button(300, 220, 200, 50, "JOGAR", text_x=370, text_y=235)
        
        if play_button.draw():
            self.game.set_scene(self.game.scenes["game"])