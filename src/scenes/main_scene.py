from src.settings import *
from engine.button import Button

class MainScene:
    def __init__(self, game):
        self.game = game
        
    def create(self):
        print("Main scene created!")
    
    def draw_2d(self):
        draw_text("Hello world", 580, 290, 20, VIOLET)
        self.button()
    
    def draw_3d(self):
        pass
    
    def update(self, dt):
        pass
    
    def button(self):
        play_button = Button(x=540, y=330, w=200, h=50, text="Play", text_x=77, text_y=15)
        exit_button = Button(x=540, y=390, w=200, h=50, text="Exit", text_x=77, text_y=15)
        
        if play_button.draw():
            self.game.set_scene("game")
            
        if exit_button.draw():
            self.game.close()