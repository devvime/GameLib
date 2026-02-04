from pyray import *
from raylib import *

class Entity:
    def __init__(self, scene):
        self.scene = scene
        self.tags = { "floor": False }
        self.model = None
        self.position = Vector3()
        self.direction = Vector3()
        self.velocity = Vector3()
        self.is_grounded = False
        
    def destroy(self):
        unload_model(self.model)