from pyray import *
from raylib import *
from os.path import join

class Ship:
    def __init__(self):
        self.ship = load_model(join("assets", "models", "ship.glb"))
        self.position = Vector3()
        
    def draw(self):
        draw_model(self.ship, self.position, 1, WHITE)
        
    def update(self, dt):
        ...