from src.settings import *
from engine.scene import Scene
from src.menus.main_menu import MainMenu

class MainScene(Scene):
    def __init__(self, game):
        super().__init__(game)


    def create(self):
        self.main_menu = MainMenu(self)


    def draw_2d(self):
        super().draw_2d()        
        self.main_menu.draw()

    
    def draw_3d(self):
        super().draw_3d()

    
    def update(self, dt):
        super().update(dt)


    def destroy(self):
        return super().destroy()