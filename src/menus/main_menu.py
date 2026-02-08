from pyray import *
from raylib import *
from engine.entity import Entity
from engine.button import Button

class MainMenu(Entity):
    def __init__(self, scene):
        super().__init__(scene)


    def draw(self):
        draw_text("Hello world", 580, 290, 20, VIOLET)
        play_button = Button(x=540, y=330, w=200, h=50, text="Play", text_x=77, text_y=15)
        exit_button = Button(x=540, y=390, w=200, h=50, text="Exit", text_x=77, text_y=15)
        
        if play_button.draw():
            self.scene.game.set_scene("game")
            
        if exit_button.draw():
            self.scene.game.close()