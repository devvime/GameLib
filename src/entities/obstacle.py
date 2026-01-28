from pyray import *
from raylib import *
from engine.entity import Entity

class Obstacle(Entity):
    def __init__(self, scene, position = Vector3(), scale = Vector3(1, 1, 1), color=GRAY):
        super().__init__(scene)
        self.position = position
        self.scale = scale
        self.color = color
        self.tags["floor"] = True
        self.model = load_model_from_mesh(gen_mesh_cube(self.scale.x, self.scale.y, self.scale.z))
        
    def draw(self):
        draw_model(self.model, self.position, 1, self.color)
        
    def update(self, dt):
        ...