from pyray import *
from raylib import *
from os.path import join
from engine.entity import Entity

class Ship(Entity):
    def __init__(self, scene):
        super().__init__(scene)
        self.model = load_model(join("assets", "models", "ship.glb"))
        self.position = Vector3(0, 2, 0)
        
    def draw(self):
        draw_model(self.model, self.position, 1, WHITE)
        
    def update(self, dt):
        ...